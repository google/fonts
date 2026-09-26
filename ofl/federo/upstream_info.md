# Federo - Investigation Report

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Federo |
| **Designer** | Cyreal (Olexa Volochay) |
| **License** | OFL |
| **Date Added** | 2011-07-27 |
| **Repository URL** | https://github.com/cyrealtype/Federo |
| **Commit** | `79d2ed54e783fb0b116aabdb6c9b0318393cd3c8` |
| **Config** | Override config.yaml in google/fonts (VFB-only sources) |
| **Status** | complete |
| **Confidence** | HIGH |

## Repository Verification

- **URL**: https://github.com/cyrealtype/Federo -- accessible (HTTP 200)
- **Remote matches cache**: Yes (`origin` points to `https://github.com/cyrealtype/Federo`)
- **Cache location**: `upstream_repos/fontc_crater_cache/cyrealtype/Federo/`
- **Repo clean**: Yes (no local modifications)

## Commit Identification

### Google Fonts History

The Federo TTF has only been modified once in google/fonts -- in the initial commit `90abd17b4f97671435798b6147b698aa9087612f` (2015-03-07, Dave Crossland, "Initial commit"). The font has never been updated since.

### Upstream Commit History

| Hash | Date | Author | Message |
|------|------|--------|---------|
| `79d2ed5` | 2016-01-10 | Alexei Vanyashin | initial commit |
| `3c5ce38` | 2016-01-22 | Alexei Vanyashin | upd |
| `5f46d60` | 2016-04-06 | alexeiva | adding img |
| `aa1630e` | 2018-02-12 | alexeiva | repo reorganising. v2.120 update |
| `5ca1009` | 2018-02-12 | alexeiva | version 1.120 update |

### Binary Verification

The TTF at upstream commit `79d2ed5` (file named `Federo.ttf`) matches the google/fonts binary (`Federo-Regular.ttf`) exactly:
- **MD5**: `db41ac92ad9c81b988ef175a667cfe7c` (both files)
- **Size**: 145,056 bytes (both files)

Note: The upstream repo's initial commit (2016-01-10) postdates the google/fonts initial commit (2015-03-07). This means the font was in google/fonts before the upstream GitHub repo existed. The upstream repo was created retroactively to host the source files for the font that was already published.

### Post-Onboarding Changes

The upstream repo has subsequent commits with significant changes:
- `3c5ce38` (2016-01-22): Renamed files (Federo.ttf -> Federo-Regular.ttf, renamed VFB sources)
- `5f46d60` (2016-04-06): Added `.glyphs` source files and sample image
- `aa1630e` (2018-02-12): Major repo reorganization, v2.120 update, regenerated from Glyphs App, added glyphs (backslash, ellipsis). TTF moved to `fonts/ttf/`, sources moved to `sources/`
- `5ca1009` (2018-02-12): Version 1.120 update to the TTF

None of these later changes have been incorporated into google/fonts. The upstream HEAD TTF (`fonts/ttf/Federo-Regular.ttf`, 48,564 bytes) is substantially different from the google/fonts version (145,056 bytes).

## Source Files

At the referenced commit `79d2ed5`, the source files are:

- `src/Federo-TTF.vfb` (FontLab VFB -- used for TTF generation)
- `src/Federo-Regular_PS_Source.vfb` (FontLab VFB -- PostScript source)
- `src/Federo.otf` (OTF binary)

There are NO `.glyphs`, `.ufo`, or `.designspace` files at this commit. The `.glyphs` file (`sources/Federo.glyphs`) was only added in commit `aa1630e` (2018-02-12), well after the onboarding.

## Config.yaml

The upstream repository has no `config.yaml` at any commit. An override config.yaml exists in google/fonts at `ofl/federo/config.yaml`:

```yaml
buildVariable: false
sources:
  - src/Federo-TTF.vfb
  - src/Federo-Regular_PS_Source.vfb
```

This was added in commit `e010f0838` (2025-11-21, Felipe Sanches, "sources info for Federo"). The config references the VFB files from the original commit `79d2ed5`.

**Important note**: VFB files are FontLab format and are NOT natively supported by gftools-builder. This config.yaml documents the source files but cannot be used for automated rebuilding. To enable rebuilding, one would need to either:
1. Reference the `.glyphs` file from a later upstream commit (which would change the font)
2. Accept that this font can only be rebuilt from the VFB sources using FontLab

Since an override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from METADATA.pb.

## METADATA.pb Source Block

Current state:

```
source {
  repository_url: "https://github.com/cyrealtype/Federo"
  commit: "79d2ed54e783fb0b116aabdb6c9b0318393cd3c8"
}
```

This is complete -- both `repository_url` and `commit` are present and verified correct.

## METADATA.pb Change History

1. `c8a4f8556` (2024-01-14, Simon Cozens): Added source block with `repository_url`
2. `e010f0838` (2025-11-21, Felipe Sanches): Added commit hash and override config.yaml

## Action Required

None. The METADATA.pb source block is complete with verified repository URL and commit hash. The override config.yaml is in place.

## Additional Notes

- Federo is a display typeface referencing Jakob Erbar's Feder Grotesk (1909), designed by Olexa Volochay in 2011
- The same designer (Cyreal/Alexei Vanyashin) maintains both Federant and Federo repos, with similar history patterns
- The copyright lists "Olexa M. Volochay | Cyreal.org" as the author
- The upstream repo was reorganized significantly in 2018, with sources regenerated from Glyphs App and additional glyphs added, but these changes were never pushed to google/fonts
