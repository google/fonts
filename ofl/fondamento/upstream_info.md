# Investigation: Fondamento

## Summary

| Field              | Value                                                    |
|--------------------|----------------------------------------------------------|
| Family Name        | Fondamento                                               |
| Designer           | Astigmatic (Brian J. Bonislawsky)                        |
| License            | OFL                                                      |
| Date Added         | 2011-11-16                                               |
| Category           | HANDWRITING, DISPLAY                                     |
| Repository URL     | https://github.com/librefonts/fondamento                 |
| Commit             | 92205310620ae12fc72d8dde6033cdc46ca07101                  |
| Branch             | master                                                   |
| Config YAML        | N/A (no gftools-buildable sources)                       |
| Status             | **missing_config**                                       |
| Confidence         | **HIGH**                                                 |

## Font Files in google/fonts

- `ofl/fondamento/Fondamento-Regular.ttf` (87,160 bytes)
- `ofl/fondamento/Fondamento-Italic.ttf`

Both files were added in the initial commit `90abd17b4` (2015-03-07, "Initial commit" by Dave Crossland). The TTF blob hash (`d0489b293`) has remained unchanged since then -- the binaries have never been updated.

## METADATA.pb Analysis

The METADATA.pb on the `main` branch has no `source { }` block. A pending source block addition exists on branch `sources_info_2026-02-25` (commit `9a14639f3`), which adds:
```
source {
  repository_url: "https://github.com/librefonts/fondamento"
  commit: "92205310620ae12fc72d8dde6033cdc46ca07101"
}
```

## Upstream Repository Analysis

**Repository**: https://github.com/librefonts/fondamento (accessible, HTTP 200)

The repository has exactly **one commit**:
- `9220531` (2014-10-17) by `hash3g` -- "update .travis.yml"

This is a typical "librefonts" repository created as part of the Google Fonts Font Bakery automation project circa 2014. The `hash3g` author was involved in this bulk repository creation effort.

### Source Files Found

The repository contains only legacy source formats:

**In `src/` directory:**
- `Fondamento-Regular-OTF.vfb` -- FontLab Studio binary (OTF outlines)
- `Fondamento-Regular-TTF.vfb` -- FontLab Studio binary (TTF outlines)
- `Fondamento-Italic-OTF.vfb` -- FontLab Studio binary (OTF outlines)
- `Fondamento-Italic-TTF.vfb` -- FontLab Studio binary (TTF outlines)
- `Fondamento-Regular.ai` -- Adobe Illustrator file
- `Fondamento-Italic.ai` -- Adobe Illustrator file
- Various `.otf.*.ttx` files (decompiled OTF table dumps)
- `METADATA_comments.txt` -- subsetting/build comments
- `VERSIONS.txt` -- lists "Version 1.000" for both fonts

**In root directory:**
- Various `.ttf.*.ttx` files (decompiled TTF table dumps)
- `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`
- `.travis.yml` -- Font Bakery CI configuration

### Build Configuration

No `config.yaml` exists. The `.travis.yml` uses the old `fontbakery-build.py` build system (pre-gftools era). The source files are VFB (FontLab Studio binary format), which are **not compatible with gftools-builder**. There are no `.glyphs`, `.ufo`, or `.designspace` files.

## Commit Verification

Since the upstream repo has only a single commit (`9220531`), and the font was added to google/fonts in the initial commit (2015-03-07), this is straightforward. The upstream repo was created in October 2014, predating the google/fonts initial commit. The commit hash `92205310620ae12fc72d8dde6033cdc46ca07101` is the only commit in the repo and correctly represents the state of sources used for the fonts in Google Fonts.

## Git History in google/fonts

| Commit      | Date       | Author   | Description                                             |
|-------------|------------|----------|---------------------------------------------------------|
| `90abd17b4` | 2015-03-07 | Dave Crossland | Initial commit (font files added)                |
| `480630de3` | --         | --       | Tentative update to METADATA.pb textprotos               |
| `27f377ab0` | --         | --       | Update copyright field in METADATA.pb                    |
| `883939708` | --         | --       | Remove METADATA.json files                               |
| `76adaf1d2` | 2021-11-01 | m4rc1e   | deploy: c7e2740... (big migration, TTF blob unchanged)  |

## Conclusion

Fondamento is a calligraphic handwriting font designed by Brian J. Bonislawsky (Astigmatic) in 2011. The upstream repository at `librefonts/fondamento` is a single-commit Font Bakery repo containing only legacy VFB sources and TTX dumps. There are no gftools-builder compatible sources (.glyphs, .ufo, .designspace), so no config.yaml can be created.

The repository URL and commit hash are verified with high confidence. The status is `missing_config` because there are no buildable source files that gftools-builder could use -- only VFB files that require FontLab Studio (proprietary software) to open.

An override config.yaml is **not feasible** for this family because the upstream sources are VFB files, not a format supported by gftools-builder.
