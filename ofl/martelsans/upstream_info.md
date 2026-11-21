# Martel Sans — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The current METADATA.pb at `ofl/martelsans/METADATA.pb` contains the following source block:

```
source {
  repository_url: "https://github.com/typeoff/martel_sans"
  commit: "7a536b7ce5f6059665d45bfff7c24bee414c1fd1"
}
primary_script: "Deva"
```

Note: The `config_yaml` field is not set in the source block. An override `config.yaml` exists in the google/fonts family directory (auto-detected by google-fonts-sources).

## Repository Analysis

**Repository**: https://github.com/typeoff/martel_sans
**Owner**: typeoff (Dan Reynolds)
**Default branch**: master
**Last pushed**: 2015-06-09 (repository has been inactive since 2015)
**Status**: Valid and accessible

### Repository Structure

```
LICENSE.md
README.md
Martel Sans Font Files/
  OTFs/
    MartelSans-{Bold,DemiBold,ExtraBold,Heavy,Light,Regular,UltraLight}.otf
  TTFs with ttautohints/
    MartelSans-{Bold,DemiBold,ExtraBold,Heavy,Light,Regular,UltraLight}.ttf
  TTFs without ttfautohints/
    MartelSans-{Bold,DemiBold,ExtraBold,Heavy,Light,Regular,UltraLight}.ttf
Martel Sans Source Files/
  Martel_Sans_20150305.glyphs
  Martel Sans-Bold.ufo/
  Martel Sans-Light.ufo/
```

### Source Files

The primary source file is `Martel Sans Source Files/Martel_Sans_20150305.glyphs`, a Glyphs format file. Two UFO masters (Bold and Light) were also present. The .glyphs file contained version information `versionMajor = 1`, `versionMinor = 1` (v1.001). The copyright was set to 2015 for both Dan Reynolds and Mathieu Reguer.

### No config.yaml in Upstream

The upstream repository contained no `config.yaml` file. The sources were gftools-builder compatible (.glyphs format), so an override config.yaml was created in the google/fonts family directory.

### Commit History

The upstream repository had 13 total commits, all from 2014-2015:

| Hash | Date | Description |
|------|------|-------------|
| `7a536b7` | 2015-04-14 | Update README.md (HEAD) |
| `e963010` | 2015-04-14 | Improved ReadMe text |
| `1f7e5eb` | 2015-04-14 | Update README.md |
| `9577cf5` | 2015-04-14 | Merge pull request #4 from davelab6/master |
| `db73bf6` | 2015-04-10 | Update README.md |
| `bebd443` | 2015-04-10 | Update LICENSE |
| `45b74e4` | 2015-03-05 | License and ReadMe update |
| `3e1885f` | 2015-03-05 | Martel Sans Version 1.001 |
| `69ba000` | 2015-03-02 | ReadMe update |
| `bad1ea0` | 2015-02-28 | ReadMe update |
| `5de9388` | 2015-02-24 | Initial release |
| `eb05719` | 2015-02-19 | Beta upload of OTF files |
| `239e3f8` | 2014-10-05 | Initial set-up |

The last commit that modified source files was `3e1885f` (2015-03-05, "Martel Sans Version 1.001"). All subsequent commits (up to HEAD at `7a536b7`) were README and license text updates only.

## Onboarding History

### Initial Onboarding (2015-03-07)

Martel Sans was initially added to Google Fonts in commit `90abd17` on 2015-03-07 by Dave Crossland as part of an "Initial commit" batch. This was just two days after the v1.001 sources were committed upstream. The initial onboarding included 7 TTF weights plus METADATA.json, DESCRIPTION, and OFL.txt.

### v1.002 Update — PR #905 (2017-05-08)

PR #905 titled "hotfix-martelsans: v1.002 added" was authored by Marc Foley and merged by Dave Crossland on 2017-05-08. The PR body was empty (no description).

The commit `e35667db` updated all 7 TTF files and made copyright string corrections in METADATA.pb (changing "Reguer" to "Rguer" — both likely OCR/encoding artifacts of "Reguer"). The version went from 1.001 to 1.002.

Key observation: The upstream repository only contained v1.001 sources and binaries. The v1.002 binaries in google/fonts had different file sizes from the upstream v1.001 TTFs and used different weight naming conventions:
- Google Fonts: ExtraLight, SemiBold, Black
- Upstream: UltraLight, DemiBold, Heavy

This indicates the v1.002 binaries were recompiled from the same `.glyphs` source but with modifications (version bump, weight renaming, possibly hinting adjustments) done as part of Marc Foley's hotfix process, without pushing changes back upstream.

### Source Block Addition (2024-03-04)

Simon Cozens added the `repository_url` field in commit `c891a9b` ("Update upstreams") on 2024-03-04, along with the `primary_script: "Deva"` field.

### Commit Hash and Config Addition (2025-10-30)

Felipe Sanches added the `commit` hash (`7a536b7`) and created the override `config.yaml` in commit `53a16a0` on 2025-10-30. The commit message noted: "PR #905 mentions 'hotfixing', but it is unclear what (if anything) was manually changed in the binaries after they were built from sources."

## Build Configuration

### Override config.yaml (in google/fonts)

An override `config.yaml` exists in `ofl/martelsans/config.yaml` with the following content:

```yaml
buildVariable: false
sources:
  - Martel Sans Source Files/Martel_Sans_20150305.glyphs
```

This configuration correctly references the .glyphs source file path relative to the upstream repository root at the referenced commit. The `buildVariable: false` flag is appropriate as this is a static (non-variable) font family.

The `config_yaml` field is omitted from METADATA.pb, which is correct behavior — google-fonts-sources auto-detects the local override config.

## Findings

1. **Repository URL**: Correct. `https://github.com/typeoff/martel_sans` is valid and accessible, owned by typeoff (Dan Reynolds).

2. **Commit hash**: The referenced commit `7a536b7` is HEAD of the master branch. It is a README-only update from 2015-04-14. The last source-modifying commit was `3e1885f` (2015-03-05, "Martel Sans Version 1.001"). Since both commits contain the same source files and the repo has been completely inactive since 2015, using HEAD is acceptable — it ensures all upstream content is captured. However, `3e1885f` would be a more precise reference for source provenance.

3. **Version mismatch**: The upstream sources are v1.001 while google/fonts has v1.002 binaries. The v1.002 update was a "hotfix" by Marc Foley (PR #905, 2017-05-08) that appears to have involved recompiling from the same .glyphs source with version bumps, weight renaming, and possibly other modifications, without pushing changes back upstream.

4. **Override config.yaml**: Correctly set up. The .glyphs source path matches the actual file in the upstream repo at the referenced commit.

5. **Weight naming discrepancy**: The upstream repo used UltraLight/DemiBold/Heavy while google/fonts uses ExtraLight/SemiBold/Black. This renaming was part of the v1.002 hotfix.

6. **Source block status**: Complete. All required fields are populated (repository_url, commit) and the override config.yaml is in place.

## Recommended Source Block

The current source block is acceptable:

```
source {
  repository_url: "https://github.com/typeoff/martel_sans"
  commit: "7a536b7ce5f6059665d45bfff7c24bee414c1fd1"
}
```

No `config_yaml` field is needed since the override `config.yaml` in the google/fonts family directory is auto-detected.

An alternative, more precise commit reference would be `3e1885f25cc1352264c442929b97148e96a6110a` (the last source-modifying commit), but since the repository has been inactive since 2015 and no source changes occurred after `3e1885f`, the current HEAD reference (`7a536b7`) is functionally equivalent and captures the complete state of the repository.

**Overall status**: Complete. No changes needed.
