# Investigation Report: Happy Monkey

## Summary

Happy Monkey is a display sans-serif font designed by Brenda Gallo, added to Google Fonts on 2012-03-14. The font has never been updated since its initial addition to the catalog. An upstream repository exists at `https://github.com/librefonts/happymonkey` (a legacy `librefonts` archive), but it contains only VFB (FontLab Studio) source files and TTX decompositions -- no modern gftools-builder compatible sources (.glyphs, .ufo, .designspace). There is no METADATA.pb source block currently, and no config.yaml is possible since the sources cannot be built with gftools-builder.

## Key Findings

| Field            | Value |
|------------------|-------|
| Family Name      | Happy Monkey |
| Repository URL   | https://github.com/librefonts/happymonkey |
| Commit           | `5e49a946fe2459a69afa0ea0dfd501280cb61183` |
| Branch           | master |
| Config YAML      | N/A (no gftools-builder compatible sources) |
| Source Files     | `src/HappyMonkey-Regular-TTF.vfb`, `src/HappyMonkey-Regular-OTF.vfb` (FontLab format) |
| Status           | **no_config_possible** |
| Confidence       | HIGH |

## Investigation Details

### Onboarding History in google/fonts

Happy Monkey has a very short history in google/fonts:

1. **Commit 90abd17b4** (2015-03-07, Dave Crossland):
   - "Initial commit" -- this is the bulk initial import of all fonts into the current google/fonts repository
   - The font was originally added to Google Fonts on 2012-03-14 (per METADATA.pb `date_added`)
   - The TTF file has never been modified since this initial commit

2. **Subsequent commits** all touch only metadata files, not the font binary:
   - `8ccda7bf7` -- Fix fsType (no change to HappyMonkey files)
   - `49fbebd3d` -- chmod -x (only changed FONTLOG.txt permissions)
   - `480630de3` -- METADATA.pb textproto update
   - `883939708` -- Remove METADATA.json
   - Various language/metadata updates

### No Source Block in METADATA.pb

The current METADATA.pb has no `source { }` block at all. It only contains basic font metadata (name, designer, license, category, date_added, fonts, subsets).

### Upstream Repository Analysis

- **Repository**: `librefonts/happymonkey` (cached at `fontc_crater_cache/librefonts/happymonkey`)
- **Current HEAD**: `5e49a94` (2014-10-17) -- "update .travis.yml"
- **Shallow clone**: Yes (only 1 commit visible)
- **Remote**: `https://github.com/librefonts/happymonkey`

The repository is a legacy `librefonts` archive. The `librefonts` organization on GitHub was used to host decomposed font sources for fonts in the Google Fonts catalog, typically using Travis CI for automated builds.

### Source Files

The repository contains:
- `src/HappyMonkey-Regular-TTF.vfb` -- FontLab Studio 5 binary source (TTF flavor)
- `src/HappyMonkey-Regular-OTF.vfb` -- FontLab Studio 5 binary source (OTF flavor)
- Multiple `.ttx` decomposition files of the compiled font (TTX XML format)
- `.travis.yml` -- Travis CI config using legacy `fontbakery-build.py` toolchain
- `FONTLOG.txt`, `OFL.txt`, `METADATA.json` (legacy format)

There are NO `.glyphs`, `.ufo`, or `.designspace` files. VFB is a proprietary FontLab format that cannot be processed by gftools-builder. The TTX files are decompositions of the compiled binary, not editable design sources.

### Designer Information

- **Designer**: Brenda Gallo (gbrenda1987@gmail.com)
- **Spacing/Kerning**: Igino Marini (ikern.com)
- **Co-designer**: Gustavo Dipre (mentioned in DESCRIPTION.en_us.html)
- **Font version**: 1.001 (from 2012, never updated)

### No Config YAML Possible

Since the upstream repository has only VFB source files, which are:
1. Proprietary binary format (FontLab Studio 5)
2. Not supported by gftools-builder
3. Not supported by fontc

No `config.yaml` can be created for this font. The sources would need to be converted to a modern format (.glyphs, .ufo, or .designspace) before a gftools-builder config could be written.

## Conclusion

Happy Monkey has an upstream repository at `librefonts/happymonkey`, but it is a legacy archive containing only VFB and TTX files. No gftools-builder compatible sources exist, making a config.yaml impossible. The font binary has never been updated since its initial addition to Google Fonts in 2012.

### Recommended METADATA.pb Source Block

A minimal source block can document the repository URL and commit, even without a config_yaml:

```
source {
  repository_url: "https://github.com/librefonts/happymonkey"
  commit: "5e49a946fe2459a69afa0ea0dfd501280cb61183"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
```

**Status**: no_config_possible (VFB-only sources, not compatible with gftools-builder)
**Confidence**: HIGH
