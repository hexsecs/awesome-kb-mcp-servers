#!/usr/bin/env python3
"""Offline integrity, completeness, identity, reachability and ingest checks."""
import hashlib
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import ingest

def digest(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file() and "__pycache__" not in str(p)}

def main():
    entries = ingest.parse_list(ROOT / "raw/2026-11-04/README.md")
    pages = {}
    ids = set()
    for p in (ROOT / "wiki").glob("*.md"):
        fields, body = ingest.split_page(p.read_text())
        if not fields:
            continue
        assert fields["type"] == "entity"
        assert fields["uid"] not in ids
        uuid.UUID(fields["uid"])
        ids.add(fields["uid"])
        assert 0 < len(fields["summary"]) <= 160
        assert fields["depth"] in {"stub", "brief", "full", "deep"}
        assert len(body) // 4 <= {"stub": 750, "brief": 750, "full": 2500, "deep": 6000}[fields["depth"]]
        pages[fields["url"]] = (p, fields)
    assert len(pages) == len(entries)
    for e in entries:
        p, f = pages[e["url"]]
        assert f["title"] == e["title"]
        assert f["category"] == e["section"]
        assert f["list_summary"] == e["summary"]
    # Traverse generated index links and check all local Markdown targets.
    visited, pending = set(), [ROOT / "index.md"]
    while pending:
        p = pending.pop().resolve()
        if p in visited:
            continue
        visited.add(p)
        for target in re.findall(r"\]\(([^)]+)\)", p.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            target = (p.parent / target.split("#")[0]).resolve()
            assert target.is_relative_to(ROOT.resolve()) and target.exists(), target
            if target.suffix == ".md":
                pending.append(target)
    assert all(p.resolve() in visited for p, _ in pages.values())
    for line in (ROOT / "raw/MANIFEST.sha256").read_text().splitlines():
        expected, name = line.split("  ", 1)
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected
    # Run mutating checks on a disposable copy only.
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp) / "kb"
        shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns("__pycache__", ".git"))
        command = [sys.executable, str(work / "tools/ingest.py"), "--date", "2026-11-04"]
        before = digest(work)
        subprocess.run(command, check=True)
        assert before == digest(work), "second ingest changed files"
        # Force a list-description rewrite at each authored depth.
        original_source = (work / "raw/2026-11-04/README.md").read_text()
        page = work / pages[entries[0]["url"]][0].relative_to(ROOT)
        original_page = page.read_text()
        identity, _ = ingest.split_page(original_page)
        for depth in ("brief", "full", "deep"):
            text = original_page.replace("depth: stub", "depth: " + depth)
            marker = "\nAuthored content must survive.\n"
            text = text[:text.index("\n---\n", 4)+5] + marker
            page.write_text(text)
            source = work / "raw/2026-11-04/README.md"
            source.write_text(original_source.replace(entries[0]["summary"], entries[0]["summary"] + " Updated.", 1))
            subprocess.run(command, check=True)
            fields, body = ingest.split_page(page.read_text())
            assert body == marker and fields["depth"] == depth
            assert fields["uid"] == identity["uid"] and fields["created"] == identity["created"]
    print(f"PASS: {len(entries)} entries; complete import, unique UUIDs, summaries, links, checksums, idempotency and authored-depth preservation")

if __name__ == "__main__":
    main()
