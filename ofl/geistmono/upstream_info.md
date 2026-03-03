# Investigation Report: Geist Mono

## Summary

Geist Mono is a monospace variable font by Vercel, the companion to Geist sans-serif. It shares the same upstream repository (`vercel/geist-font`) and was onboarded at the same commit as Geist. The METADATA.pb already has a complete source block with all required fields. This family is fully documented.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Geist Mono                                                         |
| Repository URL    | https://github.com/vercel/geist-font                              |
| Commit Hash       | b193ef74010119759bfb7f71ddf81a3dee238535                           |
| Commit Date       | 2024-10-23                                                        |
| Commit Message    | Merge pull request #141 from vercel/139-fixes                     |
| Config YAML       | sources/config-GeistMono.yaml (in upstream repo)                  |
| Source Files      | sources/GeistMono.glyphspackage                                   |
| Onboarding PR     | #8264 (google/gftools_packager_ofl_geistmono)                     |
| Onboarder         | Viviana Monsalve (viviana.monsalve.a@gmail.com)                   |
| Date Added        | 2024-10-03                                                        |
| Status            | complete                                                          |
| Confidence        | HIGH                                                              |

## Investigation Details

### 1. METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/vercel/geist-font"
  commit: "b193ef74010119759bfb7f71ddf81a3dee238535"
  config_yaml: "sources/config-GeistMono.yaml"
  archive_url: "https://github.com/vercel/geist-font/releases/download/1.4.01/GeistMono-1.4.01.zip"
  files {
    source_file: "variable/GeistMono[wght].ttf"
    dest_file: "GeistMono[wght].ttf"
  }
  branch: "main"
}
```

All fields are populated. The `config_yaml` field was added in commit `cbe1f7ee5` (2025-04-03) by Felipe Sanches, alongside the same addition for Geist.

### 2. Git History in google/fonts

The onboarding history:

1. **Commit `9ccc85496`** (2024-10-23, Viviana Monsalve): "Geist Mono: Version 1.401 added"
   - Message: "Taken from the upstream repo https://github.com/vercel/geist-font at commit b193ef74..."
   - Resolves issue #6922 (same issue as Geist)
   - Added: GeistMono[wght].ttf, METADATA.pb, article/ARTICLE.en_us.html

2. **Merge `90f16f651`** (2024-10-24, Emma Marichal): "Merge pull request #8264 from google/gftools_packager_ofl_geistmono"
   - Title: "Geist Mono: Version 1.400 added"
   - Also added OFL.txt and article banner image

3. **Commit `cbe1f7ee5`** (2025-04-03, Felipe Sanches): "sources for Geist & Geist Mono"
   - Added `config_yaml` field to METADATA.pb source block

### 3. Upstream Repository (Shared with Geist)

Geist Mono shares the upstream repository https://github.com/vercel/geist-font with the Geist sans-serif family. Both were onboarded from the same commit `b193ef74` (2024-10-23), which is a merge commit "Merge pull request #141 from vercel/139-fixes".

The repository contains separate source files and config files for each family:
- Geist: `sources/Geist.glyphspackage` + `sources/config-Geist.yaml`
- Geist Mono: `sources/GeistMono.glyphspackage` + `sources/config-GeistMono.yaml`

### 4. Source Files at Referenced Commit

At commit `b193ef74`, the Geist Mono sources consist of:
- `sources/GeistMono.glyphspackage` (Glyphs 3 package format)
- `sources/config-GeistMono.yaml` (gftools-builder config)

### 5. Config YAML

The `sources/config-GeistMono.yaml` at the referenced commit configures:
- Source: `GeistMono.glyphspackage`
- Output directory: `../fonts/GeistMono`
- Family name: "Geist Mono"
- Autohint OTF: true
- STAT table with weight axis (100-900) and italic axis

### 6. Repository Cache

The upstream repo is cached at `upstream_repos/fontc_crater_cache/vercel/geist-font/` (shared with Geist).

### 7. Relationship to Geist

Both Geist and Geist Mono:
- Share the same upstream repository (`vercel/geist-font`)
- Were onboarded from the same commit (`b193ef74`)
- Were onboarded on the same day (2024-10-23) by the same person (Viviana Monsalve)
- Resolve the same issue (#6922)
- Were merged via adjacent PRs (#8246 for Geist, #8264 for Geist Mono)
- Had their `config_yaml` fields added in the same commit (`cbe1f7ee5`)

## Conclusion

Geist Mono has a fully complete source block in METADATA.pb. The repository URL, commit hash, config.yaml path, archive URL, and file mappings are all correct and verified. No changes are needed.

### Current METADATA.pb Source Block (already correct)

```
source {
  repository_url: "https://github.com/vercel/geist-font"
  commit: "b193ef74010119759bfb7f71ddf81a3dee238535"
  config_yaml: "sources/config-GeistMono.yaml"
  archive_url: "https://github.com/vercel/geist-font/releases/download/1.4.01/GeistMono-1.4.01.zip"
  files {
    source_file: "variable/GeistMono[wght].ttf"
    dest_file: "GeistMono[wght].ttf"
  }
  branch: "main"
}
```

### Status: complete
### Confidence: HIGH
