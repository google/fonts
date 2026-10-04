# Investigation Report: Bokor

## Summary

Bokor is a Khmer display typeface by Danh Hong, originally added to Google Fonts on 2011-03-02. It has undergone several updates, most recently to version 8.001/8.002 in late 2021. The font is a static (non-variable) build from a Glyphs source file.

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bokor |
| Designer | Danh Hong |
| Repository URL | https://github.com/danhhong/Bokor |
| Commit Hash | `b5d5f6e07e365610ad5a39d42f87505e85702432` |
| Branch | master |
| Config YAML | `Source/builder.yaml` |
| License | OFL |
| Date Added | 2011-03-02 |

## How URL Found

The repository URL `https://github.com/danhhong/Bokor` is stated in:
- The gftools-packager commit message for the v8.001 update
- The copyright string in METADATA.pb
- PR #4019 in google/fonts

## How Commit Determined

The commit hash `b5d5f6e07e365610ad5a39d42f87505e85702432` is recorded in the gftools-packager commit message for the v8.001 update (google/fonts commit `bb6f43532`, PR #4019):

> [gftools-packager] Bokor: Version 8.001; ttfautohint (v1.8.3) added
> Bokor Version 8.001; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/danhhong/Bokor.git at commit b5d5f6e07e365610ad5a39d42f87505e85702432.

PR #4019 was authored by Yanone (post@yanone.de), and the same commit hash is confirmed in the PR body.

### Post-Onboarding Update

After the v8.001 onboarding, a batch hotfix (v8.002) was applied in google/fonts commit `4f5dbdb58` (2021-12-07) by Yanone to fix "urgent glyph definition issues" across multiple Khmer fonts. This update modified the binary font file but was not sourced from a new upstream commit -- it was a batch fix applied directly.

## Config YAML Status

The config file at `Source/builder.yaml` exists at the recorded commit and contains:
```yaml
sources:
  - Bokor.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

This is a valid gftools-builder configuration for a static-only font build.

## Verification

- **Commit exists in upstream**: Yes, verified. `b5d5f6e` is the HEAD of the master branch. It is a merge commit: "Merge pull request #2 from yanone/master".
- **Config.yaml exists at commit**: Yes, `Source/builder.yaml` is present and valid.
- **Source files match METADATA.pb**: The METADATA.pb references `Release/ttf/Bokor-Regular.ttf` as the source file, which is consistent with the `outputDir: "../Release"` in the builder config.
- **Branch correct**: master, confirmed (only branch in the repo).
- **Upstream repo cached**: Yes, at `upstream_repos/fontc_crater_cache/danhhong/Bokor`.
- **Upstream repo is HEAD of commit**: The recorded commit is the latest commit in the repository.

## Confidence Level

**HIGH** -- The commit hash is directly stated in the gftools-packager commit message and confirmed in PR #4019. The upstream repo verifies the commit exists at HEAD. The config.yaml is present and valid. Note that the binary in google/fonts was subsequently patched (v8.002 hotfix) without a corresponding upstream commit.

## Open Questions

None. This family's source documentation is complete and verified. The v8.002 hotfix was a downstream-only binary patch and does not affect the upstream source reference.
