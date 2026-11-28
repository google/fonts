# Federant - Investigation Report

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Federant |
| **Designer** | Cyreal (Olexa M. Volochay, Alexei Vanyashin) |
| **License** | OFL |
| **Date Added** | 2011-10-05 |
| **Repository URL** | https://github.com/cyrealtype/Federant |
| **Commit** | `c5c5f602213ac00b181d95e2078fff665dd31809` |
| **Config** | Override config.yaml in google/fonts |
| **Status** | complete |
| **Confidence** | HIGH |

## Repository Verification

- **URL**: https://github.com/cyrealtype/Federant -- accessible (HTTP 200)
- **Remote matches cache**: Yes (`origin` points to `https://github.com/cyrealtype/Federant`)
- **Cache location**: `upstream_repos/fontc_crater_cache/cyrealtype/Federant/`
- **Repo clean**: Yes (no local modifications)

## Commit Identification

### Google Fonts History

The Federant TTF in google/fonts was last modified in commit `585b8438bebd24e70c63b9c542844c3aaecadefa` (2016-01-21, Dave Crossland, "ofl/federant Update to v1.011 -- fix GPOS, improve hinting"). Before that, the only other TTF change was the initial commit `90abd17b` (2015-03-07).

### Upstream Commit History

| Hash | Date | Author | Message |
|------|------|--------|---------|
| `4003700` | 2016-01-10 | Alexei Vanyashin | initial commit |
| `ebb4a18` | 2016-01-12 | Alexei Vanyashin | adding ttx |
| `c5c5f60` | 2016-01-21 | Dave Crossland | Update to v1.011 |
| `51561a5` | 2016-01-22 | Alexei Vanyashin | Merge pull request #3 from davelab6/master |
| `c77c8f8` | 2016-01-22 | Alexei Vanyashin | updated kerning |
| `a845f02` | 2016-01-22 | Alexei Vanyashin | version update |
| `8a13ba9` | 2016-04-06 | alexeiva | adding img |

### Binary Verification

The TTF at upstream commit `c5c5f60` matches the google/fonts binary exactly:
- **MD5**: `d8843c8a318a674b8a3f19979610ff0b` (both files)
- **Size**: 45,588 bytes (both files)

This is the "Update to v1.011" commit by Dave Crossland, which matches the google/fonts commit message ("ofl/federant Update to v1.011"). The google/fonts commit was made on 2016-01-21 18:20:06 -0500, and the upstream commit was made on 2016-01-21 18:24:05 -0500 -- just 4 minutes later, consistent with the same person (Dave Crossland) committing to both repos in the same session.

### Post-Onboarding Changes

After `c5c5f60`, Alexei Vanyashin made further changes:
- `c77c8f8` (2016-01-22): "updated kerning" -- TTF changed from 45,588 to 34,316 bytes (regenerated with updated kerning in Glyphs sources)
- `a845f02` (2016-01-22): "version update" -- TTF stayed at 34,316 bytes

These post-onboarding changes have NOT been incorporated into google/fonts.

## Source Files

At the onboarding commit `c5c5f60`, the `src/` directory contains:

- `src/Federant-Regular.glyphs` (Glyphs source -- valid gftools-builder input)
- `src/Federant-Regular-OTF.vfb` (FontLab VFB)
- `src/Federant-Regular-TTF.vfb` (FontLab VFB)
- `src/Federant-Regular.vfb` (FontLab VFB, original with overlaps)
- `src/Federant-Regular.otf` (OTF binary)

The `.glyphs` file is the relevant source for gftools-builder.

## Config.yaml

The upstream repository has no `config.yaml` at any commit. An override config.yaml exists in google/fonts at `ofl/federant/config.yaml`:

```yaml
sources:
  - src/Federant-Regular.glyphs
```

This was added in commit `5ddf312e6` (2026-02-20, "Add config_yaml enrichment for 82 font families"). The path correctly references the `.glyphs` file present at the onboarding commit.

Since an override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from METADATA.pb (google-fonts-sources auto-detects local overrides).

## METADATA.pb Source Block

Current state on the working branch (`sources_per_family_2026-02-27`):

```
source {
  repository_url: "https://github.com/cyrealtype/Federant"
}
```

The commit hash `c5c5f602213ac00b181d95e2078fff665dd31809` was added on a separate branch (`sources_info_2026-02-25`) in commit `4fd9e2392` but is not yet on the current working branch. This needs to be added.

## METADATA.pb Change History

1. `c8a4f8556` (2024-01-14, Simon Cozens): Added source block with `repository_url`
2. `5ddf312e6` (2026-02-20, Felipe Sanches): Added override config.yaml
3. `4fd9e2392` (2026-02-25, Felipe Sanches): Added commit hash (on branch `sources_info_2026-02-25`)

## Action Required

- Add `commit: "c5c5f602213ac00b181d95e2078fff665dd31809"` to the METADATA.pb source block (currently missing on the working branch)
- Override config.yaml is already in place and correct

## Additional Notes

- The FONTLOG in the upstream repo documents that v1.011 was "Regenerated TTF through Glyphs to fix GPOS issue, reduce filesize, autohint"
- The font was originally designed by Olexa M. Volochay and Alexei Vanyashin for Cyreal, reviving the Feder Antiqua by Otto Ludwig Nagele (1911)
