# Investigation Report: Gidugu

## Summary

Gidugu is a Telugu sans-serif typeface designed by Purushoth Kumar Guttula, originally added to Google Fonts on 2014-12-10. The font was significantly updated on 2025-05-08 by Simon Cozens, with the upstream repository migrated from `appajid/gidugu` to `googlefonts/gidugu`. The METADATA.pb source block is complete and accurate, reflecting the latest rebuild at commit `834c5de`.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gidugu                                                             |
| Designer          | Purushoth Kumar Guttula                                            |
| Repository URL    | https://github.com/googlefonts/gidugu                              |
| Commit Hash       | 834c5de1862debc558e536377bc3ebc1c35bf958                           |
| Branch            | main                                                               |
| Config Path       | sources/config.yaml                                                |
| Source Format     | .ufo (sources/Gidugu-Regular.ufo)                                  |
| Status            | **complete**                                                       |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The existing source block in `ofl/gidugu/METADATA.pb` contains:
- `repository_url`: https://github.com/googlefonts/gidugu
- `commit`: 834c5de1862debc558e536377bc3ebc1c35bf958
- `config_yaml`: sources/config.yaml
- `branch`: main
- File mappings for Gidugu-Regular.ttf and OFL.txt

### Google Fonts Git History

The font has a rich history in google/fonts:

1. **Original onboarding** (commit `90abd17b4`, initial commit) -- added as part of the early Google Fonts library.
2. **Version 2.000 update** (commit `e5930c738`, 2025-05-08) by Simon Cozens:
   > Gidugu: Version 2.000; ttfautohint (v1.8.4.7-5d5b) added
   >
   > Taken from the upstream repo https://www.github.com/googlefonts/gidugu at commit https://www.github.com/googlefonts/gidugu/commit/368be453c9ff3a999f47fb961dce0019d12a4b17.

3. **URL fix** (commit `ba45d2341`, 2025-05-08) by Simon Cozens -- changed `www.github.com` to `github.com` in the repository URL.
4. **Rebuild** (commit `a83ea3e02`, 2025-05-20) by Simon Cozens -- updated the font binary (corresponding to upstream commits with shaping fixes and missing outlines).
5. **Sources info update** (commit `22b6a779e`, 2025-10-24) by Felipe Sanches -- updated the commit hash from `368be45` to `834c5de` and added `config_yaml` field.

### Commit Hash Analysis

The gftools-packager message referenced commit `368be453c9ff3a999f47fb961dce0019d12a4b17` ("Add built font", 2025-05-08). However, after that initial onboarding, Simon Cozens made additional upstream changes:

- `74d87ae` (2025-05-08) - "Update built file" (updated the TTF binary)
- `7e6aa89` (2025-05-20) - "Update project template"
- `f91e5a2` (2025-05-20) - "Shaping fixes, missing outlines" (source modifications to the UFO)
- `834c5de` (2025-05-20) - "Rebuild" (rebuilt the TTF from the fixed sources)

The google/fonts "Rebuild" commit (`a83ea3e02`, 2025-05-20) updated the font binary to match the upstream `834c5de` rebuild. The font binary size at `368be45` was 456,184 bytes, which matched the initial onboarding. The binary at `834c5de` is 460,988 bytes, matching the "Rebuild" commit in google/fonts.

Felipe Sanches subsequently updated METADATA.pb (commit `22b6a779e`, PR #9426) to point to the correct current commit `834c5de` and added the `config_yaml` field.

### Upstream Repository Verification

The upstream repo at `googlefonts/gidugu` (cached at `fontc_crater_cache/googlefonts/gidugu/`) has 17 commits on the main branch. The repository was previously at `appajid/gidugu` before being migrated to the googlefonts organization.

HEAD is at `a8b7f63` (a Dependabot bump), but the most recent source-relevant commit is `834c5de` ("Rebuild", 2025-05-20).

### Source Files and Config

The repository contains:
- `sources/Gidugu-Regular.ufo/` -- UFO source file
- `sources/config.yaml` -- gftools-builder configuration

The config.yaml content:
```yaml
sources:
  - Gidugu-Regular.ufo
familyName: "Gidugu"
buildVariable: false
buildOTF: false
buildWebfont: false
```

The `config.yaml` exists at both the referenced commit (`834c5de`) and at `368be45`, with identical content.

### No Override Config

There is no override `config.yaml` in the google/fonts family directory (`ofl/gidugu/`). The upstream config is used directly.

## Conclusion

The METADATA.pb source block for Gidugu is complete and accurate. The commit hash `834c5de` correctly points to the rebuild that matches the current font binary in google/fonts. No corrections are needed.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/gidugu"
  commit: "834c5de1862debc558e536377bc3ebc1c35bf958"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/ttf/Gidugu-Regular.ttf"
    dest_file: "Gidugu-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

**Status: complete** -- All source metadata is correct and verified.
