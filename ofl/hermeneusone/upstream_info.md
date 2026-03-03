# Investigation Report: Hermeneus One

## Summary

Hermeneus One is a Grecian-style serif display font designed by Pablo Impallari and Rodrigo Fuenzalida. It was added to Google Fonts in the initial commit (2015-03-07) and has never been updated since. The upstream repository at `librefonts/hermeneusone` contains only VFB (FontLab binary) source files and TTX dumps -- no gftools-builder compatible sources (.glyphs, .ufo, .designspace). A config.yaml cannot be created because there are no buildable sources.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Hermeneus One |
| Designer           | Pablo Impallari, Rodrigo Fuenzalida |
| Repository URL     | https://github.com/librefonts/hermeneusone |
| Upstream Commit    | `20a3262831635f7f246ec54caf68abd760f2f582` (only commit; 2014-10-17) |
| Config YAML        | None (no gftools-builder compatible sources) |
| Source Files       | `src/HermeneusOne-Regular.vfb`, `src/HermeneusOne-Regular-OTF.vfb`, `src/HermeneusOne-Regular-TTF.vfb` (VFB only) |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### Upstream Repository

The upstream repository is https://github.com/librefonts/hermeneusone, cached locally at `upstream_repos/fontc_crater_cache/librefonts/hermeneusone/`. The repo has only one commit (`20a3262`, dated 2014-10-17), which is a Travis CI configuration update that also constitutes the initial upload of all files.

The repo is a `librefonts` archive-style repository containing:
- TTX table dumps of the TTF font (split per table)
- `src/HermeneusOne-Regular.vfb` -- FontLab VFB source
- `src/HermeneusOne-Regular-OTF.vfb` -- OTF variant VFB source
- `src/HermeneusOne-Regular-TTF.vfb` -- TTF variant VFB source
- `src/HermeneusOne-Regular.otf.*` -- TTX dumps of OTF tables
- `FONTLOG.txt` -- references http://www.impallari.com/projects/overview/hermeneus
- `METADATA.json` -- legacy metadata
- No `.glyphs`, `.ufo`, or `.designspace` files
- No `config.yaml` or `config.yml`

### Onboarding History

The font binary was added to google/fonts in the initial commit `90abd17b4` (2015-03-07, author: Dave Crossland). The font file (`HermeneusOne-Regular.ttf`, 132940 bytes) has never been modified since.

The METADATA.pb copyright states: "Copyright (c) 2012, Pablo Impallari (www.impallari.com|impallari@gmail.com) and Rodrigo Fuenzalida (www.rfuenzalida.com), with Reserved Font Name Hermeneus."

### Source Block Status

The current HEAD of google/fonts has no source block in METADATA.pb for this family. A source block was added in commit `9a14639f3` (2026-02-25, "Add source blocks to 602 more METADATA.pb files") on a branch, pointing to `librefonts/hermeneusone` at commit `20a3262831635f7f246ec54caf68abd760f2f582`.

### Source File Analysis

All source files are in VFB format (FontLab proprietary binary). VFB files cannot be processed by gftools-builder, fontmake, or fontc. To build fonts from these sources, one would need to:
1. Convert VFB to UFO or .glyphs format using FontLab or vfb2ufo
2. Create a config.yaml referencing the converted sources

Since the upstream repo has no buildable sources, no config.yaml can be created.

### Original Design Source

The FONTLOG.txt references the project page at `http://www.impallari.com/projects/overview/hermeneus`. The original design was by Pablo Impallari and Rodrigo Fuenzalida, with hinting by Igino Marini (v1.2, November 2011).

## Conclusion

**Status: no_config_possible**

The upstream repository `librefonts/hermeneusone` is a valid archive of the font sources, but it contains only VFB (FontLab binary) files. No gftools-builder compatible sources exist, making it impossible to create a config.yaml for automated building. The source block should reference this repo at commit `20a3262` with no `config_yaml` field. The font has never been updated since the initial google/fonts commit.
