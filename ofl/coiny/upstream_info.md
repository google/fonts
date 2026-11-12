# Coiny - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Coiny |
| Designer | Marcelo Magalhaes |
| Repository URL | https://github.com/marcelommp/Coiny |
| Commit Hash | 0341b95f0c79f0e0b33ab7b5404cf9265be88516 |
| Branch | gh-pages |
| Config YAML | N/A (override config.yaml in google/fonts) |
| Override Config | Yes |
| Status | complete |

## How URL Was Found

The repository URL `https://github.com/marcelommp/Coiny` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") on January 14, 2024. The repository is owned by Marcelo Magalhaes (marcelommp), who is credited as the designer in the METADATA.pb.

## How Commit Was Determined

The commit `0341b95f0c79f0e0b33ab7b5404cf9265be88516` (dated October 3, 2016) was the HEAD of the `gh-pages` branch, the repository's default (and only) branch, until July 2026. The commit message is "Adjustments in Horn and others accents plus Tamil".

The font was last updated in google/fonts via PR #1091 ("coiny: v1.001 added") by Marc Foley on August 7, 2017, which fixed issue #334. The PR only updated the TTF binary. Since `0341b95f` was the latest commit before the PR merge (and stayed the latest until July 2026), this was the state of the repo at the time of onboarding.

The source block was added in commit `2cca1f64a` ("sources info for Coiny: v1.001 (PR #1091)") which is on main.

## Config YAML Status

**Override config.yaml exists** in google/fonts at `ofl/coiny/config.yaml`:

```yaml
buildVariable: false
sources:
  - UFO/Coiny-Regular.ufo
```

The upstream repository contains:
- `UFO/Coiny-Regular.ufo` - the primary source file
- Various other files (FontForge files, concept sketches, specimens)
- No config.yaml in the upstream repo

The override config.yaml correctly references the UFO source at the path where it exists in the upstream repository.

## Verification

- **Repository accessible**: Yes, https://github.com/marcelommp/Coiny is accessible
- **Commit exists**: Yes, `0341b95f` is on gh-pages (its HEAD until July 2026)
- **Branch correct**: Yes, gh-pages is the only branch
- **Source block on main**: Yes, the full source block (repository_url + commit + branch) is on main
- **Override config exists**: Yes, at `ofl/coiny/config.yaml`
- **Config references correct files**: Yes, `UFO/Coiny-Regular.ufo` exists at the recorded commit

## Confidence Level

**High**. The repository URL, commit hash, and branch are all correct and verified. The designer's repository contains the expected UFO source file, and an override config.yaml is already in place referencing it correctly.

## Open Questions

None. This family is complete.

## The 2026 Glyphs source (checked 2026-10-15)

**Model**: Claude Opus 5.5

In July 2026 the designer added a Glyphs source, `GLYPHS_FILES/Coiny-Regular.glyphs` (9aa16ce), and a TTF and OTF built from it (7a15915, 076b7d9). fontc_crater triage suggested it as the source to record. Its TTF was compared with the shipped `Coiny-Regular.ttf`:

- version 1.000 (shipped: 1.001); 727 glyphs (shipped: 805);
- of the 668 codepoints both map, 80 have a different advance width and 159 a bounding box more than 2 units away;
- 16 codepoints of the shipped font are missing (U+0082-U+0085, U+0087, U+0089-U+008B, U+00AD, U+0310, U+0324, U+0325, U+032E, U+0331, U+035F, U+0FD5) and 3 are new (U+011D, U+030C, U+0326);
- GPOS has 26 lookups (shipped: 8).

It is a revised design, not the source of the shipped font, so the source block was left at `0341b95f`. Recording the Glyphs source belongs with an update of the family to the new design, with new binaries. The shipped binary itself is in the repository at no commit: it carries FontForge's `FFTM` table, generated for the 2017 update (PR #1091).

fontc_crater fails to build the recorded UFO in both compilers: its `features.fea` has `pos \L <0 0 -20 0> \?  <0 0 -20 0>;` (line 495), and `\?` is not a valid glyph name.
