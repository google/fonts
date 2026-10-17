# Investigation Report: Datatype

## Summary

Datatype is a variable font (with `wdth` and `wght` axes) designed by Frank Tisellano that turns text into charts. It was very recently added to Google Fonts on 2026-02-25 via PR #10267, authored by Emma Marichal. The upstream repository at `franktisellano/datatype` already has a complete source block in METADATA.pb with commit hash and repository URL. However, the font uses a custom Python-based build system rather than gftools-builder, so there is no config.yaml and none can be created.

## Key Findings

| Field               | Value                                                    |
|---------------------|----------------------------------------------------------|
| Family Name         | Datatype                                                 |
| Designer            | Frank Tisellano                                          |
| License             | OFL                                                      |
| Date Added          | 2026-02-25                                               |
| Repository URL      | https://github.com/franktisellano/datatype               |
| Commit Hash         | 1a17d767ba7fecd54d47ec11b2f7ed644a31513d                 |
| Branch              | main                                                     |
| Config YAML         | None (custom Python build system, not gftools-builder)   |
| Source Types         | Custom Python (sources/build.py, sources/font_builder.py)|
| Status              | no_config_possible                                       |
| Confidence          | HIGH                                                     |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/datatype/METADATA.pb` already has a **complete source block**:

```
source {
  repository_url: "https://github.com/franktisellano/datatype"
  commit: "1a17d767ba7fecd54d47ec11b2f7ed644a31513d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Datatype[wdth,wght].ttf"
    dest_file: "Datatype[wdth,wght].ttf"
  }
  branch: "main"
}
```

The font file is a variable font: `Datatype[wdth,wght].ttf` with width axis (50-150) and weight axis (100-900).

### Git History in google/fonts

Four commits touch this family:
1. `2a727e489` (2026-02-25, Emma Marichal): "Datatype: Version 1.202 added" -- initial onboarding
2. `2ed24956d`: "Remove IBM Plex copyright notice from OFL.txt"
3. `956f0091b`: "Add font information and contribution details to ARTICLE.en_us.html"
4. `91bf91951`: "Add sample_text section to METADATA.pb"

These were all merged via PR #10267 on 2026-02-26.

### Upstream Repository Verification

The repository `https://github.com/franktisellano/datatype` was created on 2026-02-15. The referenced commit `1a17d767ba7fecd54d47ec11b2f7ed644a31513d` was authored on 2026-02-23 with the message "gives well-deserved thanks to Emma and Dave for their guidance and support". This commit predates the PR merge on 2026-02-26, which is consistent.

The commit message in google/fonts explicitly states: "Taken from the upstream repo https://github.com/franktisellano/datatype at commit https://github.com/franktisellano/datatype/commit/1a17d767ba7fecd54d47ec11b2f7ed644a31513d."

### Source Files and Build System

The upstream repo does **not** use gftools-builder. Instead, it has a custom Python-based build system:

- `sources/build.py` -- Main build script that orchestrates font generation
- `sources/font_builder.py` -- Font building utilities
- `sources/config.py` -- Configuration for family name, axes, masters, instances
- `sources/glyphs/` -- Python modules that programmatically draw glyphs (bar charts, sparklines, pie charts)
- `sources/glyphs/base_imported.py` -- Imports base glyphs from IBM Plex Mono
- `Makefile` -- Runs `python sources/build.py`

The font is built programmatically rather than designed in a traditional font editor. There are no `.glyphs`, `.ufo`, or `.designspace` files. The build is invoked via `make build` which runs `python sources/build.py`.

No `config.yaml` exists in the upstream repo, and an override config.yaml cannot be created because there are no gftools-builder compatible source files.

The repo is **not cached locally** at `fontc_crater_cache/`. Due to disk space constraints (98%), no clone was performed.

### Onboarding Commit Verification

The commit hash `1a17d767ba7fecd54d47ec11b2f7ed644a31513d` is verified:
- It exists in the upstream repo on the `main` branch
- It was authored on 2026-02-23, three days before the PR merge on 2026-02-26
- The PR commit message explicitly references this exact commit
- The files entry references `fonts/variable/Datatype[wdth,wght].ttf` which is present at that commit

## Conclusion

**Status: no_config_possible**

The source block in METADATA.pb is already complete and correct. The font uses a custom Python build system (not gftools-builder), so no config.yaml is applicable. No changes are needed for this family.

### Current METADATA.pb source block (already correct)

```
source {
  repository_url: "https://github.com/franktisellano/datatype"
  commit: "1a17d767ba7fecd54d47ec11b2f7ed644a31513d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Datatype[wdth,wght].ttf"
    dest_file: "Datatype[wdth,wght].ttf"
  }
  branch: "main"
}
```
