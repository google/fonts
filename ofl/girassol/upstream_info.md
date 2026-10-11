# Investigation Report: Girassol

## Summary

Girassol is a display typeface by Liam Spradlin inspired by hand-painted street signs in Carcavelos, Portugal. It was onboarded to Google Fonts on 2019-12-05 via PR #2271, submitted by Yanone (Jan Gerner) and merged by Marc Foley. The upstream repository is `liamspradlin/Girassol-Display`. The referenced commit `cc8fa1b` is the HEAD of the master branch, and the binary font file matches exactly between google/fonts and the upstream repo. An override `config.yaml` already exists in google/fonts. The existing source metadata is complete.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Girassol |
| Designer          | Liam Spradlin |
| Repository URL    | https://github.com/liamspradlin/Girassol-Display |
| Commit Hash       | cc8fa1b5a1afc28520fdc0ccc36256db243d9dfa |
| Commit Date       | 2019-12-05 |
| Commit Description| Merge pull request #8 from yanone/master |
| Config YAML       | Override config.yaml in google/fonts |
| Source File       | sources/Girassol-Regular.ufo |
| Branch            | master |
| Status            | **complete** |
| Confidence        | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/liamspradlin/Girassol-Display`
- `commit`: `cc8fa1b5a1afc28520fdc0ccc36256db243d9dfa`

No `files` mapping or `branch` field is present. No `config_yaml` is set (correct behavior since an override config.yaml exists locally).

### Git History in google/fonts

Key commits in `ofl/girassol/`:

1. **b16a7cf69** (2019-12-05) - `girassol: v1.004 added` by Yanone (authored) / Marc Foley (committed). This is the initial onboarding commit that added DESCRIPTION.en_us.html, Girassol-Regular.ttf, METADATA.pb, and OFL.txt.
2. **00fd5764d** (2019-12-05) - Merge of PR #2271 from `yanone/girassol`, merged by Marc Foley.
3. **2423d2aef** (2023-12-14) - `Update upstreams` by Simon Cozens. Added the source block with `repository_url` to METADATA.pb (no commit hash at this point).
4. **3122a09a9** (2025-11-27) - `sources info for girassol: v1.004 (PR #2271)` by Felipe Sanches. Added the `commit` hash to the source block and created the override `config.yaml`.

### Upstream Repository Verification

- **Location**: Cached at `upstream_repos/fontc_crater_cache/liamspradlin/Girassol-Display`
- **Remote URL**: `https://github.com/liamspradlin/Girassol-Display` (matches METADATA.pb)
- **Commit `cc8fa1b` verified**: This is the HEAD of the master branch and the latest commit. It is a merge commit from 2019-12-05 merging Yanone's PR #8 which included the "Fresh TTF" (unhinted font build) and copyright fix.
- **Source files**: `sources/Girassol-Regular.ufo` (UFO source)
- **Build script**: `build.sh` uses fontmake to compile from the UFO source
- **No config.yaml in upstream**: The upstream repo has no `config.yaml`. An override config exists in google/fonts.
- **Binary match**: The TTF file at `fonts/Girassol-Regular.ttf` (37644 bytes) in the upstream repo has an identical MD5 hash (`f7c9221557edb84d22e2122110ed3290`) to the file in google/fonts.

### Commit Hash Verification

The commit `cc8fa1b` was created on 2019-12-05, the same day as both the onboarding commit in google/fonts (`b16a7cf69`, 2019-12-05) and the merge of PR #2271. The timeline is:
1. Yanone's PR #8 merged in upstream (commit `cc8fa1b`) on 2019-12-05 at 13:40 EST, which included the "Fresh TTF" build producing the 37644-byte font
2. The google/fonts onboarding commit (`b16a7cf69`) was authored the same day at 12:14 CET
3. PR #2271 merged in google/fonts on 2019-12-05

The binary font files match exactly (MD5: `f7c9221557edb84d22e2122110ed3290`), confirming this is the correct onboarding commit.

### Override config.yaml

The override `config.yaml` in `ofl/girassol/config.yaml` contains:
```yaml
buildVariable: false
sources:
  - sources/Girassol-Regular.ufo
```

This correctly references the UFO source file in the upstream repo.

## Conclusion

The existing source metadata for Girassol is **complete and correct**. The source block has the correct repository URL and commit hash, both verified through binary matching and timeline analysis. The override config.yaml is in place. The only minor gap is the lack of `files` mapping and `branch` field in the source block, but these are optional and the essential data is present.

### Recommended METADATA.pb Source Block

The current source block is correct and complete for essential fields. No changes needed:

```
source {
  repository_url: "https://github.com/liamspradlin/Girassol-Display"
  commit: "cc8fa1b5a1afc28520fdc0ccc36256db243d9dfa"
}
```

**Status**: complete
**Confidence**: HIGH
