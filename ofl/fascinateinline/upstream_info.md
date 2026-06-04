# Investigation Report: Fascinate Inline

## Family Details

- **Family name**: Fascinate Inline
- **Designer**: Brian J. Bonislawsky / Astigmatic (AOETI)
- **License**: OFL
- **Category**: Display
- **Date added to Google Fonts**: 2011-12-07
- **Font styles**: Regular (single weight)
- **Font version**: 1.000

## Upstream Repository

- **URL**: https://github.com/librefonts/fascinateinline
- **Commit**: `0319622bad0ad42aae026ce7b00cd2f8ef64e658` (only commit; "update .travis.yml", 2014-10-17)
- **Branch**: master
- **Repo created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Status**: Accessible, not archived

The librefonts organization (created 2013-10-20) hosts this repo. It contains a single commit by hash3g, which set up the repo with source files and a Travis CI configuration. This is not the original author's repository but rather a mirror/archive created by the librefonts project.

## Source Files

The repository contains only legacy source formats:

### VFB files (FontLab Studio proprietary, in `src/`):
- `FascinateInline-Regular-OTF.vfb` -- merged contours, OTF-optimized
- `FascinateInline-Regular-TTF.vfb` -- TrueType outlines with hinting

Note: Unlike the Fascinate repo, this one has only 2 VFB files (no "original source with contour overlaps" variant).

### TTX dumps (XML, in root and `src/`):
- Multiple per-table TTX files for both TTF and OTF versions

### No gftools-buildable sources:
- No `.glyphs`, `.glyphx`, `.ufo`, `.designspace`, or `.sfd` files
- No `config.yaml` or `sources.yaml`

## Binary File Analysis

The `FascinateInline-Regular.ttf` in google/fonts has been unchanged since the initial commit (`90abd17b4`, 2015-03-07, by Dave Crossland). The font was originally added to Google Fonts on 2011-12-07, predating the current google/fonts repository.

- **File size**: 59,604 bytes
- **MD5**: `df7133c9949bd53157082e1e77a6f735`
- **Font created date (head table)**: 2011-12-01 04:49:00
- **Font modified date (head table)**: 2011-11-30 22:08:40

## google/fonts Commit History (ofl/fascinateinline/)

1. `90abd17b4` (2015-03-07) -- Initial commit (Dave Crossland) -- added all files
2. `480630de3` -- Tentative update to METADATA.pb textprotos
3. `27f377ab0` -- Update copyright field in METADATA.pb
4. `883939708` -- Remove METADATA.json files
5. `633ebadbf` -- Add language support metadata (#4160)
6. `28b492c0f` / `c6307ba83` / `701bd391b` -- Language metadata rollback/redo (#4677, #4706)
7. `6bda16478` -- Format HTML with new html formatter

The TTF binary was never modified after the initial commit.

## METADATA.pb Status

The current METADATA.pb on main has no `source { }` block. A source block was prepared on branch `sources_info_2026-02-25` (commit `9a14639f3`) pointing to `librefonts/fascinateinline` at commit `0319622`, but it has not been merged.

## Config Assessment

**No config.yaml is possible.** The upstream repo only has VFB sources, which are FontLab Studio proprietary binary files. These cannot be processed by gftools-builder or fontc. There is no way to create a config.yaml for this family without first converting the sources to an open format (.glyphs, .ufo, or .designspace).

## Relationship to Fascinate

Fascinate and Fascinate Inline are companion typefaces designed together by Brian J. Bonislawsky. They share:
- The same copyright notice and OFL license (both names reserved together in the OFL.txt found in google/fonts)
- The same creation date (2011-12-01, within minutes of each other per head table timestamps)
- The same date added to Google Fonts (2011-12-07)
- The same Art Deco design language, with the Inline version featuring decorative inline strokes

Despite being companion faces, they are maintained in separate librefonts repositories (`librefonts/fascinate` and `librefonts/fascinateinline`).

## Designer Information

Brian J. Bonislawsky operates as Astigmatic (AOETI). Website: http://www.astigmatic.com/. Email: astigma@astigmatic.com. He is a prolific contributor to Google Fonts with many display typefaces.

## Conclusion

- **Repository URL**: https://github.com/librefonts/fascinateinline
- **Commit**: `0319622bad0ad42aae026ce7b00cd2f8ef64e658` (only commit in repo)
- **Config**: none (VFB-only sources, not buildable with gftools-builder)
- **Status**: complete (source block can be added, but no config.yaml is possible)
- **Confidence**: HIGH -- the librefonts repo is the only known upstream, and the commit is the only commit in the repo. The VFB sources match the font's original creation date (2011).

No further action is possible regarding config.yaml without source format conversion by the original designer.
