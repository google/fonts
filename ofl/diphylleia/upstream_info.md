# Diphylleia

## Summary

| Field | Value |
|---|---|
| **Family name** | Diphylleia |
| **Designer** | Minha Hyung, JAMO |
| **License** | OFL |
| **Date added** | 2023-05-18 |
| **Repository URL** | https://github.com/JAMO-TYPEFACE/Diphylleia |
| **Commit** | `6a20531aa22286238d89f3bc1d8c29694acaec53` |
| **Branch** | main |
| **Config YAML** | `Sources/config.yaml` |
| **Status** | complete |

## Upstream Repository

The upstream repo at `JAMO-TYPEFACE/Diphylleia` contains:
- `Sources/Diphylleia.glyphs` - Glyphs source file
- `Sources/config.yaml` - gftools-builder configuration
- `Fonts/ttf/Diphylleia-Regular.ttf` - Pre-built TTF
- Standard Google Fonts project structure (AUTHORS.txt, CONTRIBUTORS.txt, etc.)

The repo has a single commit (`6a20531`), indicating the repo was likely reset/force-pushed at some point.

## Commit Verification

The original onboarding used commit `d481ed1f2dc17d2457f9788351a1d4e886cdc221`, as recorded in the gftools-packager commit `c39470536` in google/fonts (by Aaron Bell, 2023-05-18). That commit message states: "taken from the upstream repo https://github.com/JAMO-TYPEFACE/Diphylleia at commit d481ed1f2dc17d2457f9788351a1d4e886cdc221".

However, the upstream repo was subsequently reset to a single commit (`6a20531`, "Delete Diphylleia-Regular.otf", 2024-12-27). The original commit `d481ed1` no longer exists in the repo history.

The METADATA.pb was updated from `d481ed1` to `6a20531` in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported data from fontc_crater's targets.json file.

A subsequent update to the TTF was made in google/fonts commit `469bc2664` ("Update Diphylleia-Regular.ttf - Adding missing glyph from GF Kernal", by Aaron Bell, 2023-05-24), without a corresponding upstream commit.

## Config YAML

The config.yaml at `Sources/config.yaml` contains:
```yaml
sources:
  - Diphylleia.glyphs
familyName: "Diphylleia"
buildOTF: false
```

Note the capital "S" in `Sources/` - this was corrected in commit `7190093b1` in google/fonts.

## Conclusion

- Repository URL: Verified correct
- Commit hash: `6a20531` is the only commit in the repo (original `d481ed1` was lost to repo reset)
- Config YAML: Verified at `Sources/config.yaml`
- Status: `complete` - all fields populated and verified
- Note: The original onboarding commit is no longer in the repo history due to a force-push
