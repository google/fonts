# Investigation Report: Baskervville SC

- **Family name**: Baskervville SC
- **Slug**: baskervvillesc
- **Model**: Claude Opus 4.6
- **Date**: 2026-03-03

## Summary

Baskervville SC is the Small Caps variant of the Baskervville family, both sharing the same upstream repository (anrt-type/ANRT-Baskervville). The source metadata in METADATA.pb was already complete and correct. The upstream config.yaml at `sources/config.yaml` includes `buildSmallCap: true`, which produces the SC variant. No override config.yaml was needed.

## METADATA.pb (Initial State)

The METADATA.pb at `ofl/baskervvillesc/METADATA.pb` already contained a complete source block:

```
source {
  repository_url: "https://github.com/anrt-type/ANRT-Baskervville"
  commit: "0629447774568fd957d98736487afb000be38b55"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BaskervvilleSC[wght].ttf"
    dest_file: "BaskervvilleSC[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Repository Verification

- **URL**: https://github.com/anrt-type/ANRT-Baskervville (verified accessible, HTTP 200)
- **Cached at**: upstream_repos/fontc_crater_cache/anrt-type/ANRT-Baskervville
- **Remote matches**: origin = https://github.com/anrt-type/ANRT-Baskervville
- **Repo clean**: Yes, working tree clean (detached at 0629447)

## Commit Verification

The referenced commit `0629447774568fd957d98736487afb000be38b55` was verified in the upstream repository:

- **Date**: 2025-04-22
- **Author**: Rosalie Wagner
- **Message**: "rebuilt fonts with SC"
- **Key change**: Set `buildSmallCap: true` in `sources/config.yaml` (was previously `false`), and generated the new `fonts/variable/BaskervvilleSC[wght].ttf`

The binary file `BaskervvilleSC[wght].ttf` at this upstream commit (SHA-256: `272b5aa6...`) matched the google/fonts binary at the "Version 1.100 added" commit (`fe282bb64`, 2025-04-23) exactly.

A subsequent google/fonts commit (`72f3e5c39`, 2025-05-01, "update fonts with the right OFL url") rebuilt the binary to embed a corrected OFL URL, changing the checksum to `cd2ac64e...`. This is a google/fonts-side rebuild; the source commit reference remains correct.

## Relationship with Regular Baskervville

Both families share the same upstream repository and the same commit hash (`0629447`):

- **Baskervville** (`ofl/baskervville/`): Updated to Version 1.100 on 2025-04-23 by Emma Marichal
- **Baskervville SC** (`ofl/baskervvillesc/`): Updated to Version 1.100 on 2025-04-23 by Emma Marichal

The single `sources/config.yaml` with `buildSmallCap: true` drives the generation of both the regular and SC variable fonts from the same `.glyphs` sources.

## Onboarding History

1. **Initial onboarding** (2024-05-27): Baskervville SC was first added by Simon Cozens as Version 1.003 from upstream commit `11a43fe` (a merge PR from 2023-06-30 adding ubreve, capital Eszett, etc.). This was a static font (`BaskervvilleSC-Regular.ttf`).

2. **Version 1.100 update** (2025-04-23): Emma Marichal updated to commit `0629447`, which converted Baskervville SC to a variable font (`BaskervvilleSC[wght].ttf`) with a weight axis (400-700). This was the commit that enabled `buildSmallCap: true` in the upstream config.

3. **OFL URL fix** (2025-05-01): Emma Marichal rebuilt fonts with corrected OFL URL, modifying the binary but not the source reference.

## Source Files at Referenced Commit

```
sources/Baskervville.glyphs        (56,086 lines)
sources/Baskervville-Italic.glyphs (44,260 lines)
sources/config.yaml
```

## config.yaml

The upstream `sources/config.yaml` at commit `0629447` contained:

```yaml
sources:
    - Baskervville.glyphs
    - Baskervville-Italic.glyphs
familyName: Baskervville
autohintOTF: false
buildSmallCap: true
```

This is a valid gftools-builder configuration. The `config_yaml: "sources/config.yaml"` field in METADATA.pb correctly points to this file. No override config.yaml was needed.

## Newer Upstream Commits

Three commits existed after `0629447` on origin/master (fetched 2026-03-03):

1. `75cbd68` - "updated vendor ID"
2. `35a86a0` - "Fixed asymetric hyphen spacing"
3. `99f1509` - "center quoteleft.sc in bold master"

These are post-onboarding changes that would need separate review before incorporation.

## Final State

| Field | Value |
|-------|-------|
| repository_url | https://github.com/anrt-type/ANRT-Baskervville |
| commit | 0629447774568fd957d98736487afb000be38b55 |
| config_yaml | sources/config.yaml |
| branch | master |
| Status | **complete** |
| Confidence | **HIGH** |

No changes to METADATA.pb were required. The source block was already fully populated with verified correct data.
