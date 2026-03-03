# Investigation Report: Herr Von Muellerhoff

## Summary

Herr Von Muellerhoff is a handwriting/display font designed by Alejandro Paul of Sudtipos. It was added to Google Fonts in the initial commit (2015-03-07) and has never been updated. The upstream repository at `librefonts/herrvonmuellerhoff` contains a VFB file and an SFD (FontForge) file as sources. While an SFD file can technically be processed, gftools-builder does not support SFD as an input format, so no config.yaml can be created for automated building.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Herr Von Muellerhoff |
| Designer           | Alejandro Paul (Sudtipos) |
| Repository URL     | https://github.com/librefonts/herrvonmuellerhoff |
| Upstream Commit    | `f49091c92a6bd343b44b78c2ab2ef2531bc850c5` (only commit; 2014-10-17) |
| Config YAML        | None (SFD/VFB sources only, not gftools-builder compatible) |
| Source Files       | `src/HerrVonMuellerhoff-Regular-TTF.sfd`, `src/Herr Von Muellerhoff-Regular-OTF.vfb` |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### Upstream Repository

The upstream repository is https://github.com/librefonts/herrvonmuellerhoff, cached locally at `upstream_repos/fontc_crater_cache/librefonts/herrvonmuellerhoff/`. The repo has only one commit (`f49091c`, dated 2014-10-17), containing a Travis CI update and the initial file upload.

The repo is a `librefonts` archive-style repository containing:
- TTX table dumps of the TTF font (split per table)
- `src/HerrVonMuellerhoff-Regular-TTF.sfd` -- FontForge SFD source for TTF
- `src/Herr Von Muellerhoff-Regular-OTF.vfb` -- FontLab VFB source for OTF (note the space in filename)
- `src/HerrVonMuellerhoff-Regular.otf.*` -- TTX dumps of OTF tables
- `DESCRIPTION.en_us.html`
- `METADATA.json` -- legacy metadata
- No `.glyphs`, `.ufo`, or `.designspace` files
- No `config.yaml` or `config.yml`

### Onboarding History

The font binary was added to google/fonts in the initial commit `90abd17b4` (2015-03-07, author: Dave Crossland). The font file (`HerrVonMuellerhoff-Regular.ttf`, 46624 bytes) has never been modified since.

The METADATA.pb copyright states: "Copyright (c) 2004 Alejandro Paul (sudtipos@sudtipos.com), with Reserved Font Name \"Herr Von Mullerhoff\"" (note the misspelling "Mullerhoff" vs "Muellerhoff" in the reserved font name).

### Source Block Status

The current HEAD of google/fonts has no source block in METADATA.pb for this family. A source block was added in commit `9a14639f3` (2026-02-25, "Add source blocks to 602 more METADATA.pb files") on a branch, pointing to `librefonts/herrvonmuellerhoff` at commit `f49091c92a6bd343b44b78c2ab2ef2531bc850c5`.

### Source File Analysis

The repo contains two types of source files:
1. **SFD (FontForge)**: `src/HerrVonMuellerhoff-Regular-TTF.sfd` -- FontForge Spline Font Database format. While FontForge can compile fonts from SFD, gftools-builder and fontmake do not support SFD as an input format.
2. **VFB (FontLab)**: `src/Herr Von Muellerhoff-Regular-OTF.vfb` -- FontLab proprietary binary format. Cannot be processed by gftools-builder.

Neither format is compatible with the gftools-builder toolchain (which requires .glyphs, .ufo, or .designspace). A config.yaml cannot be created for this family.

### Original Design Source

The font was designed by Alejandro Paul of Sudtipos. The copyright dates to 2004, making this a relatively old design. The `VERSIONS.txt` in the repo notes "Version 1.000".

## Conclusion

**Status: no_config_possible**

The upstream repository `librefonts/herrvonmuellerhoff` is a valid archive containing SFD and VFB source files, but neither format is compatible with gftools-builder. No config.yaml can be created for automated building. The source block should reference this repo at commit `f49091c` with no `config_yaml` field. The font has never been updated since the initial google/fonts commit.
