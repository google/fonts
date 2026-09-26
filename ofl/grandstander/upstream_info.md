# Investigation Report: Grandstander

**Model**: Claude Opus 4.7 (1M context)
**Date**: 2026-04-24

## Summary

Grandstander is a variable display/handwriting font (weight axis 100-900, normal + italic) designed by Tyler Finck and ETC (Etcetera Type Company), added to Google Fonts on 2020-07-24. The upstream repository is `Etcetera-Type-Co/Grandstander`.

The family was flagged by fontc_crater's `failed_repos.json` with reason "no config file was found": the `config_yaml: "Sources/config.yaml"` field in METADATA.pb pointed to a file that does not exist at the pinned onboarding commit `33c28849` (the upstream `Sources/config.yaml` was committed later, at HEAD `0bf9e31` in 2023). Because CLAUDE.md requires preserving the onboarding commit hash rather than bumping to a later rev, the override path was taken: a local `config.yaml` was added in `ofl/grandstander/` and the now-redundant `config_yaml` field was removed from METADATA.pb. `google-fonts-sources` auto-detects the override, so crater will pick it up on the next `targets.json` regeneration.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Grandstander                                       |
| Designer           | Tyler Finck, ETC                                   |
| Date Added         | 2020-07-24                                         |
| Repository URL     | https://github.com/Etcetera-Type-Co/Grandstander   |
| Onboarding Commit  | 33c288495d8ac7bc0b29a9f35801de1df7e6d010 (from PR #2575) |
| Config             | override `config.yaml` in `ofl/grandstander/` (no `config_yaml` in METADATA.pb) |
| Source Files       | Sources/Grandstander.glyphs, Sources/Grandstander-Italic.glyphs |
| Status             | complete                                           |
| Confidence         | HIGH                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb source block:
```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Grandstander"
  commit: "0bf9e31d529d7a67b23510b841cb3597db0cb130"
  config_yaml: "Sources/config.yaml"
}
```

### Git History in google/fonts

Key commits for this family:

1. `ae1d37ea9` (2020-07-27) - **Grandstander: v2.111 added (#2575)**
   - By Rosalie Wagner
   - Commit message: "Taken at upstream repo https://github.com/Etcetera-Type-Co/Grandstander at commit https://github.com/Etcetera-Type-Co/Grandstander/tree/33c288495d8ac7bc0b29a9f35801de1df7e6d010"
   - Added VF files: `Grandstander[wght].ttf` (183,056 bytes) and `Grandstander-Italic[wght].ttf` (185,092 bytes)
   - Also added static font instances

2. `70b0fc8a8` (2021) - **Remove static fonts for unhinted variable font families (#3695)**
   - Removed the static font files, keeping only the VF files

3. `2423d2aef` (2023-12-14) - **Update upstreams** by Simon Cozens
   - Added initial source block with only `repository_url`

4. `19cdcec59` (2025-03-31) - **[Batch 1/4] port info from fontc_crater targets list**
   - Added commit hash `0bf9e31d529d7a67b23510b841cb3597db0cb130` and `config_yaml: "sources/config.yaml"`

5. `7190093b1` (2025-05-22) - Fixed config_yaml capitalization to `Sources/config.yaml`

### Upstream Repository

Cached at `fontc_crater_cache/Etcetera-Type-Co/Grandstander/` (shallow clone, depth 1).

- **HEAD/master**: `0bf9e31` (2023-07-10) - "sharp stylistic alternates" by Tyler Finck
- Branch: `master` (not `main`)
- Only the HEAD commit is visible due to shallow clone

Source structure:
- `Sources/Grandstander.glyphs` (711,511 bytes)
- `Sources/Grandstander-Italic.glyphs` (715,100 bytes)
- `Sources/config.yaml`
- `Sources/legacy-2axes/` (older 2-axis build configuration)
- `fonts/variable/Grandstander[wght].ttf` (190,984 bytes)
- `fonts/variable/Grandstander-Italic[wght].ttf` (191,872 bytes)

Config.yaml (at HEAD) specifies two sources, axis order [wght, ital], and builds static, variable, TTF, OTF, and webfont outputs with full STAT table configuration.

### Commit Hash Discrepancy

This is a clear case of commit mismatch:

| Aspect | Onboarding (2020) | METADATA.pb (current) |
|--------|-------------------|-----------------------|
| Commit | `33c28849` | `0bf9e31` |
| Date | Pre-July 2020 | July 10, 2023 |
| Description | Unknown (shallow clone) | "sharp stylistic alternates" |

**Evidence the commit is wrong:**

1. **File size mismatch**: The VF files in google/fonts (183,056 and 185,092 bytes) differ significantly from those at the current upstream HEAD (190,984 and 191,872 bytes). The upstream files are ~8KB larger per file.

2. **Font files never updated**: Git log shows the Grandstander VF files were only ever written once -- in the original onboarding commit `ae1d37ea9` (2020-07-27).

3. **Timeline**: The onboarding was in July 2020, but commit `0bf9e31` is from July 2023. The upstream repo had significant changes (including "sharp stylistic alternates") that were never pulled into google/fonts.

4. **Source of the incorrect hash**: The commit `0bf9e31` was added via the fontc_crater targets list batch port (commit `19cdcec59`), which used data from fontc_crater's target.json. The fontc_crater cache used shallow clones, so it captured the latest HEAD rather than the original onboarding commit.

The correct onboarding commit is `33c288495d8ac7bc0b29a9f35801de1df7e6d010` as stated in the original PR #2575 commit message.

### Config.yaml at Onboarding Time

Direct inspection of the upstream repo at `33c28849` (via `raw.githubusercontent.com`) confirms that **no `Sources/config.yaml` existed at the onboarding commit**. The directory at that rev contains `Grandstander.glyphs`, `Grandstander-Italic.glyphs`, a `build.sh` shell script (which drives `fontmake` directly, without a gftools-builder config), a `.DS_Store`, and a `legacy-2axes/` subfolder with an older two-axis build. The upstream `Sources/config.yaml` was introduced later, at or before `0bf9e31d` (2023). This is why crater's `failed_repos.json` reports the family as "no config file was found" when `config_yaml: "Sources/config.yaml"` is declared in METADATA.pb against this rev.

## Historical Correction (Feb 2026, PR #10356)

Commit `994ed196` replaced the incorrect METADATA.pb `commit` field (`0bf9e31`, 2023 HEAD) with the correct onboarding commit (`33c28849`, 2020-07-27). The font binaries in google/fonts were built from `33c28849` and had never been updated, so the recorded commit now matches the shipped binaries.

However, that change retained `config_yaml: "Sources/config.yaml"`, a path that does not exist at `33c28849` — the upstream `Sources/config.yaml` was added later, in 2023. Setting a config_yaml that cannot be resolved at the pinned rev blocks fontc_crater, which reports the family in `failed_repos.json`.

## Action Taken

Applied the override path per CLAUDE.md's "Override config.yaml (STRICT)" policy:

1. **Added an override `ofl/grandstander/config.yaml`** in the google/fonts family directory. Its provenance:

   - **Sources list**: hand-written for this override to reference the `.glyphs` files that do exist at the pinned onboarding commit `33c28849` — `Sources/Grandstander.glyphs` and `Sources/Grandstander-Italic.glyphs`. Upstream's own later config uses the shorter paths `Grandstander.glyphs` / `Grandstander-Italic.glyphs` because that config sits inside `Sources/`; our override sits at the family-directory root in google/fonts and is fed to gftools-builder after the upstream repo is cloned, so paths must be relative to the upstream repo root.
   - **`axisOrder` and `stat` blocks**: **copied verbatim** from the upstream repo's own `Sources/config.yaml` at a later commit (`0bf9e31d`, 2023 HEAD). That upstream config was not yet present at `33c28849` — it was added three years later, after the 2020 onboarding — but its weight lineup matches the `.glyphs` files at both revs.
   - **Build/output flags omitted**: the upstream config also carried `outputDir`, `buildStatic`, `buildVariable`, `buildTTF`, `buildOTF`, `buildWebfont`, `cleanUp`, `includeSourceFixes`. These govern upstream's local build artifacts and do not belong in a google/fonts override consumed by gftools-builder / fontc_crater. They were removed.

2. **Verified STAT-vs-sources consistency** before settling on the override. The `.glyphs` files at `33c28849` were inspected directly and contain exactly the 9-weight instance lineup declared in the copied STAT: `Grandstander.glyphs` has instances Thin / ExtraLight / Light / Regular / Medium / SemiBold / Bold (isBold) / ExtraBold / Black with `interpolationWeight` 100-900; `Grandstander-Italic.glyphs` has the italic counterparts with the same weight progression. So the STAT values — even though they come from the 2023 upstream config — correctly describe the 2020 source files.

3. **Removed `config_yaml` from METADATA.pb**. `google-fonts-sources` auto-detects the override and records it in `targets.json` as an external config (`config_is_external: true`) on the next regeneration.

**Updated METADATA.pb source block**:
```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Grandstander"
  commit: "33c288495d8ac7bc0b29a9f35801de1df7e6d010"
}
```

## Why Not Bump to HEAD (`0bf9e31d`)

Alternative considered and rejected: change the commit to `0bf9e31d` (2023 upstream HEAD, where `Sources/config.yaml` exists natively — no override needed, picks up upstream's sharp stylistic alternates and expanded character set).

The binaries currently shipped in `ofl/grandstander/` (≈183 KB and ≈185 KB) were built from `33c28849`; upstream's own binaries at `0bf9e31d` are ~8 KB larger per file because of the added content. Bumping the commit without also re-onboarding the binaries would leave the recorded commit out of sync with what is actually shipped, defeating the commit-hash field's purpose. A proper version bump — regenerate binaries via gftools-packager at `0bf9e31d`, QA, designer sign-off — is a separate PR.

## Confidence

**HIGH** — The onboarding commit is preserved and matches the shipped binaries. The override's sources point only at files that exist at that commit. STAT values were taken from upstream's later config but verified against the actual instance lineup in the 2020 `.glyphs` files (9 weights, identical names and `interpolationWeight` values in both the roman and italic files), so the STAT is consistent with what gftools-builder will produce from those sources. Upstream improvements after 2020 (stylistic alternates, expanded character set) remain un-onboarded and would require a separate version-bump PR.
