# Investigation Report: Grenze Gotisch

## Summary

Grenze Gotisch is a variable weight display serif font designed by Omnibus-Type. It was initially onboarded to Google Fonts in May 2020 from commit `772ce08` of the upstream repo, then rebuilt from the "Upstream Font Repository" (UFR) structure in August 2021 (PR #3637). The current METADATA.pb source block references commit `7b5eac1`, which is the HEAD (and only commit visible in the shallow cache) of the upstream repo. This commit was authored by Aaron Bell on 2021-08-03, two days before the UFR rebuild was merged into google/fonts on 2021-08-05. The upstream repo has a `sources/config.yaml` and a `.glyphs` source file. The variable font file size matches exactly between the upstream repo at commit `7b5eac1` (193,492 bytes) and the rebuilt font in google/fonts.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Grenze Gotisch                                                     |
| Repository URL    | https://github.com/Omnibus-Type/Grenze-Gotisch                    |
| Commit (original) | `772ce083e0a8481c40f4203770fb9eb9e292e080` (v1.001 onboarding)     |
| Commit (current)  | `7b5eac166bc3b2a519f98b5c124cb7a11670cc7b` (UFR rebuild, HEAD)    |
| Config YAML       | `sources/config.yaml`                                              |
| Source File       | `sources/GrenzeGotisch.glyphs`                                     |
| Status            | complete                                                           |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb already contains a complete source block:
```
source {
  repository_url: "https://github.com/Omnibus-Type/Grenze-Gotisch"
  commit: "7b5eac166bc3b2a519f98b5c124cb7a11670cc7b"
  config_yaml: "sources/config.yaml"
}
```

### Onboarding History in google/fonts

1. **Initial onboarding** (commit `42ed30b4f`, 2020-05-20): "grenzegotisch: v1.001 added. (#2467)" by Marc Foley. The commit message explicitly states the font was taken from upstream commit `772ce083e0a8481c40f4203770fb9eb9e292e080`.

2. **Description update** (commit `b86111664`, 2020-06-10): Updated the DESCRIPTION.en_us.html.

3. **UFR rebuild** (commit `98931f43a`, 2021-08-05): "Updating to UFR, fonts rebuilt (#3637)" by Aaron Bell. The fonts were rebuilt, with the variable font changing from 188,044 to 193,492 bytes.

4. **Static fonts removal** (commit `70b0fc8a8`, 2021-08-16): Static fonts removed for unhinted variable font families (#3695).

5. **Source block added** (commit `2423d2aef`, 2023-12-14): Simon Cozens added the initial source block with just the repository_url.

6. **Commit and config added** (commit `19cdcec59`, 2025-03-31): Batch update ported commit hash and config_yaml from fontc_crater targets list.

### Upstream Repository Verification

The cached repo at `fontc_crater_cache/Omnibus-Type/Grenze-Gotisch` is a shallow clone with only one commit:
- **Commit `7b5eac1`** (2021-08-03): "Delete GrenzeGotisch[wght].ttf" by Aaron Bell. Despite the misleading commit message, this is actually the commit that restructured the repo into UFR format, adding build infrastructure, config.yaml, and the .glyphs source file.

The original onboarding commit `772ce08` is not available in the shallow clone.

### Commit Hash Verification

The METADATA.pb commit `7b5eac1` corresponds to the UFR rebuild phase. Evidence:
- The upstream commit date (2021-08-03) is 2 days before the google/fonts merge (2021-08-05)
- The font file sizes match exactly: 193,492 bytes in both upstream `fonts/variable/` and google/fonts after the rebuild
- The commit was authored by Aaron Bell, who also submitted PR #3637

This is the correct commit for the current state of fonts in google/fonts, as the original onboarding commit `772ce08` corresponds to v1.001 which was superseded by the UFR rebuild.

### Config and Source Files

At commit `7b5eac1`, the upstream repo contains:
- `sources/config.yaml` -- gftools-builder configuration referencing `GrenzeGotisch.glyphs`
- `sources/GrenzeGotisch.glyphs` -- Glyphs source file (100,231 lines)

The config.yaml defines:
- Source: `GrenzeGotisch.glyphs`
- Family name: "Grenze Gotisch"
- Axis order: wght
- STAT table entries for weight axis (Thin through Black)

## Conclusion

The METADATA.pb source block is already complete and correct. The commit hash `7b5eac1` references the latest upstream commit which corresponds to the UFR rebuild used in PR #3637. The config.yaml path `sources/config.yaml` correctly points to the gftools-builder configuration in the upstream repo.

### Recommended METADATA.pb source block

No changes needed. The current source block is correct:

```
source {
  repository_url: "https://github.com/Omnibus-Type/Grenze-Gotisch"
  commit: "7b5eac166bc3b2a519f98b5c124cb7a11670cc7b"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: HIGH
