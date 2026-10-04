# Investigation Report: Gabarito

## Summary

Gabarito is a display sans-serif variable font (weight 400-900) designed by Naipe Foundry (Leandro Assis, Alvaro Franca, Felipe Casaprima), added to Google Fonts on 2023-09-13. The upstream repository at `naipefoundry/gabarito` contains a single commit (a merge of Emma Marichal's onboarding PR) which is both HEAD and the commit referenced in METADATA.pb. The source block is fully populated. The upstream repo has a `sources/config.yaml` with gftools-builder configuration and a `.glyphs` source file.

## Key Findings

| Field | Value |
|---|---|
| Family Name | Gabarito |
| Upstream Repo | https://github.com/naipefoundry/gabarito |
| Commit Hash | `1f3fb39d6449eefa880543f109f33ede0cd4064f` |
| Branch | main |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Source Files | `sources/Gabarito.glyphs` |
| Status | **complete** |
| Confidence | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/naipefoundry/gabarito"
  commit: "1f3fb39d6449eefa880543f109f33ede0cd4064f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Gabarito[wght].ttf"
    dest_file: "Gabarito[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

### Onboarding History in google/fonts

The font was onboarded via gftools-packager in commit `cd21f74a2` (2023-09-13) by Emma Marichal:

> [gftools-packager] Gabarito: Version 1.000 added
> Gabarito Version 1.000 taken from the upstream repo https://github.com/naipefoundry/gabarito at commit https://github.com/naipefoundry/gabarito/commit/1f3fb39d6449eefa880543f109f33ede0cd4064f.

The `config_yaml` field was added later in commit `19cdcec59` (2025-03-31, Batch 1/4 fontc_crater targets).

### Commit History in google/fonts for ofl/gabarito/

1. `cd21f74a2` (2023-09-13) - Initial onboarding: Gabarito v1.000 (gftools-packager)
2. `121351c2e` - Description and metadata updates
3. `ddc6948ed` - Designer order updated
4. `98dc03f72` - Added Naipe Foundry in designers list
5. `66f91f10f` - Merge upstream.yaml into METADATA.pb
6. `b2ecfc3f0` - Add gabarito article
7. `19cdcec59` (2025-03-31) - Added `config_yaml: "sources/config.yaml"`

### Upstream Repository Analysis

- **URL**: https://github.com/naipefoundry/gabarito
- **Cached at**: `upstream_repos/fontc_crater_cache/naipefoundry/gabarito`
- **Default branch**: main
- **Total commits**: 1 (single merge commit)
- **HEAD**: `1f3fb39d6449eefa880543f109f33ede0cd4064f` (2023-09-11)

The repository contains a single merge commit: "Merge pull request #1 from emmamarichal/main". This is the standard gftools-packager pattern where Emma Marichal prepared the upstream repo structure in a PR.

### Commit Hash Verification

The commit hash `1f3fb39d6449eefa880543f109f33ede0cd4064f` is verified correct:

1. It is the only commit in the repo and matches HEAD
2. It is explicitly referenced in the gftools-packager commit message in google/fonts
3. The upstream merge commit date (2023-09-11) is 2 days before the google/fonts onboarding (2023-09-13), which is a typical turnaround time
4. The font binary `fonts/variable/Gabarito[wght].ttf` in the upstream repo is 158,144 bytes

### Source Files and Build Configuration

The upstream repo contains:
- `sources/Gabarito.glyphs` - Glyphs source file
- `sources/CustomFilter_GFLatinCore.plist` - Custom filter for glyph set
- `sources/config.yaml` - gftools-builder configuration

Config.yaml contents:
```yaml
sources:
  - Gabarito.glyphs
axisOrder:
  - wght
familyName: Gabarito
stat:
  Gabarito[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Regular
      value: 400
      linkedValue: 700
      flags: 2
    - name: Medium
      value: 500
    - name: SemiBold
      value: 600
    - name: Bold
      value: 700
    - name: ExtraBold
      value: 800
    - name: Black
      value: 900
buildOTF: false
autohintTTF: false
```

No local override config.yaml exists in google/fonts.

## Conclusion

The source block in METADATA.pb is complete and correct. All fields (repository_url, commit, files, branch, config_yaml) are properly set. No changes are needed.

### Recommended METADATA.pb Source Block

No changes required. The existing source block is correct:

```
source {
  repository_url: "https://github.com/naipefoundry/gabarito"
  commit: "1f3fb39d6449eefa880543f109f33ede0cd4064f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Gabarito[wght].ttf"
    dest_file: "Gabarito[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: HIGH
