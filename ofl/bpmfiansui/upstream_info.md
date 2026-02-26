# Investigation Report: Bpmf Iansui

## Source Data

| Field | Value |
|---|---|
| Family Name | Bpmf Iansui |
| Designer | But Ko |
| License | OFL |
| Date Added | 2026-01-30 |
| Repository URL | https://github.com/ButTaiwan/bpmfvs |
| Commit Hash | `20f741c18bb917b63576293906c01e82ddfce032` |
| Config YAML | None |
| Status | missing_config |

## How URL Found

The repository URL was set in METADATA.pb during the original onboarding. Bpmf Iansui was added via PR #10172 by Aaron Bell (`aaronbell`), merged 2026-02-11. The PR body states: "At present, these are being built in https://github.com/aaronbell/bpmfvs, but will be transitioned upstream to https://github.com/ButTaiwan/bpmfvs once the rest of the fonts' build systems are modernized."

All three Bpmf families (Huninn, Iansui, Zihi Kai Std) share the same upstream repository.

## How Commit Determined

The commit hash `20f741c18bb917b63576293906c01e82ddfce032` was added by our automation (commit `9a14639f3`, 2026-02-25). This is the HEAD of `ButTaiwan/bpmfvs` from 2025-12-13 ("Update build-ttf.yml").

**Critical issue**: Same as Bpmf Huninn. The fonts were built in `aaronbell/bpmfvs`, not `ButTaiwan/bpmfvs`. The recorded commit predates the actual build by over a month.

The onboarding timeline for Bpmf Iansui:
1. Initial onboarding via separate PR: `0fbc58136` (2026-01-30) "Adding Bpmf Iansui"
2. Formatting update: `3a2656154`
3. Font binary updated: `589446f9f` (2026-02-09) "Update BpmfIansui-Regular.ttf - Updating with various fixes"
4. Further fixes: `16db82397` (newline fix), `ae7a73564` (copyright fix), `1f665adf7` (URL fix)

The base font for Iansui comes from `github.com/ButTaiwan/iansui` (per `upstream_sources.json` in the bpmfvs repo).

## Config YAML Status

**No config.yaml exists** and none can be created for gftools-builder.

Same situation as all Bpmf families - the project uses a custom Ruby-based build system (`make_font.rb`) that processes base fonts and adds Bopomofo phonetic annotations via IVS. This cannot be represented as a gftools-builder config.

## Verification

- **Repository accessible**: Yes, both `ButTaiwan/bpmfvs` and `aaronbell/bpmfvs` are accessible
- **Commit exists**: Yes, `20f741c` exists in both repos
- **Commit is correct for current binary**: No - the current binary was built from a later commit in `aaronbell/bpmfvs`
- **Local cache**: Neither repo is cached locally
- **Source files**: Custom build system (Ruby-based), no standard font sources

## Confidence Level

**MEDIUM** - Same issues as Bpmf Huninn. The repository URL points to the canonical upstream but the fonts were built from Aaron Bell's fork. The commit hash is incorrect (too early).

## Open Questions

1. **Which exact commit in aaronbell/bpmfvs was used to build the current font binary?** Aaron Bell should be asked.
2. **Should the repository_url be updated to aaronbell/bpmfvs?** Or should we wait for the planned transition back to ButTaiwan/bpmfvs?
3. The base font (Iansui) comes from `github.com/ButTaiwan/iansui`, adding a dependency chain. Changes to the base font require rebuilding the Bpmf variant.
