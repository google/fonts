# Investigation Report: Bpmf Zihi Kai Std

## Source Data

| Field | Value |
|---|---|
| Family Name | Bpmf Zihi Kai Std |
| Designer | But Ko |
| License | OFL |
| Date Added | 2026-01-30 |
| Repository URL | https://github.com/ButTaiwan/bpmfvs |
| Commit Hash | `20f741c18bb917b63576293906c01e82ddfce032` |
| Config YAML | None |
| Status | missing_config |

## How URL Found

The repository URL was set in METADATA.pb during the original onboarding. Bpmf Zihi Kai Std was added via PR #10173 by Aaron Bell (`aaronbell`), merged 2026-02-11. The PR body describes it as a "New project" (unlike Huninn and Iansui which are "Based on existing GF fonts"). Same note about building in `aaronbell/bpmfvs` with planned transition to `ButTaiwan/bpmfvs`.

All three Bpmf families share the same upstream repository.

## How Commit Determined

The commit hash `20f741c18bb917b63576293906c01e82ddfce032` was added by our automation (commit `9a14639f3`, 2026-02-25). This is the HEAD of `ButTaiwan/bpmfvs` from 2025-12-13.

**Critical issue**: Same as the other Bpmf families. The fonts were built in `aaronbell/bpmfvs`, and the recorded commit predates the actual build by over a month.

The onboarding timeline for Bpmf Zihi Kai Std is more complex, with multiple font binary updates:
1. Initial onboarding: `f91754e81` (2026-01-30) "Adding Bpmf Zihi Kai Std"
2. Formatting update: `44d5c78d8`
3. METADATA update: `c27a727d9`
4. First binary update: `8090ba2c9` (2026-01-30) "Update BpmfZihiKaiStd-Regular.ttf"
5. Second binary update: `72cd1d1f6` (2026-02-09) "Updating with various fixes"
6. Third binary update: `f55b8f2bb` (2026-02-09) "Update BpmfZihiKaiStd-Regular.ttf"
7. Further fixes: `f56ed21ec` (copyright/license URLs), `26417436c` (newline), `3b5debf6e` (URL formatting)

This family had the most font binary updates of the three Bpmf families (3 updates vs 1 each for Huninn and Iansui).

## Config YAML Status

**No config.yaml exists** and none can be created for gftools-builder.

Same situation as all Bpmf families - custom Ruby-based build system (`make_font.rb`). The base font for Zihi Kai Std comes from `srcfonts/ZihiKaiStd.ttf` (source not documented in `upstream_sources.json`, suggesting it may be an original creation or sourced separately).

## Verification

- **Repository accessible**: Yes, both `ButTaiwan/bpmfvs` and `aaronbell/bpmfvs` are accessible
- **Commit exists**: Yes, `20f741c` exists in both repos
- **Commit is correct for current binary**: No - the current binary was built from a later commit in `aaronbell/bpmfvs` (likely from Feb 9, 2026)
- **Local cache**: Neither repo is cached locally
- **Source files**: Custom build system (Ruby-based), no standard font sources

## Confidence Level

**MEDIUM** - Same fundamental issues as the other Bpmf families. The repository URL is the canonical upstream but the fonts were built from Aaron Bell's fork. The commit hash is incorrect.

## Open Questions

1. **Which exact commit in aaronbell/bpmfvs produced the final binary?** The third update (`f55b8f2bb`, Feb 9, 2026) was the last binary change, so the build commit in the fork should be from around that time.
2. **Where does the ZihiKaiStd base font come from?** Unlike Huninn (from justfont) and Iansui (from ButTaiwan/iansui), the Zihi Kai Std source font is not documented in `upstream_sources.json`.
3. **Will the transition from aaronbell/bpmfvs to ButTaiwan/bpmfvs happen?** Until it does, the recorded commit hash will remain inaccurate.
4. This family had the most updates of the three Bpmf families, suggesting it required more iteration to get right.

## Recent upstream/main activity (post-investigation)

The Bpmf Zihi Kai Std family was onboarded in a multi-commit sequence by Aaron Bell (2026-01-30) with the most binary updates of the three Bpmf families. The earlier investigation already documents some commits in the Onboarding timeline; for completeness, three additional shared-with-siblings commits are recorded here:

- **2026-01-30** — Aaron Bell, commit [`423e25002`](https://github.com/google/fonts/commit/423e25002) ("Onboarding three families related to the Bopomofo phonetic system"): the umbrella onboarding commit that introduced all three Bpmf families (Huninn, Iansui, Zihi Kai Std) at once.
- **2026-01-30** — Aaron Bell, commit [`cc204af75`](https://github.com/google/fonts/commit/cc204af75) ("One at a time is the way to go..."): incremental retry that re-onboarded Iansui and Zihi Kai Std after the umbrella commit's binary issues.
- **2026-01-30** — Aaron Bell, commit [`d6f37786b`](https://github.com/google/fonts/commit/d6f37786b) ("Updating strings"): same-day binary update touching both Bpmf Huninn and Bpmf Zihi Kai Std (binary-only commit per the diff).

All three are part of the original onboarding sequence. The recorded `commit` and `repository_url` fields in METADATA.pb still point to ButTaiwan/bpmfvs while the actual binaries were built in aaronbell/bpmfvs (the commit-hash provenance issue flagged in the original investigation remains open).
