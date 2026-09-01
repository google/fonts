# Bevan - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bevan |
| Repository URL | https://github.com/googlefonts/BevanFont |
| Commit Hash | ab1035d7823b4c53400a6007ee077ecc9324c3e5 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/BevanFont` is documented in the METADATA.pb `source{}` block. It was added by commit `f7455d788` ("Populate source.repository_url") and confirmed by the copyright field in the font metadata: "Copyright 2016 The Bevan Project Authors (https://github.com/googlefonts/BevanFont)". PR #4105 also explicitly references this URL.

## How the Commit Hash Was Determined

The commit hash `ab1035d7823b4c53400a6007ee077ecc9324c3e5` was identified through PR #4105, which updated Bevan to Version 2.100. The PR body (by emmamarichal) states: "Bevan Version 2.100; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/BevanFont at commit https://github.com/googlefonts/BevanFont/commit/ab1035d7823b4c53400a6007ee077ecc9324c3e5."

The google/fonts commit `160c7fe82` (2021-12-08) is the last commit that modified the .ttf files, and its message confirms the same commit hash. This commit added the Italic variant and updated the Regular.

The commit hash was also ported into the METADATA.pb in the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

The upstream commit `ab1035d` is: "Merge pull request #43 from emmamarichal/main".

### Font version history in google/fonts:
1. `90abd17b4` (2015-03-07) - Initial commit (original Bevan Regular)
2. `dd2f45e45` - bevan: v2.000 added (#448)
3. `160c7fe82` (2021-12-08) - Bevan: Version 2.100; added Italic (#4105) - **last TTF modification**

## Config YAML Status

The upstream repository has `sources/config.yaml` at the recorded commit `ab1035d`. Verified locally:

```yaml
sources:
  - Bevan.glyphs
  - Bevan-Italic.glyphs
buildVariable: False
# buildWebfont: False
# buildOTF: False
```

The `config_yaml: "sources/config.yaml"` field is present in the current METADATA.pb on google/fonts main branch. No override config.yaml is needed or present in the google/fonts family directory.

## Verification

- **Repository exists**: Yes, confirmed locally at `upstream_repos/fontc_crater_cache/googlefonts/BevanFont`
- **Commit hash exists**: Yes, verified: `ab1035d Merge pull request #43 from emmamarichal/main`
- **Config.yaml exists at recorded commit**: Yes, at `sources/config.yaml`
- **Source files at commit**: `sources/Bevan.glyphs`, `sources/Bevan-Italic.glyphs`, `sources/config.yaml`
- **PR confirmed**: PR #4105 by emmamarichal confirms the commit hash

## Confidence Level

**High** - The commit hash is confirmed by multiple sources: the gftools-packager commit message, PR #4105 body, and the fontc_crater targets list. The upstream commit exists and contains the expected source files and config.yaml. All metadata fields are complete.

## Open Questions

None. This family is fully documented with repository URL, commit hash, and config.yaml path all verified.
