# Investigation: Freckle Face

## Summary

| Field | Value |
|---|---|
| **Family Name** | Freckle Face |
| **Designer** | Brian J. Bonislawsky / Astigmatic (AOETI) |
| **License** | OFL |
| **Date Added** | 2012-11-26 |
| **Repository URL** | https://github.com/librefonts/freckleface |
| **Commit** | `158b54fbb54daa103228a08cb0ea7d03c832461b` |
| **Config** | none (VFB-only sources) |
| **Status** | missing_config |
| **Confidence** | HIGH |

## METADATA.pb (current)

The current METADATA.pb has a source block added by commit `9a14639f3` (2026-02-25):

```
source {
  repository_url: "https://github.com/librefonts/freckleface"
  commit: "158b54fbb54daa103228a08cb0ea7d03c832461b"
}
```

No `config_yaml` field is set, which is correct since no gftools-buildable sources exist.

## Upstream Repository Analysis

### Repository: librefonts/freckleface

- **URL**: https://github.com/librefonts/freckleface (verified accessible, HTTP 200)
- **Remote**: https://github.com/librefonts/freckleface
- **Branch**: master
- **Total commits**: 1
- **Repo status**: Clean, up-to-date with origin

The repository contains a single commit:

| Hash | Date | Author | Message |
|---|---|---|---|
| `158b54f` | 2014-10-17 | hash3g | update .travis.yml |

This is a typical **librefonts mirror** repository. The `librefonts` GitHub organization was created to host source files for Google Fonts families. The single commit was made by hash3g (hash.3g@gmail.com), who was involved in setting up the librefonts mirrors.

### Source Files

The repository contains **VFB** (FontLab Studio) source files and **TTX** decompositions:

**In `src/` directory:**
- `FreckleFace-Regular.vfb` — Original source with contour overlaps
- `FreckleFace-Regular-TTF.vfb` — TrueType outlines with hinting adjustments
- `FreckleFace-Regular-OTF.vfb` — Merged contours, optimized for OTF
- Multiple `.otf.*.ttx` files — TTX decomposition of the OTF
- `METADATA_comments.txt` — Build/subset commands from the original onboarding
- `VERSIONS.txt` — "FreckleFace-Regular.ttf: Version 1.000"

**In repo root:**
- Multiple `.ttf.*.ttx` files — TTX decomposition of the TTF
- `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `OFL.txt`, `METADATA.json`
- `.travis.yml` — CI config using fontbakery-build.py (legacy)

**No modern buildable sources** (no `.glyphs`, `.glyphx`, `.ufo`, `.designspace` files). The only native sources are VFB (proprietary FontLab format), which are not supported by gftools-builder/fontc.

### No Other Upstream Repositories

- No GitHub repository exists under `astigmatic/freckleface` (returns 404).
- GitHub search for "freckleface" or "freckle-face" returns only the librefonts mirror, unrelated projects, and a bower package.
- Brian J. Bonislawsky / Astigmatic does not appear to have published the source files elsewhere.

## google/fonts History

### TTF File History

The binary `FreckleFace-Regular.ttf` has been present since the initial google/fonts commit and has **never been modified**:

| Commit | Date | Author | Description |
|---|---|---|---|
| `90abd17` | 2015-03-07 | Dave Crossland | Initial commit (bulk import of all fonts) |
| `76adaf1` | 2021-11-01 | m4rc1e | deploy: reorganization (file deleted and re-added, same blob) |

**Blob hash**: `b5e4196fc3fb22d33f91890c87259a8430d3efca` (identical at initial commit and HEAD)
**File size**: 121,088 bytes
**MD5**: `44f3e4f48ac14af9f2c0736e7f72db1e`

### Font Binary Metadata

- **Version**: 1.000
- **Copyright**: Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI)
- **Designer URL**: http://www.astigmatic.com/

## Commit Hash Verification

Since the librefonts/freckleface repo has only a single commit (`158b54f`), this is trivially the correct commit to reference. The repo was created in 2014, after the font was added to Google Fonts in 2012, as a mirror to host the source files. The TTX decompositions in the repo correspond to the same Version 1.000 font.

## Config.yaml Assessment

**No override config.yaml can be created.** The upstream repo contains only VFB sources (FontLab Studio proprietary format), which are not compatible with gftools-builder or fontc. There are no `.glyphs`, `.ufo`, or `.designspace` files that could be used for building.

The TTX files are decompositions of the compiled binaries, not true editable sources suitable for font compilation pipelines.

## Conclusion

The source block in METADATA.pb is correct:
- **Repository URL**: `https://github.com/librefonts/freckleface` -- verified accessible
- **Commit**: `158b54fbb54daa103228a08cb0ea7d03c832461b` -- the only commit in the repo
- **Config**: None possible (VFB-only sources, not gftools-builder compatible)
- **Status**: `missing_config` -- sources exist but are in a legacy format (VFB) that cannot be used by modern build tools. No actionable path to create an override config.yaml.

This is a completed investigation. The font's source metadata is as complete as it can be given the available sources.
