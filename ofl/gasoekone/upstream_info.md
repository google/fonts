# Investigation Report: Gasoek One

## Summary

Gasoek One is a Korean display sans-serif font by Jiashuo Zhang and JAMO, added to Google Fonts on May 18, 2023. The upstream repo at `https://github.com/JAMO-TYPEFACE/Gasoek` has a single merge commit (`f6b875c`) which represents the complete project including the fixed binary with a missing glyph added. The METADATA.pb source block is complete and correct.

## Key Findings

| Field             | Value                                                         |
|-------------------|---------------------------------------------------------------|
| Family Name       | Gasoek One                                                    |
| Repository URL    | https://github.com/JAMO-TYPEFACE/Gasoek                      |
| Commit Hash       | f6b875c95ad933c5f937c2494ae2337f5aef2694                      |
| Config YAML       | Sources/config.yaml                                           |
| Status            | **complete**                                                  |
| Confidence        | **HIGH**                                                      |

## Investigation Details

### Onboarding History

The font was initially onboarded via commit `a6631f1a0` on May 18, 2023, authored by Aaron Bell (aaron@sajatypeworks.com). The commit message states:

> Gasoek One Version 1.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.28] taken from the upstream repo https://github.com/JAMO-TYPEFACE/Gasoek at commit https://github.com/JAMO-TYPEFACE/Gasoek/commit/f3beadd65b93b5f43e9381a546d065253d6e655a.

The referenced commit `f3beadd` no longer exists in the upstream repository.

Six days later, on May 24, 2023, Aaron Bell updated the binary (commit `19ac170fa`) with the message "Adding missing glyph from GF Kernal". This updated the font from 1,061,228 bytes to 1,061,372 bytes.

### Post-Onboarding Updates in google/fonts

1. **Initial onboarding** (a6631f1a0, May 18, 2023): Added font with upstream.yaml referencing commit `f3beadd`.
2. **Primary script** (95ce8995c): Added `primary_script: "Kore"`.
3. **Author correction** (a1172a57c): Added JAMO as author, corrected description.
4. **Binary update** (19ac170fa, May 24, 2023): Updated `GasoekOne-Regular.ttf` to fix missing glyph from GF Kernal.
5. **URL fix** (77e9ffa25): Removed https from displayed URL.
6. **Stroke/classification** (1db714082): Added stroke and classification metadata.
7. **upstream.yaml merge** (66f91f10f, April 3, 2024): Merged upstream.yaml into METADATA.pb source block.
8. **fontc_crater batch** (19cdcec59, March 31, 2025): Updated commit hash from `f3beadd` to `f6b875c` and added `config_yaml: "sources/config.yaml"` (lowercase).
9. **Sources casing fix** (7190093b1, May 22, 2025): Corrected `config_yaml` from `sources/config.yaml` to `Sources/config.yaml` to match the actual directory name in the upstream repo.

### Upstream Repository Analysis

- **URL**: https://github.com/JAMO-TYPEFACE/Gasoek
- **Remote verified**: Yes, `git fetch` succeeds
- **Repo status**: Clean, on branch `main`, up to date
- **Total commits**: 1 (merge commit `f6b875c`, "Merge pull request #3 from aaronbell/main", May 24, 2023)

The upstream repo appears to have been force-pushed/squashed, leaving only the single merge commit that incorporates Aaron Bell's fix for the missing GF Kernal glyph. This merge commit (PR #3 in the upstream repo) contains:
- Source file: `Sources/Gasoek.glyphs`
- Build config: `Sources/config.yaml`
- Compiled binary: `Fonts/ttf/GasoekOne-Regular.ttf`
- Documentation images and metadata files

### Binary Verification

The compiled font in the upstream repo at `f6b875c` is identical to the one in google/fonts:

| File                     | Size (bytes) | SHA256 Match |
|--------------------------|-------------|--------------|
| GasoekOne-Regular.ttf    | 1,061,372   | Yes          |

Note: The current binary (1,061,372 bytes) matches the post-update version, not the original onboarding version (1,061,228 bytes). This is correct because the upstream merge commit `f6b875c` includes the glyph fix that was applied on the same day (May 24, 2023).

### Config YAML

The upstream repo has `Sources/config.yaml` (note the capital "S" in Sources) with:
```yaml
sources:
  - Gasoek.glyphs
familyName: "Gasoek One"
buildOTF: false
```

No override config.yaml exists in the google/fonts family directory.

### Note on Commit Hash and Repository History

The original onboarding referenced commit `f3beadd` which no longer exists in the upstream repo. The repo was likely force-pushed, and only the merge commit `f6b875c` (which merges aaronbell's fix for the missing GF Kernal glyph) survives. Since this commit produces a binary-identical font to what is currently in google/fonts, and it is the only commit available, `f6b875c` is the correct reference.

## Conclusion

The METADATA.pb source block is **complete and correct**. No changes needed.

### Current METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/JAMO-TYPEFACE/Gasoek"
  commit: "f6b875c95ad933c5f937c2494ae2337f5aef2694"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/ttf/GasoekOne-Regular.ttf"
    dest_file: "GasoekOne-Regular.ttf"
  }
  branch: "main"
  config_yaml: "Sources/config.yaml"
}
```
