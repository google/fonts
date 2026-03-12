**Model**: Claude Opus 4.6

# Yinmar — Upstream Source Investigation

## Summary

Repositories were found for Yinmar but they contained only VOLT/TTF sources, not UFO or Glyphs. No source block was added to `METADATA.pb`.

## Repositories Found (Non-UFO Sources)

- **URL**: https://github.com/khmertype/Yinmar
  - Contents: `Source/Limelight.vtd` (VOLT data), `Source/MyanmarYinmar_volt.ttf`, binary TTFs
- **URL**: https://github.com/khmertype/MyanmarYinmar
  - Contents: `Source/MyanmarYinmar_volt.ttf` only

## Investigation Notes

Yinmar is a Myanmar Unicode font designed by Danh Hong. Two repositories were found under the `khmertype` GitHub organization, both attributed to Danh Hong's Myanmar font work. However, both repositories contained only VOLT (.vtd) source data embedded in or alongside TTF binaries — not open UFO or Glyphs source files. VOLT (Visual OpenType Layout Tool) is a Microsoft tool that generates OpenType layout tables but is not an open source design format suitable for the google/fonts source block.

## Status

**Skipped** — sources are VOLT/TTF only; no UFO/Glyphs sources were found.
