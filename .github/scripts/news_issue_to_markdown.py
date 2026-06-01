#!/usr/bin/env python3
"""Create a sanitized Hugo news Markdown file from a GitHub Issue Form event."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse


EXPECTED_LABEL = "news-vorschlag"
APPROVAL_LABEL = "freigegeben"
ALLOWED_AUDIENCES = {"Schüler:innen", "Eltern", "Lehrkräfte", "SEB", "Allgemein"}
AUDIENCE_ALIASES = {"Schülerinnen und Schüler": "Schüler:innen"}
ALLOWED_CATEGORIES = {
    "KI",
    "Informatik",
    "Veranstaltung",
    "Wettbewerb",
    "Material",
    "Empfehlung",
    "Hinweis",
    "Sonstiges",
}
FIELD_ALIASES = {
    "Kurzbeschreibung": "abstract",
    "Details oder externer Link (optional)": "details",
    "Zielgruppe": "audience",
    "Thema/Kategorie": "category",
    "Kategorie": "category",
    "GAK/SEB-Relevanz": "relevance",
    "Datenschutz-Bestätigung": "no_pii",
}
NO_RESPONSE = {"", "_No response_", "No response"}
PII_PATTERNS = [
    re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"),
    re.compile(r"(?<!\d)(?:\+?\d[\d\s()./-]{7,}\d)(?!\d)"),
]


class NewsError(ValueError):
    pass


def read_event() -> dict:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise NewsError("GITHUB_EVENT_PATH fehlt.")
    return json.loads(Path(event_path).read_text(encoding="utf-8"))


def issue_labels(issue: dict) -> set[str]:
    return {label.get("name", "") for label in issue.get("labels", [])}


def parse_issue_form(body: str) -> dict[str, str]:
    fields: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        if line.startswith("### "):
            label = line[4:].strip()
            current = FIELD_ALIASES.get(label)
            if current:
                fields[current] = []
            continue
        if current:
            fields[current].append(line)
    return {key: "\n".join(value).strip() for key, value in fields.items()}


def clean_text(value: str, limit: int, field: str) -> str:
    value = value.strip()
    if value in NO_RESPONSE:
        return ""
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", value)
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value).strip()
    if len(value) > limit:
        raise NewsError(f"{field} ist zu lang (maximal {limit} Zeichen).")
    return value


def parse_multi(value: str, allowed: set[str], field: str) -> list[str]:
    items: list[str] = []
    for raw in value.splitlines():
        entry = raw.strip()
        if entry.startswith("- "):
            entry = entry[2:].strip()
        if entry in NO_RESPONSE:
            continue
        if not entry:
            continue
        entry = AUDIENCE_ALIASES.get(entry, entry)
        if entry not in allowed:
            raise NewsError(f"Ungültiger Wert in {field}: {entry}")
        if entry not in items:
            items.append(entry)
    if not items:
        raise NewsError(f"{field} fehlt.")
    return items


def split_details_and_link(value: str) -> tuple[str, str]:
    value = clean_text(value, 2000, "Details oder externer Link")
    if not value:
        return "", ""
    urls = re.findall(r"https?://[^\s<>)\"']+", value)
    external_link = ""
    if urls:
        candidate = urls[0].rstrip(".,;:")
        parsed = urlparse(candidate)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise NewsError("Externer Link ist keine gültige http(s)-URL.")
        external_link = candidate
        value = value.replace(candidate, "").strip()
    return value, external_link


def clean_issue_title(value: str) -> str:
    title = clean_text(value, 100, "Issue-Titel")
    title = re.sub(r"^\[Neuigkeit\]\s*:?\s*", "", title, flags=re.I).strip()
    return clean_text(title, 80, "Issue-Titel")


def validate_no_pii(fields: dict[str, str]) -> None:
    confirmation = fields.get("no_pii", "")
    if "[x]" not in confirmation.lower():
        raise NewsError("Datenschutz-Bestätigung fehlt.")
    combined = "\n".join(
        fields.get(key, "") for key in ("title", "abstract", "details", "relevance")
    )
    for pattern in PII_PATTERNS:
        if pattern.search(combined):
            raise NewsError("Mögliche personenbezogene Daten gefunden (E-Mail oder Telefonnummer). Bitte Issue bereinigen.")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return slug[:60].strip("-") or "neuigkeit"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join(yaml_string(value) for value in values) + "]"


def markdown_plain(value: str) -> str:
    value = value.replace("\\", "\\\\")
    return re.sub(r"([`*_{}\[\]()#+.!<>|-])", r"\\\1", value)


def write_output(name: str, value: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with Path(output_path).open("a", encoding="utf-8") as handle:
        handle.write(f"{name}={value}\n")


def main() -> int:
    event = read_event()
    issue = event.get("issue", {})
    labels = issue_labels(issue)
    if EXPECTED_LABEL not in labels:
        raise NewsError(f"Nur Issues mit Label '{EXPECTED_LABEL}' werden verarbeitet.")
    if APPROVAL_LABEL not in labels:
        raise NewsError(f"Freigabelabel '{APPROVAL_LABEL}' fehlt.")

    fields = parse_issue_form(issue.get("body") or "")
    fields["title"] = clean_issue_title(issue.get("title") or "")
    required = ["title", "abstract", "audience", "category", "no_pii"]
    missing = [field for field in required if not fields.get(field) or fields.get(field) in NO_RESPONSE]
    if missing:
        raise NewsError("Pflichtfelder fehlen: " + ", ".join(missing))

    validate_no_pii(fields)
    title = clean_text(fields["title"], 80, "Titel")
    abstract = clean_text(fields["abstract"], 220, "Kurzbeschreibung")
    relevance = clean_text(fields.get("relevance", ""), 600, "GAK/SEB-Relevanz")
    details, external_link = split_details_and_link(fields.get("details", ""))
    audiences = parse_multi(fields["audience"], ALLOWED_AUDIENCES, "Zielgruppe")
    categories = parse_multi(fields["category"], ALLOWED_CATEGORIES, "Thema/Kategorie")

    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    slug = slugify(title)
    issue_number = issue.get("number")
    file_path = Path("content") / "news" / f"{today}-{slug}.md"

    lines = [
        "---",
        f"title: {yaml_string(title)}",
        f"date: {today}",
        "draft: false",
        f"categories: {yaml_list(categories)}",
        f"audiences: {yaml_list(audiences)}",
        f"abstract: {yaml_string(abstract)}",
        "sample: false",
        f"source_issue: {issue_number}",
    ]
    if external_link:
        lines.append(f"external_link: {yaml_string(external_link)}")
    lines.extend(["---", "", markdown_plain(abstract)])
    if relevance:
        lines.extend(["", "## Relevanz für GAK/SEB", "", markdown_plain(relevance)])
    if details:
        lines.extend(["", "## Details", "", markdown_plain(details)])
    if external_link:
        lines.extend(["", "## Externer Link", "", f"[Geprüften Link öffnen]({external_link})"])
    lines.append("")

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("\n".join(lines), encoding="utf-8")

    write_output("file", str(file_path).replace("\\", "/"))
    write_output("slug", slug)
    write_output("title", title)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NewsError as exc:
        print(f"Fehler: {exc}", file=sys.stderr)
        raise SystemExit(1)
