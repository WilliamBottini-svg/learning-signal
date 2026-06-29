# Gateway smoke — gemini-2.0-flash-lite-001 unavailable

**Date:** 2026-06-25  
**Harness:** Stanford AI Gateway Mode 1  
**Planned model:** `gemini-2.0-flash-lite-001`  
**Result:** All 6 bundles failed with HTTP 404 (Vertex publisher model not found).

The key allow-list includes `gemini-2.0-flash-lite-001`, but the gateway returns 404 from Vertex AI in multiple regions. This is an infrastructure/key-scope issue, not a skill failure.

**Fallback used:** `gemini-2.5-flash-lite` — see [`gateway-smoke-2026-06-25-gemini-25-flash-lite.md`](gateway-smoke-2026-06-25-gemini-25-flash-lite.md).

Raw error log: `tests/results/runs/2026-06-25-gemini-flash-smoke.jsonl` (gitignored; all rows have `error` set).
