import json
import sys
from pathlib import Path


REQUIRED_TOP = [
    "column_name",
    "issue_type",
    "issue_title",
    "issue_date",
    "intro",
    "news_items",
    "ending_observation",
    "footer",
]

REQUIRED_ITEM = [
    "title",
    "short_title",
    "source",
    "date",
    "url",
    "keywords",
    "fact",
    "why_matters",
    "work_relevance",
    "screen_text",
    "verify_status",
]


def clen(value):
    return len(str(value).strip())


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_current_json.py <data/current.json>")
        return 2

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    warnings = []

    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"missing top-level field: {key}")

    items = data.get("news_items", [])
    if not isinstance(items, list):
        errors.append("news_items must be a list")
        items = []

    if len(items) == 0:
        errors.append("news_items is empty")
    if len(items) > 8:
        warnings.append("news_items has more than 8 items; extended weekly template shows first 8")

    for idx, item in enumerate(items, 1):
        for key in REQUIRED_ITEM:
            if key not in item:
                errors.append(f"item {idx}: missing field {key}")
        if len(item.get("keywords", [])) > 3:
            errors.append(f"item {idx}: keywords has more than 3 entries")
        if clen(item.get("short_title", "")) > 18:
            warnings.append(f"item {idx}: short_title may be too long")
        if clen(item.get("screen_text", "")) > 36:
            warnings.append(f"item {idx}: screen_text may be too long")
        if not item.get("url"):
            warnings.append(f"item {idx}: url is empty")
        if item.get("verify_status") != "已核验":
            warnings.append(f"item {idx}: verify_status is {item.get('verify_status')!r}")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")

    if errors:
        return 1
    print(f"OK: {path} has {len(items)} news item(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
