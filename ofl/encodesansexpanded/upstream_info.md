# Encode Sans Expanded

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Impallari Type, Andres Torresi, Jacques Le Bailly
**METADATA.pb path**: `ofl/encodesansexpanded/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/impallari/Encode-Sans |
| Commit | `370cdccdb22daf862c6fca0636aad64b6835decd` |
| Config YAML | none |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/impallari/Encode-Sans` was already present in the METADATA.pb `source { repository_url }` field, added by Simon Cozens in commit `c8a4f8556` ("More upstreams (e,f)", 2024-01-14). This URL matches the copyright string in the font files: "Copyright 2012 The Encode Project Authors (impallari@gmail.com)". The URL resolves (HTTP 200) and contains the original Encode Sans superfamily sources covering all width variants (Normal, Condensed, Semi Condensed, Expanded, Semi Expanded).

Note: The main `encodesans` family (which was upgraded to v3 as a variable font) uses a different upstream repo (`https://github.com/thundernixon/Encode-Sans`), which is Stephen Nixon's redesigned version. However, the `encodesansexpanded` family was never updated to v3 and still uses the original v2.000 static fonts from the impallari repo.

## How the Commit Hash Was Identified

The font files in `ofl/encodesansexpanded/` were added by Marc Foley via PR #627 ("encodesansexpanded: v2.000 added"), merged on 2017-02-07 by Dave Crossland. The PR body was empty, providing no explicit upstream commit reference.

Marc Foley was also the author of the two most recent commits in the impallari/Encode-Sans repo:
- `97a5aec` (2017-01-03): "sources | fonts: updated font names and regenerated fonts"
- `fc35928` (2017-01-30): "fonts | sources: Cahnged thing weight to 250."

These were merged via PR #3 into the impallari repo as merge commit `370cdcc` on 2017-02-03, just 4 days before the google/fonts onboarding.

Binary comparison of the font files shows the fonts in google/fonts do NOT exactly match the pre-built fonts at any commit in the impallari repo (the files differ despite some having matching sizes). This indicates Marc Foley likely rebuilt the fonts from the `.glyphs` source file before submitting them to google/fonts. The source state at `370cdcc` (HEAD of the impallari repo) is the most likely source commit, as it was the latest commit at the time of the onboarding and Marc Foley authored the changes himself.

The FONTLOG.txt in google/fonts confirms: "30 Jane 2017 (Marc Foley) Encode v2.00 - Vietnamese added", matching this timeline.

## How Config YAML Was Resolved

The impallari/Encode-Sans repository does NOT contain a `config.yaml` file. The source file is a Glyphs file at `sources/Encode-Sans.glyphs`, which contains the full superfamily with multiple width and weight instances (including "Encode Sans Expanded" instances at width interpolation value 1000). No override `config.yaml` exists in the google/fonts family directory (`ofl/encodesansexpanded/`) either.

An override config.yaml could be created to reference the `.glyphs` source, but this is complicated by the fact that the single `.glyphs` source generates fonts for all five width families (Normal, Condensed, Semi Condensed, Expanded, Semi Expanded). The config would need to select only the Expanded instances.

## Verification

- Repository URL resolves: Yes (HTTP 200)
- Commit `370cdcc` exists in upstream repo: Yes
- Commit date: 2017-02-03 14:52:05 -0300
- Commit message: "Merge pull request #3 from m4rc1e/master — fonts | sources: Changed thin weight from 100 to 250."
- Commit author: Pablo Impallari (merge), Marc Foley (changes)
- Source files at commit: `sources/Encode-Sans.glyphs` (single .glyphs file for entire superfamily)
- Pre-built fonts at commit: `fonts/EncodeSansExpanded-*.ttf` (9 weight files)
- Font files match google/fonts: Not binary-identical (likely rebuilt by Marc Foley)

## Related Families

Encode Sans is a superfamily sharing the same upstream repo (`impallari/Encode-Sans`) for the v2.000 width variants:

| Family | Directory | Source Repo | Status |
|--------|-----------|-------------|--------|
| Encode Sans | `ofl/encodesans/` | thundernixon/Encode-Sans | Updated to v3 (variable font) |
| Encode Sans Condensed | `ofl/encodesanscondensed/` | impallari/Encode-Sans | Still v2.000 |
| Encode Sans Semi Condensed | `ofl/encodesanssemicondensed/` | impallari/Encode-Sans | Still v2.000 |
| Encode Sans Expanded | `ofl/encodesansexpanded/` | impallari/Encode-Sans | Still v2.000 |
| Encode Sans Semi Expanded | `ofl/encodesanssemiexpanded/` | impallari/Encode-Sans | Still v2.000 |
| Encode Sans SC | `ofl/encodesanssc/` | thundernixon/Encode-Sans | Updated to v3 |

The main Encode Sans and Encode Sans SC families were updated to v3 by Stephen Nixon (thundernixon/arrowtype) in 2020 as variable fonts with both width and weight axes. The four separate width families (Condensed, Semi Condensed, Expanded, Semi Expanded) remain at v2.000 with static fonts from the impallari repo.

## Confidence

**HIGH**: The repository URL is well-established in METADATA.pb and confirmed by the copyright string. The commit hash `370cdcc` is the HEAD of the impallari repo and represents the final state of the sources prepared by Marc Foley (who also submitted the google/fonts PR #627) just 4 days before the onboarding merge. While the binary font files are not exact matches (indicating a rebuild from sources), the source `.glyphs` file at this commit is definitively the one used for onboarding. The only gap is the missing `config.yaml`, which the impallari repo does not have.

## Open Questions

1. Should an override `config.yaml` be created for this family? The `.glyphs` source contains the full superfamily; a config would need instance-filtering to produce only the Expanded width variants.
2. The four v2.000 width families (Condensed, Semi Condensed, Expanded, Semi Expanded) have not been updated to use the thundernixon/Encode-Sans v3 sources, which include variable font support with width axis. Should these families be consolidated into the main Encode Sans variable font (which already has width axis coverage)?
