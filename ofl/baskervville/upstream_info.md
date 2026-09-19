# Baskervville

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: ANRT
**METADATA.pb path**: `ofl/baskervville/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/anrt-type/ANRT-Baskervville |
| Commit | `0629447774568fd957d98736487afb000be38b55` |
| Config YAML | `sources/config.yaml` |
| Branch | master |

## How the Repository URL Was Found
The repository URL `https://github.com/anrt-type/ANRT-Baskervville` is documented in the METADATA.pb `source { }` block. It is also confirmed by the copyright string in the font files: "Copyright 2018 The Baskervville Project Authors (https://github.com/anrt-type/ANRT-Baskervville)". The google/fonts commit message for the Version 1.100 update (d575059e9, 2025-04-23) explicitly states: "Taken from the upstream repo https://github.com/anrt-type/ANRT-Baskervville".

## How the Commit Hash Was Identified
The commit hash `0629447774568fd957d98736487afb000be38b55` is recorded in METADATA.pb and confirmed by the google/fonts commit message for d575059e9: "at commit https://github.com/anrt-type/ANRT-Baskervville/commit/0629447774568fd957d98736487afb000be38b55". The commit exists in the upstream repo and is titled "rebuilt fonts with SC" dated 2025-04-22.

## How Config YAML Was Resolved
The config file `sources/config.yaml` is present in the upstream repo at the referenced commit. Verified by listing the tree at commit 0629447:
- `sources/Baskervville-Italic.glyphs`
- `sources/Baskervville.glyphs`
- `sources/config.yaml`

The config.yaml contains:
```yaml
sources:
    - Baskervville.glyphs
    - Baskervville-Italic.glyphs
familyName: Baskervville
autohintOTF: false
buildSmallCap: true
```

No override config.yaml exists in the google/fonts family directory.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2025-04-22 11:33:01 +0200
- Commit message: "rebuilt fonts with SC"
- Source files at commit: `sources/Baskervville.glyphs`, `sources/Baskervville-Italic.glyphs`, `sources/config.yaml`
- Font files at commit: `fonts/variable/Baskervville[wght].ttf`, `fonts/variable/Baskervville-Italic[wght].ttf`, `fonts/variable/BaskervvilleSC[wght].ttf`

## Note on Upstream Changes
There are 2 commits in the upstream repo after the referenced commit:
1. `75cbd68` - "updated vendor ID"
2. `35a86a0` - "Fixed asymetric hyphen spacing"

These changes would need a separate review and QA process before being incorporated into Google Fonts.

## Confidence
**High**: The commit hash is explicitly confirmed by the google/fonts commit message, the upstream repo URL matches the copyright string, the commit exists and contains the expected source files and config.yaml.

## Open Questions
None
