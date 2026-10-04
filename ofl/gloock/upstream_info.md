# Investigation Report: Gloock

## Summary

Gloock is a display serif typeface designed by Duarte Pinto, onboarded to Google Fonts on 2023-01-06 via gftools-packager. The upstream repository at `https://github.com/duartp/gloock` is well-structured with Glyphs source files and a config.yaml. The METADATA.pb source block is complete with repository_url, commit hash, file mappings, branch, and config_yaml path. All data is correct and verified.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Gloock |
| Designer           | Duarte Pinto |
| Repository URL     | https://github.com/duartp/gloock |
| Commit Hash        | de92978ce821ae0cba86954b4c46abc70486981d |
| Config YAML        | sources/config.yaml (in upstream repo) |
| Source Type        | Glyphs (.glyphs) |
| Weights            | Regular (400) |
| Status             | complete |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a comprehensive source block:

```
source {
  repository_url: "https://github.com/duartp/gloock"
  commit: "de92978ce821ae0cba86954b4c46abc70486981d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gloock-Regular.ttf"
    dest_file: "Gloock-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

This includes file mappings, branch specification, and config_yaml path.

### Upstream Repository

- **URL**: https://github.com/duartp/gloock
- **Cached at**: upstream_repos/fontc_crater_cache/duartp/gloock
- **Remote verified**: Yes, remote origin matches

The repository contains a well-organized structure:
- `sources/Gloock.glyphs` - Glyphs source file
- `sources/config.yaml` - gftools-builder configuration
- `sources/other/Gloock-Regular.designspace` - Alternative designspace source
- `sources/other/Gloock-Regular.ufo/` - UFO source
- `fonts/ttf/Gloock-Regular.ttf` - Pre-compiled TTF binary
- `fonts/otf/Gloock-Regular.otf` - Pre-compiled OTF binary
- `OFL.txt`, `README.md`, `FONTLOG.txt` - Standard documentation
- `.github/workflows/build.yaml` - CI build configuration

### Config YAML Verification

The config.yaml at `sources/config.yaml` contains:

```yaml
sources:
  - Gloock.glyphs
familyName: Gloock
buildVariable: false
```

This is a valid gftools-builder configuration pointing to the Glyphs source file.

### Commit Hash Verification

The referenced commit `de92978` (2023-01-05, "Merge pull request #1 from emmamarichal/main") is the only commit in the repository. It is a merge commit where Emma Marichal's PR set up the entire repository structure. This is confirmed by the gftools-packager message in google/fonts commit `65b8ac26c`:

> "Gloock Version 1.000; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/duartp/gloock at commit https://github.com/duartp/gloock/commit/de92978ce821ae0cba86954b4c46abc70486981d"

The onboarding happened the next day (2023-01-06) by Emma Marichal, just one day after the upstream commit (2023-01-05). The commit hash is definitively correct.

### Google Fonts History

- **Onboarding** (65b8ac26c, 2023-01-06): Added by Emma Marichal via gftools-packager with the pre-compiled TTF from the upstream repo.
- The TTF file has not been updated since onboarding.

## Conclusion

This is a fully complete and well-documented source block. All fields are correct: repository_url, commit hash, file mappings, branch, and config_yaml path. No changes needed.

### Recommended METADATA.pb Source Block

No changes needed. The existing source block is correct:

```
source {
  repository_url: "https://github.com/duartp/gloock"
  commit: "de92978ce821ae0cba86954b4c46abc70486981d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gloock-Regular.ttf"
    dest_file: "Gloock-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

### Status: complete

All source metadata is present and verified. No corrections needed.
