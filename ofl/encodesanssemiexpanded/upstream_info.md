# Investigation: Encode Sans Semi Expanded

## Summary

| Field | Value |
|---|---|
| **Family Name** | Encode Sans Semi Expanded |
| **Designer** | Impallari Type, Andres Torresi, Jacques Le Bailly |
| **License** | OFL |
| **Date Added** | 2017-02-08 |
| **Repository URL** | https://github.com/impallari/Encode-Sans |
| **Commit Hash** | `370cdccdb22daf862c6fca0636aad64b6835decd` |
| **Branch** | master |
| **Config YAML** | None (needs override) |
| **Status** | missing_config |
| **Confidence** | HIGH |

## METADATA.pb Analysis

The METADATA.pb file at `ofl/encodesanssemiexpanded/METADATA.pb` has an existing `source {}` block added by Simon Cozens in commit `c8a4f8556` (2024-01-14, "More upstreams (e,f)"):

```
source {
  repository_url: "https://github.com/impallari/Encode-Sans"
}
```

The source block has the repository URL but is missing `commit` and `config_yaml` fields.

## Upstream Repository

**Repository**: https://github.com/impallari/Encode-Sans (verified accessible, HTTP 200)

The impallari/Encode-Sans repository is the original source for the Encode Sans superfamily, containing all width variants (Normal, Condensed, Semi Condensed, Semi Expanded, Expanded) within a single Glyphs source file.

### Source Files

- `sources/Encode-Sans.glyphs` -- single Glyphs source file containing all masters and instances for all width variants (9 SemiExpanded instances confirmed)

### Repository Structure

```
AUTHORS.txt
CONTRIBUTORS.txt
fonts/               (pre-compiled TTFs for all width variants)
OFL.txt
README.md
sources/
  Encode-Sans.glyphs
```

### Commit History (relevant)

| Hash | Date | Author | Message |
|---|---|---|---|
| `370cdcc` | 2017-02-03 | impallari (merge) | Merge pull request #3 from m4rc1e/master |
| `fc35928` | 2017-01-30 | Marc Foley (m4rc1e) | fonts \| sources: Changed thin weight to 250 |
| `2fdfa4a` | 2017-01-27 | impallari (merge) | Merge pull request #2 from m4rc1e/master |
| `97a5aec` | 2017-01-03 | Marc Foley (m4rc1e) | sources \| fonts: updated font names and regenerated fonts |

No tags exist in the repository.

## Onboarding Analysis

### google/fonts History

The font files were added to google/fonts in a single commit:

- **Commit**: `b72acc6d6cbf82d2d7b5d431bcc5c673be18e412`
- **Date**: 2017-02-07
- **Author**: Marc Foley
- **Message**: "encodesanssemiexpanded: v2.000 added (#629)"
- **PR**: [#629](https://github.com/google/fonts/pull/629)

PR #629 body states: "This complies with our Font Bakery Discussion, googlefonts/fontbakery#1211. Family name is Encode Sans Semi Expanded."

The font binary files have not been modified since this initial onboarding commit.

### Commit Hash Determination

The onboarding commit hash is determined to be `370cdccdb22daf862c6fca0636aad64b6835decd` (tip of master in impallari/Encode-Sans) based on:

1. **Timeline alignment**: The upstream commit (2017-02-03) predates the google/fonts merge (2017-02-07) by 4 days.
2. **Same author**: Marc Foley (m4rc1e) authored both the upstream PRs (#2, #3) in impallari/Encode-Sans and the google/fonts PR #629.
3. **File size correlation**: Binary files differ by only 4-52 bytes per file, consistent with minor post-processing (fontbakery fixes, hinting adjustments) rather than different source commits.
4. **No later commits**: `370cdcc` is the latest and final commit in the repository. There are no subsequent commits that could have been the source.

| File | Upstream Size | google/fonts Size | Diff |
|---|---|---|---|
| EncodeSansSemiExpanded-Regular.ttf | 169,436 | 169,488 | +52 |
| EncodeSansSemiExpanded-Bold.ttf | 169,412 | 169,420 | +8 |
| EncodeSansSemiExpanded-Thin.ttf | 163,196 | 163,204 | +8 |

**Confidence: HIGH** -- The latest commit is the only plausible source. Marc Foley performed both the upstream work and the google/fonts onboarding within the same week.

## config.yaml Status

**No config.yaml exists** in either the upstream repository or the google/fonts family directory.

The upstream repo has a `.glyphs` source file (`sources/Encode-Sans.glyphs`) which is compatible with gftools-builder. However, the single source file generates all width variants (Normal, Condensed, Semi Condensed, Semi Expanded, Expanded), which complicates creating an override config.yaml for a single width variant.

A config.yaml override could be created for gftools-builder, but it would need to specify which instances to generate (only the Semi Expanded ones from the full designspace).

## Related Families

The Encode Sans superfamily spans multiple google/fonts entries, all sharing the same upstream repository structure:

| Family | Repository | Status |
|---|---|---|
| Encode Sans (base) | thundernixon/Encode-Sans | Updated to v3 (variable font, 2020) |
| Encode Sans Condensed | impallari/Encode-Sans | Still at v2 (static, 2017) |
| Encode Sans Semi Condensed | impallari/Encode-Sans | Still at v2 (static, 2017) |
| Encode Sans Semi Expanded | impallari/Encode-Sans | Still at v2 (static, 2017) |
| Encode Sans Expanded | impallari/Encode-Sans | Still at v2 (static, 2017) |
| Encode Sans SC | thundernixon/Encode-Sans | Separate small caps variant |

The base "Encode Sans" family was upgraded to v3.0 by Stephen Nixon (thundernixon) in 2020 via PR #2438, which introduced a variable font with wght+wdth axes. The width-specific static families (Condensed, Semi Condensed, Semi Expanded, Expanded) remain at v2 from the original impallari repository.

## Notes

- The impallari/Encode-Sans repo has had no activity since 2017-02-03. It appears to be archived/inactive.
- The thundernixon/Encode-Sans fork is a significant rework (v3) that consolidated the design into a variable font. It is the canonical upstream for the base "Encode Sans" family but not for the width-specific static families.
- The width-specific families in google/fonts (Condensed, Semi Condensed, Semi Expanded, Expanded) may eventually be considered superseded by the variable font's width axis, but they remain as separate catalog entries.
