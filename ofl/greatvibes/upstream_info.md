# Investigation: Great Vibes

## Summary

Great Vibes is a script/handwriting font by Robert Leuschke, originally added to Google Fonts on 2012-03-29 and significantly updated in March 2024 with extended language support (Cyrillic, Greek). The upstream repository is `googlefonts/great-vibes` on GitHub. The METADATA.pb already contains a complete source block with the correct repository URL, commit hash, and config_yaml path. The upstream repo has gftools-builder compatible sources (.glyphs) with a `config.yaml` file.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Great Vibes                                                        |
| Designer          | Robert Leuschke                                                    |
| Repository URL    | https://github.com/googlefonts/great-vibes                         |
| Commit Hash       | f95eb967a3414e5accd65f4fa653c47f607654fa                           |
| Config YAML       | sources/config.yaml                                                |
| Source Files      | sources/GreatVibes-Pro.glyphs                                      |
| Status            | **complete**                                                       |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/greatvibes/METADATA.pb` contains a source block with:
- `repository_url`: https://github.com/googlefonts/great-vibes
- `commit`: f95eb967a3414e5accd65f4fa653c47f607654fa
- `archive_url`: https://github.com/googlefonts/great-vibes/releases/download/v1.103/great-vibes-v1.103.zip
- `branch`: master
- `config_yaml`: sources/config.yaml
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and GreatVibes-Regular.ttf

Note: The file mappings are duplicated (each file mapping appears twice). This is a minor data quality issue but does not affect functionality.

### Git History in google/fonts

The font has been updated multiple times:

1. **Initial commit** (`90abd17b4`, 2015-03-07): Part of bulk initial import (font had been in Google Fonts since 2012-03-29)
2. **Version 1.010 update** (`59adf74d6`, 2021-06-14) by Viviana Monsalve: "Great Vibes: Version 1.010; ttfautohint (v1.8.3) added (#3528)" -- taken from upstream commit `40810389f7f44d1b7101bcce88294f485b590b80`
3. **Version 1.103 update** (`a6039f387`, 2024-03-28) by Viviana Monsalve: "Great Vibes: Version 1.103; ttfautohint (v1.8.4.7-5d5b) added" -- taken from upstream commit `f95eb967a3414e5accd65f4fa653c47f607654fa`

The most recent update (v1.103) is the one referenced in the current METADATA.pb source block. The commit message explicitly states the font was taken from:
- Upstream repo: https://github.com/googlefonts/great-vibes
- Commit: https://github.com/googlefonts/great-vibes/commit/f95eb967a3414e5accd65f4fa653c47f607654fa

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/great-vibes/` has a single commit (`f95eb96`) dated 2024-03-28, titled "v1.003 font dot circle fix".

Repository contents:
- `sources/GreatVibes-Pro.glyphs` -- Glyphs source file
- `sources/config.yaml` -- gftools-builder configuration
- `sources/CustomFilter_GreatVibes.plist` -- Glyphs custom filter
- `fonts/ttf/GreatVibes-Regular.ttf` -- built font file
- `fonts/webfonts/GreatVibes-Regular.woff2` -- web font
- `OFL.txt`, `Documentation/`, `AUTHORS.txt`, `CONTRIBUTORS.txt`
- `Makefile`, `scripts/`, `requirements.txt`
- `.github/workflows/build.yaml` -- CI/CD workflow
- `PDF tests/` -- test files

The config.yaml contains:
```yaml
sources:
  - GreatVibes-Pro.glyphs
familyName: "Great Vibes"
buildVariable: false
buildOTF: false
```

### Commit Hash Verification

The upstream repo has only a single commit (`f95eb967a3414e5accd65f4fa653c47f607654fa`, dated 2024-03-28), so there is no ambiguity. The google/fonts update commit (`a6039f387`, also dated 2024-03-28) was made the same day, and the commit message explicitly references this exact upstream commit. The dates perfectly align.

### Note on Duplicated File Mappings

The METADATA.pb contains duplicate `files {}` entries -- the OFL.txt, DESCRIPTION.en_us.html, and fonts/ttf/GreatVibes-Regular.ttf mappings each appear twice. This appears to be a data entry issue but does not affect the correctness of the source metadata.

## Conclusion

The METADATA.pb source block is complete and correct. The only minor issue is the duplicated file mappings, which could be cleaned up but are not functionally problematic.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/googlefonts/great-vibes"
  commit: "f95eb967a3414e5accd65f4fa653c47f607654fa"
  archive_url: "https://github.com/googlefonts/great-vibes/releases/download/v1.103/great-vibes-v1.103.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/GreatVibes-Regular.ttf"
    dest_file: "GreatVibes-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

Note: The recommended block above removes the duplicate file entries present in the current METADATA.pb.

**Status: complete** -- All source metadata fields are present and verified.
