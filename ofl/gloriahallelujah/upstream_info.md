# Investigation Report: Gloria Hallelujah

## Summary

Gloria Hallelujah is a handwriting font designed by Kimberly Geswein, added to Google Fonts in 2011. The upstream repository at `https://github.com/librefonts/gloriahallelujah` contains only TTX-decomposed font tables and a FontLab VFB source file. There are no gftools-builder compatible sources (.glyphs, .ufo, .designspace, or .sfd). The METADATA.pb currently has no source block on main. A source block was prepared on a separate branch (`sources_info_2026-02-25`) but has not been merged.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Gloria Hallelujah |
| Designer           | Kimberly Geswein |
| Repository URL     | https://github.com/librefonts/gloriahallelujah |
| Commit Hash        | 1fd8b2f0f0dd8fe36f738733df0f869676b958e4 |
| Config YAML        | None (VFB-only sources, not buildable by gftools-builder) |
| Source Type        | FontLab VFB (.vfb) + TTX tables |
| Weights            | Regular (400) |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb on main has **no source block**. It contains only basic metadata: name, designer, license, category, date_added, font definition, subsets, and classifications.

A source block was added in commit `9a14639f3c` on branch `sources_info_2026-02-25` (by Felipe Sanches, 2026-02-25) with repository_url and commit hash, but this has not been merged to main.

### Upstream Repository

- **URL**: https://github.com/librefonts/gloriahallelujah
- **Cached at**: upstream_repos/fontc_crater_cache/librefonts/gloriahallelujah
- **Remote verified**: Yes, remote origin matches

The repository contains a single commit (`1fd8b2f`, 2014-10-17, author: hash3g) with:
- `src/GloriaHallelujah.vfb` - FontLab VFB source file (binary, proprietary format)
- `src/METADATA_comments.txt` - Build/subsetting comments
- `src/VERSIONS.txt` - Records "Version 1.004 2010"
- `GloriaHallelujah.ttf.*.ttx` - TTX-decomposed font tables (glyf, cmap, head, etc.)
- `GloriaHallelujah.ttf.ttx` - Main TTX index file
- `METADATA.json` - Legacy metadata
- `OFL.txt` - License
- `.travis.yml` - CI configuration

There is **no config.yaml** in the upstream repo and **no gftools-builder compatible sources**. The VFB format is a proprietary FontLab format that cannot be used with gftools-builder. The TTX files are decomposed font tables, not a standard build source.

### Commit Hash Verification

Commit `1fd8b2f` is the only commit in the repository. It was created on 2014-10-17 by hash3g (likely a Google Fonts team member involved in the librefonts archive). The repository appears to be an archival copy of the font sources, not an active development repository.

The font was added to Google Fonts much earlier (date_added: 2011-07-27), and the google/fonts initial commit (90abd17b4, 2015-03-07) included the font. The TTF file received one modification in google/fonts (8ccda7bf7, 2015-08-05, "Fix fsType for 40 font files"), and one deploy-related change (76adaf1d2, 2021-11-01).

### Source File Limitations

The only source file (`GloriaHallelujah.vfb`) is in FontLab's proprietary binary format (.vfb). This format:
- Cannot be read by gftools-builder
- Cannot be read by fontc
- Requires FontLab Studio (legacy proprietary software) to open
- Is not convertible to modern formats without FontLab

Therefore, creating a config.yaml for this family is not possible with current build tools.

### Google Fonts History

- **Initial commit** (90abd17b4, 2015-03-07): Font included in the initial commit of google/fonts.
- **fsType fix** (8ccda7bf7, 2015-08-05): TTF binary modified to fix the fsType embedding flag.
- **Deploy** (76adaf1d2, 2021-11-01): A deploy commit touched the file.
- No further updates to the font binary.

## Conclusion

The upstream repository is an archival copy containing only VFB sources and TTX decompositions, neither of which is compatible with gftools-builder. A source block should be added to METADATA.pb with the repository_url and commit hash, but no config.yaml is possible.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/gloriahallelujah"
  commit: "1fd8b2f0f0dd8fe36f738733df0f869676b958e4"
}
```

Note: This source block was already prepared on branch `sources_info_2026-02-25` but not yet merged to main.

### Status: no_config_possible

The upstream repository only contains VFB (FontLab proprietary) sources. No gftools-builder compatible sources exist, making a config.yaml impossible without source format conversion.
