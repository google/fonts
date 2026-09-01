# Investigation Report: Geist

## Summary

Geist is a sans-serif variable font by Vercel (designers: Andres Briganti, Mateo Zaragoza, and others). It was onboarded to Google Fonts on 2024-10-24 via PR #8246 by Viviana Monsalve. Both Geist and Geist Mono share the same upstream repository (`vercel/geist-font`) and the same onboarding commit. The METADATA.pb already has a complete source block with repository URL, commit hash, config.yaml path, archive URL, and file mappings. This family is fully documented.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Geist                                                              |
| Repository URL    | https://github.com/vercel/geist-font                              |
| Commit Hash       | a6d260e6cbc07eafdfad438f33601fe3c38b1e6f (updated 2026-04-03; was b193ef74010119759bfb7f71ddf81a3dee238535) |
| Commit Date       | 2026-04-02                                                         |
| Commit Message    | Merge pull request #216 from emmamarichal/main — Update Geist and Geist Mono |
| Config YAML       | sources/config-Geist.yaml (in upstream repo)                      |
| Source Files      | sources/Geist.glyphspackage                                       |
| Onboarding PR     | #8246 (google/gftools_packager_ofl_geist)                         |
| Onboarder         | Viviana Monsalve (viviana.monsalve.a@gmail.com)                   |
| Date Added        | 2024-10-02                                                        |
| Status            | complete                                                          |
| Confidence        | HIGH                                                              |

## Investigation Details

### 1. METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/vercel/geist-font"
  commit: "b193ef74010119759bfb7f71ddf81a3dee238535"
  config_yaml: "sources/config-Geist.yaml"
  archive_url: "https://github.com/vercel/geist-font/releases/download/1.4.01/Geist-1.4.01.zip"
  files {
    source_file: "variable/Geist[wght].ttf"
    dest_file: "Geist[wght].ttf"
  }
  branch: "main"
}
```

All fields are populated. The `config_yaml` field was added later in commit `cbe1f7ee5` (2025-04-03) by Felipe Sanches.

### 2. Git History in google/fonts

The onboarding history:

1. **Commit `56681a845`** (2024-10-23, Viviana Monsalve): "Geist: Version 1.401 added"
   - Message: "Taken from the upstream repo https://github.com/vercel/geist-font at commit b193ef74..."
   - Resolves issue #6922
   - Added: Geist[wght].ttf, METADATA.pb, article/ARTICLE.en_us.html

2. **Merge `c0b7dced4`** (2024-10-24, Emma Marichal): "Merge pull request #8246 from google/gftools_packager_ofl_geist"
   - Title: "Geist: Version 1.400 added"
   - Also added OFL.txt and article banner image

3. **Commit `cbe1f7ee5`** (2025-04-03, Felipe Sanches): "sources for Geist & Geist Mono"
   - Added `config_yaml` field to METADATA.pb source block

### 3. Upstream Repository

The upstream repo at https://github.com/vercel/geist-font is shared by both Geist and Geist Mono. The referenced commit `b193ef74` (2024-10-23) is a merge commit "Merge pull request #141 from vercel/139-fixes" at the HEAD of the main branch.

The commit date (2024-10-23) is the same day as the google/fonts onboarding commit, confirming it was used for the onboarding.

### 4. Source Files at Referenced Commit

At commit `b193ef74`, the `sources/` directory contains:
- `sources/Geist.glyphspackage` (Glyphs 3 package format)
- `sources/GeistMono.glyphspackage` (for Geist Mono)
- `sources/config-Geist.yaml` (gftools-builder config)
- `sources/config-GeistMono.yaml` (gftools-builder config for Mono)
- `sources/CustomFilter_GF_Latin_All.plist`

### 5. Config YAML

The `sources/config-Geist.yaml` at the referenced commit configures:
- Source: `Geist.glyphspackage`
- Output directory: `../fonts/Geist`
- Family name: "Geist"
- Autohint OTF: true
- STAT table with weight axis (100-900) and italic axis

### 6. Repository Cache

The upstream repo is cached at `upstream_repos/fontc_crater_cache/vercel/geist-font/`. The repo is clean and checked out at the referenced commit `b193ef74`.

## Conclusion

Geist has a fully complete source block in METADATA.pb. The repository URL, commit hash, config.yaml path, archive URL, and file mappings are all correct and verified. No changes are needed.

### Current METADATA.pb Source Block (already correct)

```
source {
  repository_url: "https://github.com/vercel/geist-font"
  commit: "b193ef74010119759bfb7f71ddf81a3dee238535"
  config_yaml: "sources/config-Geist.yaml"
  archive_url: "https://github.com/vercel/geist-font/releases/download/1.4.01/Geist-1.4.01.zip"
  files {
    source_file: "variable/Geist[wght].ttf"
    dest_file: "Geist[wght].ttf"
  }
  branch: "main"
}
```

### Status: complete
### Confidence: HIGH

## Recent upstream/main activity (post-investigation)

- **2026-04-02 (upstream)** — skullface, upstream commit [`a6d260e6c`](https://github.com/vercel/geist-font/commit/a6d260e6c) ("Merge pull request #216 from emmamarichal/main — Update Geist and Geist Mono"). Advanced upstream `main` from `b193ef740...` to `a6d260e6c...` and produced new v1.800 (Geist) and v1.700 (Geist Mono) binaries. The PR was authored by emmamarichal upstream — same person who later onboarded the binaries to google/fonts.
- **2026-04-03** — Emma Marichal, commit [`87a44ad3d`](https://github.com/google/fonts/commit/87a44ad3d) ("Geist: Version 1.800 added"): onboarded the upstream update via gftools-packager. Updates to METADATA.pb included:
  - `commit` advanced from `b193ef740...` to `a6d260e6c...`
  - Italic font entry added; subsets `cyrillic-ext` and `vietnamese` added
  - Removed `archive_url` (was `1.4.01/Geist-1.4.01.zip`)
  - File mapping path changed: `variable/Geist[wght].ttf` → `fonts/Geist/variable/Geist[wght].ttf` (upstream layout reorganized)
  - `config_yaml` field updated path: still `sources/config-Geist.yaml` (unchanged in upstream)

The shipping `Geist[wght].ttf` (169056 bytes, md5 `3f599483f71a2100bf53030faeddd23f`) is byte-identical to upstream `fonts/Geist/variable/Geist[wght].ttf` at commit `a6d260e6c`. `head.fontRevision = 1.8000`, `name` ID 5 = "Version 1.800".

The Key Findings table at the top of this document has been updated to reflect the new commit.

## Confidence (post-update)

**High**: Md5 verification of the shipping `Geist[wght].ttf` against upstream `a6d260e6c:fonts/Geist/variable/Geist[wght].ttf` was byte-identical. The recorded source-block fields are correct and current.
