# Bagel Fat One

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete
- **Designer**: Kyungwon Kim, JAMO
- **Primary Script**: Korean (Kore)

## Source Data

| Field            | Value                                                      |
|------------------|------------------------------------------------------------|
| Repository URL   | https://github.com/JAMO-TYPEFACE/BagelFat                  |
| Commit           | `d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b`                 |
| Config YAML      | `Sources/config.yaml` (in upstream repo)                   |
| Branch           | `main`                                                     |
| Date Added       | 2023-05-18                                                 |

## Repository URL Verification

The repository URL `https://github.com/JAMO-TYPEFACE/BagelFat` was confirmed valid. The cached clone at `JAMO-TYPEFACE/BagelFat` had its remote set to the same URL. The copyright string in METADATA.pb also referenced this repository. Issue google/fonts#6089, filed by Chris Simpkins, requested onboarding of this font from the same URL.

## Commit Verification

### Onboarding History

The font was onboarded via PR google/fonts#6272, authored by Aaron Bell (@aaronbell) and merged on 2023-05-25.

The initial commit (`d9406e5`, 2023-05-18) was created by gftools-packager and referenced upstream commit `5ff1333d3384611f499419a844e2b3006dc7cacd`. However, during the PR review process, Aaron Bell pushed a second commit (`4202185`, 2023-05-24) with the message "Update BagelFatOne-Regular.ttf / Adding missing glyph from GF Kernal". On the same day, the upstream repository received commit `d8dd4e8` ("Merge pull request #3 from aaronbell/main") which incorporated that same fix.

### Commit `d8dd4e8` Analysis

The commit `d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b` was the latest (and only visible) commit on the `main` branch of the upstream repo. It was dated 2023-05-24, one day before the PR was merged. The upstream repo had only this single commit visible in the shallow clone. The SHA-256 hash of `Fonts/ttf/BagelFatOne-Regular.ttf` in the upstream repo matched exactly with the current binary in google/fonts (`9286944032c5a9b20ad70940105417beae14013e0b4f5fc292425afdc4330245`), confirming that commit `d8dd4e8` was the correct final source for the binary currently in the Google Fonts catalog.

### Timeline

1. **2023-05-18**: Initial onboarding commit in google/fonts from upstream commit `5ff1333d` (PR #6272 opened)
2. **2023-05-24 09:58**: Upstream commit `d8dd4e8` merged (PR #3 in upstream, adding missing glyph)
3. **2023-05-24 10:00**: Updated binary pushed to google/fonts PR #6272 (commit `4202185`)
4. **2023-05-25**: PR #6272 merged into google/fonts

The METADATA.pb correctly references `d8dd4e8`, which was the final upstream commit that produced the binary shipped in Google Fonts.

## Config YAML Verification

The upstream repository contained `Sources/config.yaml` at commit `d8dd4e8` with the following content:

```yaml
sources:
  - BagelFat.glyphs
familyName: "Bagel Fat One"
buildOTF: false
```

This was a valid gftools-builder configuration referencing the Glyphs source file `Sources/BagelFat.glyphs` (6.8 MB). The METADATA.pb `config_yaml` field was set to `Sources/config.yaml`, which correctly pointed to this file. No override config.yaml was needed since the upstream repo already had one.

## Conclusion

All source metadata for Bagel Fat One was complete and correct. The repository URL, commit hash, and config.yaml path in METADATA.pb all matched the upstream repository state. The commit `d8dd4e8` was verified as the correct reference -- it was the final upstream commit before the google/fonts PR was merged, and the binary files matched exactly. No changes were required.
