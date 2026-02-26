# Investigation Report: Bpmf Huninn

## Source Data

| Field | Value |
|---|---|
| Family Name | Bpmf Huninn |
| Designer | But Ko, justfont |
| License | OFL |
| Date Added | 2026-01-30 |
| Repository URL | https://github.com/ButTaiwan/bpmfvs |
| Commit Hash | `20f741c18bb917b63576293906c01e82ddfce032` |
| Config YAML | None |
| Status | missing_config |

## How URL Found

The repository URL was set in METADATA.pb by Aaron Bell during the original onboarding (commit `423e25002`, 2026-01-30). The METADATA.pb `source` block points to `https://github.com/ButTaiwan/bpmfvs`.

However, the PR (#10171) reveals that the fonts were actually built in Aaron Bell's fork at `https://github.com/aaronbell/bpmfvs`, with the intention of transitioning back to the main `ButTaiwan/bpmfvs` repository after other fonts were updated.

## How Commit Determined

The commit hash `20f741c18bb917b63576293906c01e82ddfce032` was added to METADATA.pb by our automation (commit `9a14639f3`, 2026-02-25). This commit exists in both `ButTaiwan/bpmfvs` and `aaronbell/bpmfvs`.

**Critical issue**: This commit (`20f741c`) is the HEAD of the `ButTaiwan/bpmfvs` repo from 2025-12-13 ("Update build-ttf.yml"). But the fonts were built in `aaronbell/bpmfvs`, which forked from this point and added many new commits during Jan-Feb 2026. The actual font binaries were built from commits in the fork that are newer than this hash.

The onboarding timeline:
1. Initial onboarding: `423e25002` (2026-01-30) by Aaron Bell
2. Font binary updated: `15555bd43` (2026-02-09) "Update BpmfHuninn-Regular.ttf - Updating with various fixes"
3. Further metadata fixes: `d0ec3026e`, `cc204af75`, `d6f37786b`, `308c0a0a5` (formatting and string updates)

The font binary was updated on Feb 9, 2026. In `aaronbell/bpmfvs`, there are many commits from that date. The actual build commit is unclear but is certainly NOT `20f741c`.

## Config YAML Status

**No config.yaml exists** and none can be created for gftools-builder.

The Bpmf project uses a custom Ruby-based build system (`make_font.rb`). The build process:
1. Takes base font TTFs as input (e.g., `srcfonts/Huninn-Regular.ttf` from github.com/justfont/Huninn)
2. Uses `otfccdump`/`otfccbuild` to manipulate font data
3. Adds Bopomofo phonetic annotations via IVS (Ideographic Variation Sequences)
4. Produces output fonts in `fonts/` directory

This is fundamentally different from gftools-builder and cannot be represented with a config.yaml.

## Verification

- **Repository accessible**: Yes, both `ButTaiwan/bpmfvs` and `aaronbell/bpmfvs` are accessible
- **Commit exists in both repos**: Yes, `20f741c` exists in both (it is the HEAD of ButTaiwan/bpmfvs)
- **Commit is correct for current binary**: No - the current binary was built from a later commit in `aaronbell/bpmfvs`
- **Local cache**: Neither repo is cached locally
- **Source files**: Custom build system (Ruby-based), no standard font sources

## Confidence Level

**MEDIUM** - The repository URL is reasonable (points to the canonical upstream), but the recorded commit hash is incorrect. The actual build commit should be from `aaronbell/bpmfvs` around Feb 9, 2026. The config.yaml will never exist for this project due to its custom build system.

## Open Questions

1. **Which exact commit in aaronbell/bpmfvs was used to build the current font binary?** Aaron Bell should be asked to clarify.
2. **Should the repository_url point to aaronbell/bpmfvs or ButTaiwan/bpmfvs?** The PR says it will transition to ButTaiwan, but that hasn't happened yet.
3. **Will this project ever have a config.yaml?** Given the custom Ruby-based build system, this seems unlikely without a complete rewrite of the build process.
4. The `upstream_sources.json` in the repo reveals that the Huninn base font comes from `github.com/justfont/Huninn`, adding a dependency chain.
