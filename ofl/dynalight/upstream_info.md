# Investigation Report: Dynalight

**Date investigated:** 2026-02-27
**Status:** `missing_config` (VFB-only sources, no gftools-builder config possible)
**Designer:** Brian J. Bonislawsky (Astigmatic)

## METADATA.pb Path

`ofl/dynalight/METADATA.pb`

## Source Data

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| repository_url   | `https://github.com/librefonts/dynalight`                |
| commit           | `af7642053cc1189c5c8a4b93d0b4c1b1c5edcb49`              |
| branch           | `master`                                                 |
| config_yaml      | N/A (VFB-only sources)                                   |

## How URL Was Found

The upstream repository URL `https://github.com/librefonts/dynalight` was already recorded in the tracking data (`data/gfonts_library_sources.json`). The `librefonts` GitHub organization hosts mirrors of Google Fonts source repositories, created by user hash3g. The repository is accessible (HTTP 200) and contains the font sources.

No original Astigmatic-owned repository was found. The librefonts mirror appears to be the only public source repository for this font.

## How Commit Hash Was Identified

The upstream repository contains exactly one commit:

```
af7642053cc1189c5c8a4b93d0b4c1b1c5edcb49 2014-10-17 "update .travis.yml"
```

This single commit, authored by hash3g on 2014-10-17, constitutes the entire repository content. It added all files including source VFBs, TTX decompositions, FONTLOG.txt, license, and a Travis CI configuration. Since there is only one commit, the hash identification is trivial.

The font was added to Google Fonts on 2011-12-19 (per METADATA.pb `date_added`), well before the librefonts mirror was created in 2014. The font binary was part of the google/fonts "Initial commit" on 2015-03-07, which was the bulk import of the entire existing catalog at the time.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and none can be created because the source files are exclusively in FontLab VFB format:

- `src/Dynalight-Regular.vfb` -- Original source with contour overlaps
- `src/Dynalight-Regular-OTF.vfb` -- Merged contours for OTF
- `src/Dynalight-Regular-TTF.vfb` -- TrueType outlines with hinting

VFB is a proprietary FontLab Studio binary format that is not supported by gftools-builder. The repository also contains TTX decompositions of both TrueType and OpenType builds, but these are not suitable as gftools-builder sources either.

No override `config.yaml` exists in the google/fonts family directory (`ofl/dynalight/`).

## Verification

- **Repository accessible:** Yes (HTTP 200 at `https://github.com/librefonts/dynalight`)
- **Repository clean:** Yes (no local modifications)
- **Branch:** `master` (single branch)
- **Commit exists:** Yes, `af76420` is the sole commit in the repository
- **Font binary in google/fonts:** `Dynalight-Regular.ttf` (53,148 bytes), present since the initial commit (2015-03-07)
- **Font version:** 1.000 (per `src/VERSIONS.txt`)
- **Source block in METADATA.pb (main):** Not yet present (source block exists on `sources_info_2026-02-25` branch from PR #10278)

## Confidence

**HIGH** -- The repository URL and commit hash are unambiguous. The librefonts mirror has a single commit containing all sources. The font has never been updated in google/fonts since the initial bulk import. The limitation is purely that VFB sources cannot be built with gftools-builder, so no config.yaml is applicable.

## Notes

- This is a librefonts mirror, not an original designer-owned repository. The original sources were created by Brian J. Bonislawsky of Astigmatic (AOETI).
- The font was added to Google Fonts in December 2011, predating the google/fonts GitHub repository.
- The copyright field contains a Reserved Font Name ("Dynalight").
- The font is classified as both DISPLAY and HANDWRITING.
- No PRs to google/fonts specifically reference Dynalight.
