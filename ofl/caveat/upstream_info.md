# Investigation Report: Caveat

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Caveat |
| **Designer** | Impallari Type |
| **License** | OFL |
| **Date Added** | 2015-09-23 |
| **Repository URL** | https://github.com/googlefonts/caveat |
| **Commit Hash** | `59745e818ef7973e11e70cb1358d0e902b56c5fc` |
| **Branch** | master |
| **Config YAML** | Override in google/fonts |
| **Status** | complete |

## How URL Was Found

The repository URL was established in the `upstream.yaml` file created during the v2.000 update (commit `a85fc09e4` in google/fonts, October 2020). The upstream.yaml contained:

```yaml
branch: master
files:
  OFL.txt: OFL.txt
  fonts/variable/Caveat[wght].ttf: Caveat[wght].ttf
  fonts/ttf/Caveat-Regular.ttf: static/Caveat-Regular.ttf
  fonts/ttf/Caveat-Bold.ttf: static/Caveat-Bold.ttf
repository_url: https://github.com/googlefonts/caveat
```

This was later merged into METADATA.pb as a source block by Simon Cozens (commit `66f91f10f`).

## How Commit Was Determined

The google/fonts v2.000 update commit (`a85fc09e4`) by Marc Foley explicitly states:

> "Caveat Version 2.000 taken from the upstream repo https://github.com/googlefonts/caveat at commit https://github.com/googlefonts/caveat/commit/59745e818ef7973e11e70cb1358d0e902b56c5fc."

This is the HEAD commit of the upstream repo (most recent), which matches. The commit hash was added to the METADATA.pb source block by our enrichment work (`9a14639f3`), but the reference in the onboarding PR confirms it is correct.

## Config YAML Status

**No config.yaml exists in the upstream repo at any commit.** The Caveat project uses a custom `sources/build.sh` script that invokes fontmake directly:

```bash
fontmake -m Caveat.designspace -i -o ttf --output-dir ../fonts/ttf/
fontmake -m Caveat.designspace -o variable --output-path ../fonts/variable/Caveat[wght].ttf
```

The build script also applies post-processing with gftools fix-dsig, ttfautohint, fix-vf-meta, MVAR removal, and hinting fixes. This is a pre-gftools-builder workflow.

The source files at the tracked commit include:
- `sources/Caveat.designspace`
- `sources/Caveat-Regular.ufo`
- `sources/Caveat-Bold.ufo`
- `sources/Caveat-Brush.glyphs` (for the separate Caveat Brush font)
- `sources/build.sh`

**No override config.yaml** exists in `google/fonts/ofl/caveat/`.

## Verification

- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/googlefonts/caveat/`
- **Commit exists**: Yes, `59745e8` is the HEAD commit ("Fix /Ldot /ldot /AE /OE and new build.sh")
- **Commit matches onboarding**: Confirmed via the v2.000 PR commit message
- **Font file history**: Updated from v1.500 to v2.000 via commit `a85fc09e4` (the last significant update to the font binary)
- **Source types**: designspace, ufo (gftools-buildable in principle, but uses custom build.sh)

## Confidence Level

**HIGH** - The commit hash is explicitly documented in the onboarding commit message. The repository URL is correct. The only gap is the missing config.yaml, which would need to be created as an override in google/fonts to enable gftools-builder compilation.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Caveat.designspace
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. **Should a config.yaml override be created?** The Caveat sources (designspace + UFO) are buildable by gftools-builder in principle, but the original build.sh includes significant post-processing. A config.yaml would need to replicate the build settings.
2. **Caveat Brush source**: The repo also contains `sources/Caveat-Brush.glyphs` which is the source for the separate Caveat Brush family. However, this source was noted as "not the latest" in the README (see Caveat Brush investigation report).
