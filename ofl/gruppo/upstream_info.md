# Investigation Report: Gruppo

## Summary

Gruppo is a display/sans-serif typeface designed by Vernon Adams, added to Google Fonts on 2010-12-20. The font was updated in 2023 by Emma Marichal via gftools-packager (PR #6234), which restructured the upstream repo and regenerated the font from a Glyphs source file. The upstream repository at `https://github.com/googlefonts/GruppoFont` is valid and the commit hash `20e1bc8` in METADATA.pb correctly references the merge commit used for the 2023 update. An override `config.yaml` already exists in the google/fonts family directory. The source block is complete.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gruppo                                                             |
| Designer          | Vernon Adams                                                       |
| Date Added        | 2010-12-20                                                         |
| Repository URL    | https://github.com/googlefonts/GruppoFont                         |
| Commit Hash       | 20e1bc8c76ee1d692c5645b8aaf971cc58ca2e51                           |
| Branch            | master                                                             |
| Config            | Override config.yaml in google/fonts                               |
| Source Format     | Glyphs (.glyphs)                                                   |
| Source File       | sources/Gruppo.glyphs                                              |
| Status            | **complete**                                                       |
| Confidence        | HIGH                                                               |

## Investigation Details

### Upstream Repository

The upstream repo is `https://github.com/googlefonts/GruppoFont` (HTTP 200, verified accessible). It is cached locally at `fontc_crater_cache/googlefonts/GruppoFont`.

The repo has 10 commits total. The original font was pushed by Vernon Adams in 2012, with the source in UFO format (`src/Gruppo-Regular.ufo/`) and an SFD file. In April 2023, Emma Marichal submitted PR #1 to the upstream repo, which:
- Generated a Glyphs source file from the UFO source
- Restructured the repo into `sources/`, `fonts/ttf/`, `fonts/otf/`, `fonts/webfonts/` directories
- Moved the old UFO source to `sources/old/`
- Fixed anchors and kerning groups
- Exported new compiled fonts

The merge commit `20e1bc8` (2023-04-27) is the HEAD of the repo.

### Onboarding History

1. **Initial commit** (90abd17b, 2015-03-07): Font originally added to google/fonts.
2. **gftools-packager update** (d822fba5b, 2023-04-27, by Emma Marichal): Updated font to Version 1.001 from upstream commit `20e1bc8`. This is PR #6234, merged 2023-05-03.
3. **Sources info commit** (d63b7ea5d, 2025-11-10, by Felipe Sanches): Added override `config.yaml`.

### Commit Hash Verification

The commit hash `20e1bc8c76ee1d692c5645b8aaf971cc58ca2e51` is explicitly referenced in the gftools-packager commit message (d822fba5b) and in PR #6234's body. The commit is the merge of Emma Marichal's restructuring PR on the upstream repo, dated 2023-04-27. The gftools-packager commit in google/fonts is also dated 2023-04-27. The compiled TTF at `fonts/ttf/Gruppo-Regular.ttf` in the upstream repo at this commit matches the binary delivered to google/fonts. This is highly reliable.

### Build Configuration

- **Upstream config.yaml**: None exists in the upstream repo.
- **Override config.yaml**: Present in `ofl/gruppo/config.yaml` in google/fonts, containing:
  ```yaml
  buildVariable: false
  sources:
    - sources/Gruppo.glyphs
  ```
- The source file `sources/Gruppo.glyphs` exists at commit `20e1bc8` in the upstream repo.

### Current METADATA.pb Source Block

The existing source block in METADATA.pb is complete and correct:

```
source {
  repository_url: "https://github.com/googlefonts/GruppoFont"
  commit: "20e1bc8c76ee1d692c5645b8aaf971cc58ca2e51"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gruppo-Regular.ttf"
    dest_file: "Gruppo-Regular.ttf"
  }
  branch: "master"
}
```

## Conclusion

**Status: complete**

The source block in METADATA.pb is already complete with the correct repository URL, commit hash, file mappings, and branch. The override `config.yaml` in google/fonts correctly references the Glyphs source. No changes are needed.

### Recommended METADATA.pb Source Block

No changes needed. The existing block is correct:

```
source {
  repository_url: "https://github.com/googlefonts/GruppoFont"
  commit: "20e1bc8c76ee1d692c5645b8aaf971cc58ca2e51"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gruppo-Regular.ttf"
    dest_file: "Gruppo-Regular.ttf"
  }
  branch: "master"
}
```
