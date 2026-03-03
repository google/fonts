# Meera Inimai — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in the METADATA.pb file.

## Repository Analysis

The upstream repository is `https://github.com/santhoshtr/meera-tamil`, maintained by Santhosh Thottingal (one of the copyright holders listed in the font). The repository contains:

- `MeeraTamil-Regular.sfd` — FontForge SFD source (the only editable source)
- `features/` — OpenType feature files
- `Makefile` — Custom build using FontForge scripting
- `ttf/` — Pre-compiled TTF binaries
- `tools/` — Build helper scripts

The repo was renamed from "MeeraTamil" to "meera-tamil" at some point. It has 23 commits, with the latest being `75261af` (2016-03-26, "Rename MeeraTamil.sfd -> MeeraTamil-Regular.sfd").

Note: The font name in Google Fonts is "Meera Inimai" but the upstream project is called "Meera Tamil". These appear to be the same font — the copyright strings match.

## Onboarding History

The font was added to google/fonts via PR #1000 ("hotfix-meerainimai: v2.001 added"), merged as commit `30dc4b94a`. It was later restructured in the deploy commit `76adaf1d2`. The font has never been updated since.

## Build Configuration

The upstream repo uses a custom `Makefile` with FontForge scripting (`tools/generate.py`) to build the font. The sources are exclusively in SFD format, which is not compatible with gftools-builder. No `config.yaml` exists and none can be created without first converting the SFD to a modern format (.ufo, .glyphs, or .designspace).

## Findings

1. The font has no source block in METADATA.pb
2. The upstream repository (`santhoshtr/meera-tamil`) was identified by searching GitHub for the font name and matching copyright holders
3. Sources are SFD-only — no gftools-builder compatible formats exist
4. No override `config.yaml` can be created
5. The font name differs between Google Fonts ("Meera Inimai") and the upstream repo ("Meera Tamil")

## Recommended Source Block

```
source {
  repository_url: "https://github.com/santhoshtr/meera-tamil"
  commit: "75261af9389afed926f31e44043864ae50fd76f4"
  branch: "master"
}
```

No `config_yaml` field is possible due to SFD-only sources.

**Confidence**: MEDIUM — the copyright strings match but the font names differ slightly between Google Fonts and the upstream repo.
