# Maintainer schema — MCP Servers (Awesome KB)

OpenShelf 1.7, profile awesome. Read kb.yaml. Format authority is
OpenNorms/openshelf; maintenance method is hexsecs/awesome-kb-skill.

## Canon and scope

punkpeye/awesome-mcp-servers is canon, designated by the owner 2026-11-04.
Ingest Tutorials, Community, Server Implementations and Frameworks bullet entries; ignore navigation, badges, ads and gallery duplicates.
Do not recursively ingest linked resources. Repeated URLs share one entity,
with all source title/category/description occurrences in list_occurrences.
Entity category is its first source category; categories holds every category.

## Maintenance

wiki/<slug>.md holds entities; wiki/index-<category>.md and index.md are
generated. raw/<capture-date>/ holds immutable upstream snapshots and license
texts. tools/ingest.py parses the list; log.md is append-only.

New stubs receive tooling-minted UUIDv7 identity, ingestion created/updated
dates, status unknown, depth stub, and pinned source citation. last_checked
must stay absent until the resource's URL and maintenance state are verified.
uid and created never change. Preserve authored brief/full/deep body, depth,
status, verification stamps and additional sources through re-ingestion.
Summary is capped at 160 chars; list_summary preserves upstream description.

Run python3 tools/check.py, a repeat ingest, and openshelf lint . before landing.
Do not change the source capture; add a new dated capture for a newer source.
Observe LICENSE and THIRD_PARTY_NOTICES.md when redistributing or transforming.

## Generated README list

The README contains a marked generated list, maintained by tools/render_readme.py
from the same index graph. Ingest updates both views; do not edit between the
generated markers. Introduction and license sections outside the markers stay
manual. Entry names link to KB pages and upstream links open original resources.
Large catalogs continue under lists/ at category boundaries to keep README and
continuation pages below GitHub's 500 KiB display limit. These files are generated,
not additional OpenShelf entities. Run python3 tools/render_readme.py --check to
verify completeness, links, display size and synchronization.
