# Investigation Report: Libre Franklin

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Family**: Libre Franklin
**Directory**: `ofl/librefranklin`
**Designer**: Impallari Type
**License**: OFL
**Status**: complete
**Confidence**: HIGH

## Summary

Libre Franklin is a well-documented variable font family with a complete source block in METADATA.pb. The upstream repository, commit hash, config.yaml path, and file mappings were all verified and found to be correct. No changes are needed.

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/googlefonts/Libre-Franklin"
  commit: "310b7eef1f7b7ba82322295e0034675ea68040b0"
  files { ... }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Upstream Repository

- **URL**: https://github.com/googlefonts/Libre-Franklin (verified accessible, HTTP 200)
- **Branch**: master
- **Local cache**: `upstream_repos/fontc_crater_cache/googlefonts/Libre-Franklin`
- **Repo status**: Clean, up to date with remote

### Repository History

The repository was originally hosted at `impallari/Libre-Franklin` (still accessible at https://github.com/impallari/Libre-Franklin), then moved to `TypeNetwork/Libre-Franklin` (now redirects to googlefonts), and currently resides at `googlefonts/Libre-Franklin`.

The local clone is a shallow clone showing only the HEAD commit. The latest commit on master is `310b7eef` ("update licence URL", authored by Emma Marichal on 2024-09-05).

## Commit Hash Verification

The METADATA.pb references commit `310b7eef1f7b7ba82322295e0034675ea68040b0`, which was verified:

- **Commit message**: "update licence URL"
- **Author**: Emma Marichal (emmamarichal)
- **Date**: 2024-09-05 11:12:29 +0200
- **Status**: This is the HEAD of the master branch (latest commit)

### Timeline Verification

The commit was referenced in google/fonts PR #8134 ("Libre Franklin: Version 3.000 added"), also by Emma Marichal. The PR body explicitly states: "Taken from the upstream repo https://github.com/googlefonts/Libre-Franklin at commit https://github.com/googlefonts/Libre-Franklin/commit/310b7eef1f7b7ba82322295e0034675ea68040b0."

- Upstream commit date: 2024-09-05 11:12:29 +0200
- google/fonts commit (a2daac853): 2024-09-05 11:30:40 +0200 (same day, 18 minutes later)
- PR #8134 created: 2024-09-05T09:30:44Z
- PR #8134 merged: 2024-09-06T11:45:17Z

The timeline is consistent: Emma Marichal made the upstream commit, then immediately created the google/fonts PR referencing that exact commit. The same person authored both the upstream commit and the google/fonts onboarding PR, giving high confidence in the hash accuracy.

## config.yaml Verification

The config.yaml exists at `sources/config.yaml` in the upstream repo at the referenced commit. It is a valid gftools-builder configuration:

```yaml
sources:
  - LibreFranklin.glyphs
  - LibreFranklin-Italic.glyphs
axisOrder:
  - wght
familyName: Libre Franklin
stat:
  LibreFranklin[wght].ttf:
  - name: Weight
    tag: wght
    values: [Thin:100, ExtraLight:200, Light:300, Regular:400, Medium:500, SemiBold:600, Bold:700, ExtraBold:800, Black:900]
  - name: Italic
    tag: ital
    values: [Roman:0]
  LibreFranklin-Italic[wght].ttf:
  - name: Weight
    tag: wght
    values: [Thin:100, ExtraLight:200, Light:300, Regular:400, Medium:500, SemiBold:600, Bold:700, ExtraBold:800, Black:900]
  - name: Italic
    tag: ital
    values: [Italic:1]
```

The sources reference `.glyphs` files (Glyphs format), which are gftools-builder compatible. No override config.yaml exists in the google/fonts family directory.

## Source Files at Referenced Commit

At commit `310b7eef`, the following source files were verified to exist:
- `sources/LibreFranklin.glyphs` (Roman source)
- `sources/LibreFranklin-Italic.glyphs` (Italic source)
- `sources/config.yaml` (gftools-builder configuration)
- `sources/V.2000/` (directory with older version sources)
- `fonts/variable/LibreFranklin[wght].ttf` (compiled variable font)
- `fonts/variable/LibreFranklin-Italic[wght].ttf` (compiled variable italic font)

## google/fonts History

Key commits modifying `ofl/librefranklin/`:

1. **4a9988f84** (2017-07-26) - "librefranklin: v1.002 added. (#1100)" - Initial onboarding
2. **bac9b4ad1** (2020-10-13) - "Libre Franklin: Version 2.000 added (#2721)" - PR #2721 by Marc Foley, taken from TypeNetwork/Libre-Franklin at commit 84f508d. Converted from static to variable fonts.
3. **a2daac853** (2024-09-05) - "Libre Franklin: Version 3.000 added" - PR #8134 by Emma Marichal, taken from googlefonts/Libre-Franklin at commit 310b7eef. Added source block with commit hash, updated repo URL from TypeNetwork to googlefonts, added cyrillic subsets and static fonts.
4. **8e7a5aa44** (2024-09-05) - "remove statics" - Follow-up commit by Emma Marichal removing the static font files that were added in the previous commit.
5. **4ad8ac680** (2025-03-31) - "[Batch 2/4] port info from fontc_crater targets list" - Added `config_yaml: "sources/config.yaml"` to the source block.

## Conclusion

The Libre Franklin source metadata is **complete** and **accurate**:
- Repository URL is correct and accessible
- Commit hash `310b7eef` is verified as the exact commit used for the Version 3.000 onboarding (PR #8134)
- The `config_yaml` field correctly points to `sources/config.yaml` in the upstream repo
- The branch is correctly set to `master`
- All file mappings in the source block are valid

No corrections needed. Status: **complete**.
