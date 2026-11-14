# Cherry Bomb One - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Cherry Bomb One |
| **Designer** | Satsuyako |
| **License** | OFL |
| **Category** | DISPLAY |
| **Date Added** | 2020-12-14 |
| **Repository URL** | https://github.com/satsuyako/CherryBomb |
| **Commit Hash** | 9171b63b087c39b1d769287287f38582a57911eb |
| **Branch** | ver3.00 |
| **Config YAML** | Override in google/fonts |
| **Status** | complete |

## How URL Found

The repository URL `https://github.com/satsuyako/CherryBomb` is documented in the METADATA.pb source block and confirmed by multiple PRs:

- PR #2881 ("Cherry Bomb One: Version 4.000; ttfautohint (v1.8.3) added") - initial onboarding by Aaron Bell - references `https://github.com/satsuyako/CherryBomb.git`
- PR #2983 ("Cherry Bomb One: Version 4.100; ttfautohint (v1.8.3) added") - update by Aaron Bell - references the same repo

The copyright notice also references this URL: "Copyright 2019 The Cherry Bomb Project Authors (https://github.com/satsuyako/CherryBomb)"

## How Commit Determined

The commit hash `9171b63b087c39b1d769287287f38582a57911eb` is explicitly documented in:
1. The METADATA.pb source block
2. PR #2983 body: "Cherry Bomb One Version 4.100; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/satsuyako/CherryBomb.git at commit https://github.com/satsuyako/CherryBomb/commit/9171b63b087c39b1d769287287f38582a57911eb."
3. The update commit message (`6d254d751`)

This commit is a merge commit on the `ver3.00` branch: "Merge pull request #12 from aaronbell/ver3.00". It is not HEAD -- additional commits have been made after onboarding:
- `b773690` - "Fixed the commaaccent glyph shape to avoid confusion with cedilla"
- `bdacbec` - Merge pull request #13 from shujisado/patch-1
- `399e313` - "Modify SIL1.1 ja-trans URL"

These post-onboarding commits would need separate review before incorporation.

### Onboarding History

1. **v4.000** (PR #2881, 2021-01-18): Initial onboarding from commit `9f7cce81aa78b3b13eceb86ec6282f23651350a2`
2. **v4.100** (PR #2983, 2021-02-11): Update from commit `9171b63b087c39b1d769287287f38582a57911eb` (current recorded commit)

## Config YAML Status

**Override config.yaml exists in google/fonts.** The file at `google/fonts/ofl/cherrybombone/config.yaml` contains:

```yaml
buildVariable: false
sources:
  - sources/CherryBomb.glyphs
```

The upstream repository does not have a `config.yaml` file. Instead, it has a custom `build.py` script that uses fontmake/glyphsLib/ufo2ft programmatically. The override config.yaml was added in commit `9eac7c371` ("sources info for Cherry Bomb One: Version 4.100 (PR #2983)").

Since an override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block per project policy.

The source file `sources/CherryBomb.glyphs` exists in the upstream repo at the recorded commit.

## Verification

- **Repository URL**: Verified - cloned at `upstream_repos/fontc_crater_cache/satsuyako/CherryBomb/`, remote matches
- **Commit hash**: Verified - exists in repo on `ver3.00` branch, confirmed by PR #2983 and commit message
- **Branch**: Verified - `ver3.00` is the default branch (remotes/origin/HEAD -> origin/ver3.00), and the recorded commit exists on this branch
- **Override config.yaml**: Verified - exists at `google/fonts/ofl/cherrybombone/config.yaml`
- **Source files**: Verified - `sources/CherryBomb.glyphs` exists in upstream
- **METADATA.pb source block**: Complete with repository_url, commit, branch, and file mappings (config_yaml correctly omitted due to override)

## Confidence Level

**HIGH** across all fields. Everything is explicitly documented in PRs, commit messages, and METADATA.pb. The override config.yaml correctly addresses the lack of a config file in the upstream repo.

## Open Questions

- None. This family is fully documented and verified. Note that 3 commits exist after the recorded onboarding commit on the `ver3.00` branch, which would need review before any future update.
