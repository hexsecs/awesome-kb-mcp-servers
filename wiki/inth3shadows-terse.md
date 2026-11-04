---
uid: 01a1a884-bbd4-79fd-847f-770a3f2f8fc4
title: "inth3shadows/terse"
summary: "Transparent proxy that sits in front of any other MCP server and shrinks its tool output before it reaches the model. Lossless by default — a denser…"
type: entity
category: "Aggregators"
url: "https://github.com/inth3shadows/terse"
status: unknown
created: 2026-11-04
updated: 2026-11-04
depth: stub
source_list: awesome-mcp-servers
source_commit: 29f2d490cc02468e7c9d87b0cf68d40d3041e7ef
list_summary: "Transparent proxy that sits in front of any other MCP server and shrinks its tool output before it reaches the model. Lossless by default — a denser encoding of the same bytes, with a round-trip gate asserting an exact inverse, so nothing is dropped or summarised. Repeated calls to the same tool emit a delta against the prior result instead of the whole payload. Per-tool opt-in, no decode step, no model in the loop. `uv tool install terse-mcp` then `terse proxy -- <server>`"
categories: ["Aggregators"]
list_occurrences: [{"title": "inth3shadows/terse", "category": "Aggregators", "description": "Transparent proxy that sits in front of any other MCP server and shrinks its tool output before it reaches the model. Lossless by default — a denser encoding of the same bytes, with a round-trip gate asserting an exact inverse, so nothing is dropped or summarised. Repeated calls to the same tool emit a delta against the prior result instead of the whole payload. Per-tool opt-in, no decode step, no model in the loop. `uv tool install terse-mcp` then `terse proxy -- <server>`"}]
sources:
  - url: "https://github.com/punkpeye/awesome-mcp-servers/blob/29f2d490cc02468e7c9d87b0cf68d40d3041e7ef/README.md"
    retrieved: 2026-11-04
---

Transparent proxy that sits in front of any other MCP server and shrinks its tool output before it reaches the model. Lossless by default — a denser encoding of the same bytes, with a round-trip gate asserting an exact inverse, so nothing is dropped or summarised. Repeated calls to the same tool emit a delta against the prior result instead of the whole payload. Per-tool opt-in, no decode step, no model in the loop. `uv tool install terse-mcp` then `terse proxy -- <server>`

- **Resource:** https://github.com/inth3shadows/terse
- **List section:** Aggregators
- **Source:** [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — the list is canon; this page is a generated stub (`depth: stub`). Depth is added by PR (see AGENTS.md).
