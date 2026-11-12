# Investigation Report: Fascinate

## Family Details

- **Family name**: Fascinate
- **Designer**: Brian J. Bonislawsky / Astigmatic (AOETI)
- **License**: OFL
- **Category**: Display
- **Date added to Google Fonts**: 2011-12-07
- **Font styles**: Regular (single weight)
- **Font version**: 1.000

## Upstream Repository

- **URL**: https://github.com/librefonts/fascinate
- **Commit**: `afac7a8ab8c537ef1b89ef6c5ae52a81567b9935` (only commit; "update .travis.yml", 2014-10-17)
- **Branch**: master
- **Repo created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Status**: Accessible, not archived

The librefonts organization (created 2013-10-20) hosts this repo. It contains a single commit by hash3g, which set up the repo with source files and a Travis CI configuration. This is not the original author's repository but rather a mirror/archive created by the librefonts project.

## Source Files

The repository contains only legacy source formats:

### VFB files (FontLab Studio proprietary, in `src/`):
- `Fascinate-Regular-OTF.vfb` -- merged contours, OTF-optimized
- `Fascinate-Regular-TTF.vfb` -- TrueType outlines with hinting
- `Fascinate-Regular.vfb` -- original source with contour overlaps

### TTX dumps (XML, in root and `src/`):
- Multiple per-table TTX files for both TTF and OTF versions

### No gftools-buildable sources:
- No `.glyphs`, `.glyphx`, `.ufo`, `.designspace`, or `.sfd` files
- No `config.yaml` or `sources.yaml`

## Binary File Analysis

The `Fascinate-Regular.ttf` in google/fonts has been unchanged since the initial commit (`90abd17b4`, 2015-03-07, by Dave Crossland). The font was originally added to Google Fonts on 2011-12-07, predating the current google/fonts repository.

- **File size**: 51,900 bytes
- **MD5**: `996b87c22f22f50c07246cd21f635d30`
- **Font created date (head table)**: 2011-12-01 04:38:00
- **Font modified date (head table)**: 2011-11-30 22:08:33

## google/fonts Commit History (ofl/fascinate/)

1. `90abd17b4` (2015-03-07) -- Initial commit (Dave Crossland) -- added all files
2. `480630de3` -- Tentative update to METADATA.pb textprotos
3. `27f377ab0` -- Update copyright field in METADATA.pb
4. `883939708` -- Remove METADATA.json files
5. `633ebadbf` -- Add language support metadata (#4160)
6. `28b492c0f` / `c6307ba83` / `701bd391b` -- Language metadata rollback/redo (#4677, #4706)
7. `6bda16478` -- Format HTML with new html formatter

The TTF binary was never modified after the initial commit.

## METADATA.pb Status

The current METADATA.pb on main has no `source { }` block. A source block was prepared on branch `sources_info_2026-02-25` (commit `9a14639f3`) pointing to `librefonts/fascinate` at commit `afac7a8`, but it has not been merged.

## Config Assessment

**No config.yaml is possible.** The upstream repo only has VFB sources, which are FontLab Studio proprietary binary files. These cannot be processed by gftools-builder or fontc. There is no way to create a config.yaml for this family without first converting the sources to an open format (.glyphs, .ufo, or .designspace).

## Designer Information

Brian J. Bonislawsky operates as Astigmatic (AOETI). Website: http://www.astigmatic.com/. Email: astigma@astigmatic.com. He designed both Fascinate and Fascinate Inline as companion faces -- the OFL license file in google/fonts reserves both names together.

## Conclusion

- **Repository URL**: https://github.com/librefonts/fascinate
- **Commit**: `afac7a8ab8c537ef1b89ef6c5ae52a81567b9935` (only commit in repo)
- **Config**: none (VFB-only sources, not buildable with gftools-builder)
- **Status**: complete (source block can be added, but no config.yaml is possible)
- **Confidence**: HIGH -- the librefonts repo is the only known upstream, and the commit is the only commit in the repo. The VFB sources match the font's original creation date (2011).

No further action is possible regarding config.yaml without source format conversion by the original designer.
