# Investigation Report: Gideon Roman

## Summary

Gideon Roman is a display serif typeface designed by Robert Leuschke, onboarded to Google Fonts on 2021-08-26. The upstream repository is `googlefonts/gideon`, which contains a single commit with the full project. The METADATA.pb source block is complete and accurate, with the correct commit hash, repository URL, and config path.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gideon Roman                                                       |
| Designer          | Robert Leuschke                                                    |
| Repository URL    | https://github.com/googlefonts/gideon                              |
| Commit Hash       | c7220310f3d5a41af5c7906b3c33672a0a2146c8                           |
| Branch            | master                                                             |
| Config Path       | sources/config.yml                                                 |
| Source Format     | .glyphs (sources/GideonRoman.glyphs)                               |
| Status            | **complete**                                                       |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The existing source block in `ofl/gideonroman/METADATA.pb` contains:
- `repository_url`: https://github.com/googlefonts/gideon
- `commit`: c7220310f3d5a41af5c7906b3c33672a0a2146c8
- `branch`: master
- `config_yaml`: sources/config.yml
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and GideonRoman-Regular.ttf

### Google Fonts Git History

The onboarding commit in google/fonts is `b1573ad2c` (2021-08-31) by Viviana Monsalve:

> Gideon Roman: Version 2.010 added (#3770)
>
> [gftools-packager] Gideon Roman: Version 2.010 added
>
> Gideon Roman Version 2.010 taken from the upstream repo https://github.com/googlefonts/gideon at commit https://github.com/googlefonts/gideon/commit/c7220310f3d5a41af5c7906b3c33672a0a2146c8.

This was PR #3770. The commit message explicitly references the upstream commit hash, which matches what is in METADATA.pb.

### Upstream Repository Verification

The upstream repo at `googlefonts/gideon` (cached at `fontc_crater_cache/googlefonts/gideon/`) contains exactly one commit:

- `c722031` - "Renamed to Gideon Roman" (2021-08-26, by Viviana Monsalve)

This is the only commit in the entire repository, so there is no ambiguity about which commit was used.

### Source Files and Config

The repository contains:
- `sources/GideonRoman.glyphs` -- Glyphs source file
- `sources/config.yml` -- gftools-builder configuration (note: `.yml` extension, not `.yaml`)

The config.yml content:
```yaml
sources:
  - GideonRoman.glyphs
familyName: "Gideon Roman"
buildVariable: false
autohintTTF: false
```

The METADATA.pb correctly references `sources/config.yml` (with the `.yml` extension).

### No Override Config

There is no override `config.yaml` in the google/fonts family directory (`ofl/gideonroman/`). The upstream config is used directly.

## Conclusion

The METADATA.pb source block for Gideon Roman is complete and accurate. No corrections are needed.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/gideon"
  commit: "c7220310f3d5a41af5c7906b3c33672a0a2146c8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/GideonRoman-Regular.ttf"
    dest_file: "GideonRoman-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

**Status: complete** -- All source metadata is correct and verified.
