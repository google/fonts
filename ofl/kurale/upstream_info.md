# Kurale - Investigation Report

**Family Name**: Kurale
**Directory Slug**: `kurale`
**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete

---

## METADATA.pb Analysis

The METADATA.pb file at `ofl/kurale/METADATA.pb` contained a source block with both a repository URL and a commit hash:

```
source {
  repository_url: "https://github.com/etunni/kurale"
  commit: "ff36a9f75711afc415a9a9f96968861d22d878cf"
}
```

The `config_yaml` field was correctly omitted because an override `config.yaml` exists in the google/fonts family directory.

**Designer**: Eduardo Tunni
**License**: OFL
**Date Added**: 2015-05-14
**Primary Script**: Devanagari
**Category**: Serif

## Upstream Repository

- **URL**: https://github.com/etunni/kurale
- **Cached at**: `upstream_repos/fontc_crater_cache/etunni/kurale/`
- **Remote verified**: origin points to `https://github.com/etunni/kurale`
- **Default branch**: master

The repository contained a `.glyphs` source file at `sources/Kurale.glyphs` (68,490 lines, ~1.1 MB) and pre-built font binaries in `fonts/`. The DESCRIPTION.en_us.html also confirmed the upstream URL, describing Kurale as derived from Gabriela and linking to the same GitHub repository.

## Source Files

At the referenced commit `ff36a9f`:
- `sources/Kurale.glyphs` - Glyphs source file (Latin, Cyrillic, and Devanagari)
- `fonts/Kurale-Regular.ttf` - Pre-built TTF binary
- `fonts/Kurale-Regular.otf` - Pre-built OTF binary

The source is a single-master, non-variable font (`buildVariable: false`).

## Commit Hash Verification

The METADATA.pb referenced commit `ff36a9f75711afc415a9a9f96968861d22d878cf` with message "sources | fonts | OFL: updated copyright string", dated 2016-12-14.

### Binary Verification

The TTF binary at the referenced commit was compared with the onboarded binary in google/fonts:

| Source | MD5 |
|--------|-----|
| Upstream `ff36a9f:fonts/Kurale-Regular.ttf` | `7e63a40022b4b92268acd6a84d703a06` |
| google/fonts onboarding commit `66afa1b59:ofl/kurale/Kurale-Regular.ttf` | `7e63a40022b4b92268acd6a84d703a06` |

**Exact match confirmed.** The commit hash `ff36a9f` is the correct onboarding reference.

### Timeline Analysis

- **2016-12-14**: Commit `ff36a9f` made in upstream (copyright string update)
- **2016-12-14**: Merge commit `ffff94a` merged `ff36a9f` into master (PR #2 from m4rc1e)
- **2017-01-17**: Font onboarded in google/fonts as v2.000 via PR #547 (commit `66afa1b59`, author: Marc Foley)
- **2017-03-13**: Later merge commit `08bf768` (PR #4 from alexeiva) - this was a re-merge of the same content, post-onboarding

The commit `ff36a9f` is the actual content commit (not a merge commit), and both it and its merge `ffff94a` produce identical TTF binaries that match the onboarded file. Using the content commit rather than the merge commit is the correct choice for the source block reference.

## Override config.yaml

An override `config.yaml` existed in the google/fonts family directory (`ofl/kurale/config.yaml`):

```yaml
buildVariable: false
sources:
  - sources/Kurale.glyphs
```

This was added in commit `c2fdc6a7d` ("sources info for Kurale: v2.000 (PR #547)") by Felipe Sanches on 2025-10-30. The upstream repository had no `config.yaml` file, so the override was necessary for gftools-builder compatibility.

The `config_yaml` field was correctly omitted from METADATA.pb since google-fonts-sources auto-detects local overrides.

## History in google/fonts

Key commits affecting Kurale in google/fonts:

1. `745abb20d` - Initial addition of Kurale
2. `66afa1b59` - "kurale: v2.000 added (#547)" - v2.000 onboarding by Marc Foley (2017-01-17)
3. `21e98aac8` - "More upstreams (i,j,k)" - Simon Cozens added repository_url to source block (2024-01-14)
4. `c2fdc6a7d` - "sources info for Kurale: v2.000 (PR #547)" - Added commit hash and override config.yaml (2025-10-30)

## Conclusion

The source block in METADATA.pb was complete with:
- **Repository URL**: `https://github.com/etunni/kurale` (verified, accessible)
- **Commit**: `ff36a9f75711afc415a9a9f96968861d22d878cf` (verified via binary match)
- **Config**: Override `config.yaml` in google/fonts family directory (correctly omitted from METADATA.pb)
- **Status**: complete
- **Confidence**: HIGH

No further action was required for this family.
