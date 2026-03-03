# Investigation Report: Lexend Zetta

**Family Name**: Lexend Zetta
**Directory**: `ofl/lexendzetta`
**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Confidence**: HIGH

## Summary

Lexend Zetta is one of eight sub-families in the Lexend superfamily (Lexend, Lexend Deca, Lexend Exa, Lexend Giga, Lexend Mega, Lexend Peta, Lexend Tera, Lexend Zetta). All share the same upstream repository and the same source file (`sources/Lexend.glyphs`), differentiated by per-family config YAML files that set different `familyName` values.

The METADATA.pb source block was already complete with repository URL, commit hash, config path, file mappings, and branch. All fields were verified as correct.

## Upstream Repository

- **URL**: https://github.com/googlefonts/lexend
- **Local cache**: `upstream_repos/fontc_crater_cache/googlefonts/lexend`
- **Remote verified**: Yes (origin points to `https://github.com/googlefonts/lexend`)
- **Branch**: `main`

## Source Block in METADATA.pb

The existing source block contained:

```
source {
  repository_url: "https://github.com/googlefonts/lexend"
  commit: "20491885ca2cf7ffc556432973e7bdbc701952b5"
  config_yaml: "sources/zetta.yaml"
  files {
    source_file: "fonts/zetta/variable/LexendZetta[wght].ttf"
    dest_file: "LexendZetta[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

## Commit Hash Verification

- **Referenced commit**: `20491885ca2cf7ffc556432973e7bdbc701952b5`
- **Commit message**: "Merge pull request #2 from RosaWagner/main" (re-added forgotten parenthesis in copyright string)
- **Commit date**: 2021-07-30 18:27:32 +0200
- **Author**: Rosalie Wagner

### Cross-verification

1. **gftools-packager message**: The google/fonts commit `beda156f5` (PR #3623) explicitly stated: "Lexend Zetta Version 1.007 taken from the upstream repo https://github.com/googlefonts/lexend at commit https://github.com/googlefonts/lexend/commit/20491885ca2cf7ffc556432973e7bdbc701952b5."

2. **Timeline coherence**: The upstream commit was made at 18:27:32 +0200 and the google/fonts PR #3623 was merged at 18:36:51 +0200 on the same day (2021-07-30), just 9 minutes later. The commit was the HEAD of the upstream `main` branch at that time.

3. **Binary file comparison**: The variable font `LexendZetta[wght].ttf` extracted from the upstream commit matched the file in google/fonts exactly (MD5: `3dfbd1c4ad3bd01668dd72c039bf161e`).

4. **No intervening commits**: No additional upstream commits were made between `2049188` and the google/fonts merge.

**Conclusion**: The commit hash is verified as correct with high confidence.

## Config YAML Verification

- **Path**: `sources/zetta.yaml`
- **Exists at referenced commit**: Yes
- **Content verified**: The config references `Lexend.glyphs` as the source, sets `familyName: "Lexend Zetta"`, outputs to `../fonts/zetta`, and includes proper STAT table definitions for the `wght` axis (100-900).
- **Override config.yaml in google/fonts**: Not present (not needed -- upstream has the config)

## Font File History in google/fonts

The Lexend Zetta binary was last updated in PR #3623 (commit `beda156f5`, 2021-07-30) which brought all eight Lexend families to Version 1.007. Prior updates included:

- PR #3517 (`da0650b86`): Version 1.100 added (variable fonts introduced)
- PR #3345 (`f893bb335`): Version 1.005 with ttfautohint
- PR #2789 (`29b338579`): Version 1.002 bug fix

The source block was added later in commit `11e18675f` (2025-04-02) by Felipe Sanches, which added commit hash and config_yaml fields to all eight Lexend families simultaneously.

## Upstream Repository State

The upstream repo has had additional development since the referenced commit (CI configs, HEXP axis work, README updates), but these changes have not been pulled into google/fonts. The current HEAD of `main` is `7894f02` (2023-03-02). Any newer work would require separate review before updating the catalog.

## Conclusion

The METADATA.pb source block for Lexend Zetta was already complete and fully verified. The repository URL, commit hash, config_yaml path, file mappings, and branch are all correct. No changes are needed.
