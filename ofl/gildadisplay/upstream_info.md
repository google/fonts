# Investigation Report: Gilda Display

## Summary

Gilda Display is a classic serif display font by Eduardo Tunni, originally added to Google Fonts on 2012-10-31. It was updated in January 2023 via PR #5815 by Emma Marichal using gftools-packager, which also added the source block to METADATA.pb. The upstream repository is `etunni/gilda-display`, and the referenced commit `640bdfd` is the latest commit in the repo, representing Emma Marichal's update work. An override `config.yaml` already exists in the google/fonts family directory. The existing source metadata is complete and correct.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Gilda Display |
| Designer          | Eduardo Tunni |
| Repository URL    | https://github.com/etunni/gilda-display |
| Commit Hash       | 640bdfd3d2ee3b533d1f88687a9e4541136254e0 |
| Commit Date       | 2023-01-25 |
| Commit Description| Merge pull request #2 from emmamarichal/master |
| Config YAML       | Override config.yaml in google/fonts |
| Source File       | sources/GildaDisplay.glyphs |
| Branch            | master |
| Status            | **complete** |
| Confidence        | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb already contains a complete source block:
- `repository_url`: `https://github.com/etunni/gilda-display`
- `commit`: `640bdfd3d2ee3b533d1f88687a9e4541136254e0`
- `branch`: `master`
- `files` mappings for OFL.txt and the TTF

### Git History in google/fonts

Key commits in `ofl/gildadisplay/`:

1. **90abd17b4** - Initial commit (original onboarding, 2012)
2. **aacc2d180** (2023-01-25) - `[gftools-packager] Gilda Display: Version 1.002; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.22] added` by Emma Marichal. This commit added the source block to METADATA.pb and updated the font binary. The commit message explicitly references the upstream repo and commit hash.
3. **e4ee36af2** (2023-01-25) - `New push / description updated` by Emma Marichal. Updated DESCRIPTION.en_us.html.
4. **55b85ed84** (2023-01-25) - Merge of PR #5815, merged by Marc Foley.
5. **bc6966e5d** (2025-10-07) - `sources info for Gilda Display: Version 1.002 (PR #5815)` by Felipe Sanches. Added the override `config.yaml`.

### Upstream Repository Verification

- **Location**: Cached at `upstream_repos/fontc_crater_cache/etunni/gilda-display`
- **Remote URL**: `https://github.com/etunni/gilda-display` (matches METADATA.pb)
- **Commit `640bdfd` verified**: This is the HEAD of the master branch and the latest commit. It is a merge commit from 2023-01-25, merging Emma Marichal's work.
- **Source files**: `sources/GildaDisplay.glyphs` (Glyphs source)
- **No config.yaml in upstream**: The upstream repo has no `config.yaml`. An override config exists in google/fonts.
- **Binary match**: The TTF file at `fonts/ttf/GildaDisplay-Regular.ttf` (68020 bytes) in the upstream repo has an identical MD5 hash (`ca13b47da562dc0e3a7f4b360ab80787`) to the file in google/fonts.

### Commit Hash Verification

The commit `640bdfd` was created on 2023-01-25, the same day as the gftools-packager commit in google/fonts (also 2023-01-25). The gftools-packager commit message explicitly states: "taken from the upstream repo https://github.com/etunni/gilda-display at commit https://github.com/etunni/gilda-display/commit/640bdfd3d2ee3b533d1f88687a9e4541136254e0." The binary files match exactly.

### Override config.yaml

The override `config.yaml` in `ofl/gildadisplay/config.yaml` contains:
```yaml
buildVariable: false
sources:
  - sources/GildaDisplay.glyphs
```

This correctly references the `.glyphs` source file in the upstream repo.

## Conclusion

The existing source metadata for Gilda Display is **complete and correct**. All fields are properly set:
- Repository URL is valid and matches the upstream remote
- Commit hash `640bdfd` is verified as the correct onboarding commit (latest in upstream, binary match confirmed)
- Override config.yaml is in place in google/fonts
- The `files` block correctly maps the OFL.txt and TTF paths

### Recommended METADATA.pb Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/etunni/gilda-display"
  commit: "640bdfd3d2ee3b533d1f88687a9e4541136254e0"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/GildaDisplay-Regular.ttf"
    dest_file: "GildaDisplay-Regular.ttf"
  }
  branch: "master"
}
```

**Status**: complete
**Confidence**: HIGH
