# Investigation: Grape Nuts

## Summary

Grape Nuts is a handwriting font by Robert Leuschke, added to Google Fonts on 2022-02-17. The upstream repository is `googlefonts/grapenuts` on GitHub. The METADATA.pb already contains a complete source block with the correct repository URL, commit hash, and config_yaml path. The upstream repo has a single commit and contains gftools-builder compatible sources (.glyphs) with a `config.yml` file.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Grape Nuts                                                         |
| Designer          | Robert Leuschke                                                    |
| Repository URL    | https://github.com/googlefonts/grapenuts                           |
| Commit Hash       | 1313fb48d7196fd9388b8327d1a30c03323c33ee                           |
| Config YAML       | sources/config.yml                                                 |
| Source Files      | sources/GrapeNuts.glyphs                                           |
| Status            | **complete**                                                       |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/grapenuts/METADATA.pb` already contains a complete source block:
- `repository_url`: https://github.com/googlefonts/grapenuts
- `commit`: 1313fb48d7196fd9388b8327d1a30c03323c33ee
- `branch`: main
- `config_yaml`: sources/config.yml
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and GrapeNuts-Regular.ttf

### Git History in google/fonts

The font was onboarded in commit `37f5e5ac2` (2022-02-23) by Viviana Monsalve, with the message:

> Grape Nuts: Version 1.010; ttfautohint (v1.8.3) added (#4322)

The commit body explicitly states the font was taken from:
- Upstream repo: https://github.com/googlefonts/grapenuts
- Commit: https://github.com/googlefonts/grapenuts/commit/1313fb48d7196fd9388b8327d1a30c03323c33ee

The source block was later added in two stages:
1. Commit `66f91f10f` (2024-04-03) by Simon Cozens: "Merge upstream.yaml into METADATA.pb" -- added repository_url, file mappings, and branch.
2. Commit `19cdcec59` (2025-03-31) by Felipe Sanches: "[Batch 1/4] port info from fontc_crater targets list" -- added commit hash and config_yaml.

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/grapenuts/` contains a single commit (`1313fb4`) dated 2022-02-17, which matches the commit hash referenced in METADATA.pb.

Repository contents:
- `sources/GrapeNuts.glyphs` -- Glyphs source file
- `sources/config.yml` -- gftools-builder configuration
- `fonts/ttf/GrapeNuts-Regular.ttf` -- built font file
- `OFL.txt`, `documentation/`, `AUTHORS.txt`, `CONTRIBUTORS.txt`

The config.yml contains:
```yaml
sources:
  - GrapeNuts.glyphs
familyName: "Grape Nuts"
buildVariable: false
```

Note: The config file uses `.yml` extension (not `.yaml`), and the METADATA.pb correctly references `sources/config.yml`.

### Commit Hash Verification

The upstream repo has only a single commit (`1313fb48d7196fd9388b8327d1a30c03323c33ee`, dated 2022-02-17), so there is no ambiguity. The onboarding commit in google/fonts (2022-02-23) references this exact commit, and the dates align (upstream commit is 6 days before the google/fonts merge).

## Conclusion

The METADATA.pb source block is complete and correct. No changes are needed.

### Recommended METADATA.pb source block (already present)

```
source {
  repository_url: "https://github.com/googlefonts/grapenuts"
  commit: "1313fb48d7196fd9388b8327d1a30c03323c33ee"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/GrapeNuts-Regular.ttf"
    dest_file: "GrapeNuts-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

**Status: complete** -- All source metadata fields are present and verified.
