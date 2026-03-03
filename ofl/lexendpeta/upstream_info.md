# Lexend Peta - Investigation Report

**Family Name**: Lexend Peta
**Directory Slug**: `lexendpeta`
**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete

---

## METADATA.pb Analysis

The METADATA.pb file at `ofl/lexendpeta/METADATA.pb` contained a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/lexend"
  commit: "20491885ca2cf7ffc556432973e7bdbc701952b5"
  config_yaml: "sources/peta.yaml"
  files {
    source_file: "fonts/peta/variable/LexendPeta[wght].ttf"
    dest_file: "LexendPeta[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

**Designer**: Bonnie Shaver-Troup, Thomas Jockin, Santiago Orozco, Hector Gomez, Superunion
**License**: OFL
**Date Added**: 2019-08-01
**Category**: Sans Serif
**Variable Axes**: wght (100-900)

## Upstream Repository

- **URL**: https://github.com/googlefonts/lexend
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/lexend/`
- **Remote verified**: origin points to `https://github.com/googlefonts/lexend`
- **Default branch**: main
- **Repo state**: Clean, HEAD detached at `2049188`

Lexend Peta is one of seven Lexend font families (Lexend, Lexend Deca, Lexend Exa, Lexend Giga, Lexend Mega, Lexend Peta, Lexend Tera, Lexend Zetta) that all share the same upstream repository. The copyright string in METADATA.pb confirmed this: "Copyright 2019 The Lexend Project Authors (https://github.com/googlefonts/lexend)".

## Source Files

At the referenced commit `2049188`:

- `sources/Lexend.glyphs` - Single Glyphs source file shared by all Lexend sub-families (Glyphs app version 3094)
- `sources/peta.yaml` - gftools-builder config specific to Lexend Peta
- `fonts/peta/variable/LexendPeta[wght].ttf` - Pre-built variable TTF binary

The `sources/peta.yaml` config contained:

```yaml
sources:
  - Lexend.glyphs
familyName: "Lexend Peta"
outputDir: ../fonts/peta
buildStatic: False
buildWebfont: False
axisOrder:
  - wght
stat:
  - name: Weight
    tag: wght
    values:
    - name: Thin
      value: 100
    - name: ExtraLight
      value: 200
    - name: Light
      value: 300
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
```

Each Lexend variant (Deca, Exa, Giga, Mega, Peta, Tera, Zetta) had its own `.yaml` config file that referenced the shared `Lexend.glyphs` source with a different `familyName` setting.

## Commit Hash Verification

The METADATA.pb referenced commit `20491885ca2cf7ffc556432973e7bdbc701952b5` with message "Merge pull request #2 from RosaWagner/main", dated 2021-07-30 18:27:32 +0200.

### gftools-packager Confirmation

The google/fonts commit `beda156f5` (PR #3623) explicitly stated in its body:

> Lexend Peta Version 1.007 taken from the upstream repo https://github.com/googlefonts/lexend at commit https://github.com/googlefonts/lexend/commit/20491885ca2cf7ffc556432973e7bdbc701952b5.

This gftools-packager message directly referenced the same commit hash for all seven Lexend families.

### Timeline Analysis

- **2021-07-30 13:48 - 15:26 +0200**: Upstream repo restructured: repository cleaned up, fonts version 1.007 generated, OFL.txt updated, copyright string fixed (commits `36a3978` through `2049188`)
- **2021-07-30 18:27 +0200**: Commit `2049188` created as "Merge pull request #2 from RosaWagner/main" -- this was the HEAD of main at the time
- **2021-07-30 18:36 +0200**: Google/fonts commit `beda156f5` merged via PR #3623, adding Version 1.007 of all eight Lexend families

The timestamps showed that the upstream commit and the google/fonts onboarding happened within 9 minutes of each other on the same day. The commit `2049188` was the latest commit on the upstream main branch at the time of onboarding. No additional upstream commits existed between the referenced commit and the google/fonts merge.

### Subsequent Upstream Activity

After the onboarding commit, the upstream repository received additional commits (CI configuration, HEXP axis build, web subfamilies removal, README updates) through 2023-03-02. These changes were not reflected in google/fonts and would require separate review if incorporation is desired.

## Override config.yaml

No override `config.yaml` existed in the google/fonts family directory. This was correct because the upstream repository already contained a proper gftools-builder config at `sources/peta.yaml`, which was referenced in the `config_yaml` field of METADATA.pb.

## History in google/fonts

Key commits affecting Lexend Peta in google/fonts:

1. `e9f7ace90` - "lexendpeta: v1.001 added" - Initial addition (2019-08-01)
2. `29b338579` - "Lexend: version 1.002 added (bug fix) (#2789)" - Bug fix update (2020-11-04)
3. `f893bb335` - "Lexend Peta: Version 1.005; ttfautohint (v1.8.3) added (#3345)" - v1.005 update (2021-04-28)
4. `da0650b86` - "Lexend Peta: Version 1.100 added (#3517)" - v1.100 update (2021-07-09)
5. `beda156f5` - "Lexend Peta: Version 1.007 added (#3623)" - v1.007 update, the current version (2021-07-30)
6. `66f91f10f` - "Merge upstream.yaml into METADATA.pb [skip ci]" - Source block with repository_url, files, and branch added (2024-04-03)
7. `11e18675f` - "sources info for Lexend (incl. Deca, Exa, Giga, Mega, Peta, Tera & Zetta)" - Commit hash and config_yaml added to source block (2025-04-02)

Note: The version number went from 1.100 back to 1.007 in the final update. This was because v1.100 was an intermediate release, and v1.007 was the result of a complete repository restructure by Rosa Wagner that produced the definitive font binaries from the new build configuration.

## Conclusion

The source block in METADATA.pb was complete with:
- **Repository URL**: `https://github.com/googlefonts/lexend` (verified, accessible, shared by all Lexend families)
- **Commit**: `20491885ca2cf7ffc556432973e7bdbc701952b5` (verified via gftools-packager message in PR #3623 and timeline analysis)
- **Config**: `sources/peta.yaml` in upstream repository (gftools-builder compatible, references shared Lexend.glyphs source)
- **Files mapping**: Correctly specified (`fonts/peta/variable/LexendPeta[wght].ttf` and `OFL.txt`)
- **Branch**: main (verified)
- **Status**: complete
- **Confidence**: HIGH

No further action was required for this family.
