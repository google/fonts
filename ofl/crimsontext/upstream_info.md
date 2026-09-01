# Crimson Text - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Crimson Text |
| Repository URL | https://github.com/googlefonts/Crimson |
| Commit Hash | 4f1458ae64c6c0d9c5fdfbf5095c7fabe0fa063f |
| Branch | master |
| Config YAML | sources/config.yaml |
| Designer | Sebastian Kosch |
| License | OFL |
| Date Added | 2011-01-26 |

## How URL Found

The repository URL `https://github.com/googlefonts/Crimson` is documented in the METADATA.pb `source {}` block. The original Crimson Text project was at `skosch/Crimson`, but was transferred to the googlefonts organization. The copyright strings in the METADATA.pb font entries reference this googlefonts URL.

## How Commit Determined

The commit hash `4f1458ae64c6c0d9c5fdfbf5095c7fabe0fa063f` was set in the METADATA.pb source block when the fonts were last updated in PR #4416 (commit 1ac62d533, authored by Emma Marichal on 2022-03-30).

**Important nuance**: The PR #4416 body text initially referenced an earlier commit `f8b7d63dd515b63aa232857f76af3f9da048f239` ("Merge pull request #3 from emmamarichal/master", 2022-03-24). However, the METADATA.pb source block in the same PR already had commit `4f1458a` ("Merge pull request #4 from emmamarichal/master", 2022-03-25). This indicates the PR was updated after additional work was done upstream (PR #4 added "Some glyphs: ordinals, idotaccent, caron.alt"). The METADATA.pb is the authoritative record, and `4f1458a` is HEAD of the upstream repo, confirming this is the final commit used.

Chronology:
- 2022-03-24: Upstream commit `f8b7d63` (PR #3 merged - version number change)
- 2022-03-25: Upstream commit `4f1458a` (PR #4 merged - additional glyphs added) -- **this is the recorded commit**
- 2022-03-30: google/fonts commit 1ac62d533 (PR #4416 merged)

## Config YAML Status

The config file `sources/config.yaml` exists in the upstream repository at the referenced commit. It contains:

```yaml
sources:
  - CrimsonText.glyphs
  - CrimsonText-Italic.glyphs
familyName: "Crimson Text"
buildVariable: false
autohintTTF: false
```

This is a valid gftools-builder configuration pointing to Glyphs sources. The `config_yaml` field was added to METADATA.pb in commit 19cdcec59 ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31).

## Verification

- **Repository accessible**: Yes - cloned at `upstream_repos/fontc_crater_cache/googlefonts/Crimson/`
- **Commit exists**: Yes - `4f1458a` is HEAD of the upstream repo
- **Config exists at commit**: Yes - `sources/config.yaml` is present at the referenced commit
- **Source files present**: Yes - `.glyphs` files for Roman and Italic
- **Font files match**: Binary .ttf files are mapped via `files {}` entries in METADATA.pb (6 styles: Regular, Italic, SemiBold, SemiBoldItalic, Bold, BoldItalic)
- **Commit hash is HEAD**: Yes, `4f1458a` is the latest commit in the repo

## Confidence Level

**HIGH** - The commit hash in METADATA.pb was set during the original font update PR (#4416). While the PR body text referenced an earlier commit, the METADATA.pb source block had the final commit from the beginning. The upstream repo confirms this is HEAD, config.yaml exists, and all source data is consistent.

## Open Questions

None.
