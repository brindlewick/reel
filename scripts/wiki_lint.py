#!/usr/bin/env python3
"""Check the wiki, so that its rules are run rather than remembered.

    python3 scripts/wiki_lint.py [<repo>]    default: the repository this script is in

Prints one fault per line and fixes none: a fault means a page or the index is wrong, and which
one is a judgement for a person. Exit 0 when clean, 1 when there are faults, and 2 on a usage
error or when there is no wiki to check.

lint() is a pure function of the repository's files, so the tests run every check on fixtures
in memory. Only collect() and main() touch the disk.
"""
from __future__ import annotations

import os
import posixpath
import re
import sys
from pathlib import Path

TYPES = ("concept", "decision", "schema", "source")
STATUSES = ("decided", "open", "superseded")
STANDINGS = ("claimed", "mixed", "refuted", "settled", "supported")
INDEX = "wiki/index.md"
SKIP_DIRS = {".git", ".worktrees", "node_modules", "__pycache__"}

DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
LINK = re.compile(r"\]\(([^)\s]+)\)")
CITATION = re.compile(r"\[@([a-z]+)/([^\]\s]+)\]")
SOURCE = re.compile(r"([a-z]+)/([^,\]\s]+)")
INDEX_LINE = re.compile(r"^\s*[-*]\s+\[[^\]]+\]\(([^)\s]+)\)(.*)$")


def front_matter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return dict(re.findall(r"^([a-z_]+):[ \t]*(.*?)[ \t]*$", text[4:end], re.M))


def prose(text: str) -> str:
    """The text without code: notation shown in backticks is an example, not a link."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def local(target: str) -> str | None:
    """The path of a relative link, or None for an external link or an anchor."""
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    return target.split("#")[0]


def resolve(page: str, path: str) -> str:
    return posixpath.normpath(posixpath.join(posixpath.dirname(page), path))


def exists(files: dict[str, str], path: str) -> bool:
    path = path.rstrip("/")
    return path in files or any(f.startswith(path + "/") for f in files)


def lint(files: dict[str, str]) -> list[str]:
    """Every fault in a repository, given as {path relative to the repository: text}."""
    pages = sorted(p for p in files if p.startswith("wiki/") and p.endswith(".md"))
    faults: list[str] = []
    meta: dict[str, dict[str, str]] = {}
    for page in pages:
        fm = front_matter(files[page])
        if fm is None:
            faults.append(f"{page}: no front matter")
            continue
        meta[page] = fm
        faults += check_page(files, page, fm)
    return faults + check_index(files, pages, meta) + check_raw(files)


def check_page(files: dict[str, str], page: str, fm: dict[str, str]) -> list[str]:
    faults = [f"{page}: front matter has no {key}" for key in ("title", "type", "updated") if key not in fm]
    kind = fm.get("type")
    if kind is not None and kind not in TYPES:
        faults.append(f"{page}: type {kind!r} is not one of {', '.join(TYPES)}")

    sources = SOURCE.findall(fm.get("sources", ""))
    for group, slug in sources:
        if not exists(files, f"raw/{group}/{slug}"):
            faults.append(f"{page}: source {group}/{slug} does not resolve under raw/")
    if kind == "decision":
        faults += check_decision(page, fm)
    elif kind == "concept":
        faults += check_concept(page, fm, [group for group, _ in sources])

    text = prose(files[page])
    for group, ident in CITATION.findall(text):
        ident = ident.rstrip("/.,;")
        if not exists(files, f"raw/{group}/{ident}"):
            faults.append(f"{page}: citation [@{group}/{ident}] does not resolve under raw/")
    for target in LINK.findall(text):
        path = local(target)
        if path and not exists(files, resolve(page, path)):
            faults.append(f"{page}: link to {target} does not resolve")
    return faults


def check_decision(page: str, fm: dict[str, str]) -> list[str]:
    status = fm.get("status")
    if status is None:
        return [f"{page}: decision with no status"]
    if status not in STATUSES:
        return [f"{page}: status {status!r} is not one of {', '.join(STATUSES)}"]
    if status == "decided" and not DATE.fullmatch(fm.get("decided", "")):
        return [f"{page}: decided decision has no decided date"]
    return []


def check_concept(page: str, fm: dict[str, str], groups: list[str]) -> list[str]:
    standing = fm.get("standing")
    if standing is None:
        return [f"{page}: concept with no standing"]
    if standing not in STANDINGS:
        return [f"{page}: standing {standing!r} is not one of {', '.join(STANDINGS)}"]
    trials = groups.count("trials")
    if standing != "claimed" and trials == 0:
        return [f"{page}: standing {standing} rests on no trial; documentation alone cannot move a standing"]
    if standing == "supported" and trials < 3:
        return [f"{page}: standing supported rests on {trials} trial(s); three are needed"]
    return []


def check_index(files: dict[str, str], pages: list[str], meta: dict[str, dict[str, str]]) -> list[str]:
    if INDEX not in files:
        return [f"{INDEX}: missing, so no page can be listed"]
    lines: dict[str, str] = {}
    for line in prose(files[INDEX]).splitlines():
        match = INDEX_LINE.match(line)
        path = local(match.group(1)) if match else None
        if match and path:
            lines[resolve(INDEX, path)] = match.group(2).lstrip(" :").strip()

    faults = []
    for page in pages:
        if page == INDEX:
            continue
        if page not in lines:
            faults.append(f"{page}: not listed in {INDEX}")
            continue
        if not lines[page]:
            faults.append(f"{page}: listed in {INDEX} with no line on what it holds")
            continue
        fm = meta.get(page, {})
        field = {"decision": "status", "concept": "standing"}.get(fm.get("type", ""))
        word = fm.get(field) if field else None
        if word and not lines[page].startswith(f"**{word}**"):
            faults.append(f"{page}: its line in {INDEX} does not start with **{word}**, its {field}")
    return faults


def check_raw(files: dict[str, str]) -> list[str]:
    def records(group: str) -> list[str]:
        prefix = f"raw/{group}/"
        return sorted({f[len(prefix):].split("/")[0] for f in files if f.startswith(prefix) and "/" in f[len(prefix):]})

    faults = []
    for slug in records("trials"):
        if f"raw/trials/{slug}/method.md" not in files:
            faults.append(f"raw/trials/{slug}: trial has no method.md, so it cannot be repeated")
    for slug in records("articles"):
        source = f"raw/articles/{slug}/source.md"
        if source not in files:
            faults.append(f"raw/articles/{slug}: capture has no source.md")
            continue
        fm = front_matter(files[source]) or {}
        faults += [f"{source}: source.md has no {key}" for key in ("url", "retrieved") if not fm.get(key)]
    return faults


def collect(repo: Path) -> dict[str, str]:
    """Every file under the repository, with the text of markdown files and nothing for others."""
    files: dict[str, str] = {}
    for root, dirs, names in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in names:
            path = Path(root, name)
            text = path.read_text(encoding="utf-8") if name.endswith(".md") else ""
            files[path.relative_to(repo).as_posix()] = text
    return files


def main(argv: list[str]) -> int:
    if len(argv) > 2 or (len(argv) == 2 and argv[1].startswith("-")):
        print("usage: wiki_lint.py [<repo>]", file=sys.stderr)
        return 2
    repo = Path(argv[1]) if len(argv) == 2 else Path(__file__).resolve().parent.parent
    if not (repo / "wiki").is_dir():
        print(f"no wiki/ in {repo}", file=sys.stderr)
        return 2
    faults = lint(collect(repo))
    for fault in faults:
        print(fault)
    return 1 if faults else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
