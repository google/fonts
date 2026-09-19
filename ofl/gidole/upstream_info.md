# Investigation Report: Gidole

## Summary

Gidole is a sans-serif typeface designed by Andreas Larsen, onboarded to Google Fonts on 2025-02-26. The upstream repository is `googlefonts/gidole`, which was forked/migrated from the original designer's repository. The METADATA.pb source block is complete and accurate, with the correct commit hash, repository URL, and config path.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gidole                                                             |
| Designer          | Andreas Larsen                                                     |
| Repository URL    | https://github.com/googlefonts/gidole                              |
| Commit Hash       | 8568937c577ea42b7c2655d93a5d822222c08321                           |
| Branch            | master                                                             |
| Config Path       | sources/config.yaml                                                |
| Source Format     | .glyphspackage (sources/Gidole-Regular.glyphspackage)              |
| Status            | **complete**                                                       |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The existing source block in `ofl/gidole/METADATA.pb` contains:
- `repository_url`: https://github.com/googlefonts/gidole
- `commit`: 8568937c577ea42b7c2655d93a5d822222c08321
- `branch`: master
- `config_yaml`: sources/config.yaml
- File mappings for OFL.txt, Gidole-Regular.ttf, article/ARTICLE.en_us.html, and several article images

### Google Fonts Git History

The onboarding commit in google/fonts is `b0d76e3f4` (2025-02-26) by Yanone:

> Gidole: Version 2.100; ttfautohint (v1.8.4.7-5d5b) added
>
> Taken from the upstream repo https://github.com/googlefonts/gidole at commit https://github.com/googlefonts/gidole/commit/8568937c577ea42b7c2655d93a5d822222c08321.
>
> Resolves #341

This was merged via PR #9122. The commit message explicitly references the upstream commit hash, which matches METADATA.pb.

### Upstream Repository Verification

The upstream repo at `googlefonts/gidole` (cached at `fontc_crater_cache/googlefonts/gidole/`) contains a single commit:

- `8568937` - "Added article" (the HEAD and only commit)

This is the only commit in the repository, so the hash is unambiguous.

### Source Files and Config

The repository contains:
- `sources/Gidole-Regular.glyphspackage/` -- Glyphs package source file
- `sources/config.yaml` -- gftools-builder configuration
- `SFD/` -- Legacy FontForge SFD sources (including several variants: Hairline, Mono, Alternates, etc.)

The config.yaml content:
```yaml
sources:
  - Gidole-Regular.glyphspackage
buildTTF: true
buildOTF: false
buildWebfont: false
```

The METADATA.pb correctly references `sources/config.yaml`.

### Notable: Legacy SFD Sources

The repository also contains a `SFD/` directory with FontForge source files for multiple variants (Regular, Hairline, Thin, Mono, Semibold, Alternates), suggesting the project was originally developed in FontForge and later converted to Glyphs format for the Google Fonts onboarding. Only the Regular weight was onboarded.

### No Override Config

There is no override `config.yaml` in the google/fonts family directory (`ofl/gidole/`). The upstream config is used directly.

## Conclusion

The METADATA.pb source block for Gidole is complete and accurate. No corrections are needed.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/gidole"
  commit: "8568937c577ea42b7c2655d93a5d822222c08321"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gidole-Regular.ttf"
    dest_file: "Gidole-Regular.ttf"
  }
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "article/1Gidole.png"
    dest_file: "article/1Gidole.png"
  }
  files {
    source_file: "article/2GidoleCapital.png"
    dest_file: "article/2GidoleCapital.png"
  }
  files {
    source_file: "article/3GidoleLowercase.png"
    dest_file: "article/3GidoleLowercase.png"
  }
  files {
    source_file: "article/4GidoleNumbers.png"
    dest_file: "article/4GidoleNumbers.png"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

**Status: complete** -- All source metadata is correct and verified.
