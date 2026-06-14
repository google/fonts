# Investigation Report: Exo

## Family Overview
- **Family name**: Exo
- **Designer**: Natanael Gama, Robin Mientjes
- **License**: OFL
- **Date added to Google Fonts**: 2012-02-08
- **Category**: Sans Serif
- **Subsets**: latin, latin-ext, menu, vietnamese
- **Variable axes**: wght (100-900)
- **Files**: Exo[wght].ttf, Exo-Italic[wght].ttf

## Source Repository
- **Repository URL**: https://github.com/NDISCOVER/Exo-1.0
- **Status**: Valid and accessible
- **Cached at**: upstream_repos/fontc_crater_cache/NDISCOVER/Exo-1.0

## METADATA.pb Source Block (Current)
```
source {
  repository_url: "https://github.com/NDISCOVER/Exo-1.0"
  commit: "3be4f55b626129f17a3b82677703e48c03dc2052"
  config_yaml: "sources/config.yaml"
}
```

## Source Files
- **Format**: UFO + Designspace
- **Designspaces**: `sources/Exo.designspace`, `sources/Exo-Italic.designspace`
- **UFO masters**:
  - `sources/Exo-Thin.ufo`
  - `sources/Exo-Black.ufo`
  - `sources/Exo-ThinItalic.ufo`
  - `sources/Exo-BlackItalic.ufo`
- **Config**: `sources/config.yaml` (gftools-builder config with STAT table definitions)

## Config.yaml Details
The upstream config at `sources/config.yaml` specifies:
- Two designspace sources: Exo.designspace and Exo-Italic.designspace
- Axis order: wght, ital
- Family name: "Exo"
- STAT table entries for both Exo[wght].ttf and Exo-Italic[wght].ttf

## Commit Hash Verification

### Commit in METADATA.pb: `3be4f55b626129f17a3b82677703e48c03dc2052`
- **Message**: "Merge pull request #14 from aaronbell/master"
- **Author**: NDISCOVER
- **Date**: 2021-08-26
- **Description**: This is the HEAD (and only) commit on the default branch. It merges Aaron Bell's PR #14 which converted the repo to UFR (Unified Font Repository) format.

### History of Font Updates in google/fonts

1. **Initial addition** (2012-02-08): Exo was first added to Google Fonts as static fonts.

2. **v1.500** (commit `7e288cf7b`, 2017-07-26, by Marc Foley): Static fonts re-added after a revert, fixing fsSelection bits and OS/2 weightClass values. Referenced upstream PR #3.

3. **v2.000** (commit `6c9cb21c9`, 2020-04-06, by Marc Foley): Variable font version added. Commit message states: "Taken from the upstream repo https://github.com/NDISCOVER/Exo-1.0 at commit https://github.com/NDISCOVER/Exo-1.0/pull/6/commits/64880ddaec76e6de64001291d5450d451a7020e0". This replaced static fonts with variable font files (Exo[wght].ttf and Exo-Italic[wght].ttf). Commit `64880dda` in the upstream repo is "Fix to /ffl and /germandbls.smcp" by Jill Pichotta (2020-03-22), which was the tip of PR #6 from TypeNetwork.

4. **v2.001 / STAT fix** (commit `6fba670af`, 2021-08-27, by Aaron Bell, google/fonts PR #3635): Font files rebuilt with UFR format conversion. PR body: "Font repro updated to the UFR format (https://github.com/aaronbell/Exo-1.0). PR'd to upstream. Font files rebuilt." This corresponds to upstream PR #14 from aaronbell, merged on 2021-08-26 as commit `3be4f55`. The google/fonts merge happened the very next day (2021-08-27).

5. **Source block added** (commit `2423d2aef`, 2023-12-14, by Simon Cozens): Added initial `source { repository_url }` block.

6. **Commit and config_yaml added** (commit `19cdcec59`, 2025-03-31, by Felipe Sanches): Batch port from fontc_crater targets list added `commit` and `config_yaml` fields to the source block.

### Verification of Commit Hash

The commit hash `3be4f55b626129f17a3b82677703e48c03dc2052` in METADATA.pb is **correct**. This is verified by:

1. **It is the HEAD of the upstream repo** -- the only commit on the default branch after squash-merging PR #14.
2. **Timeline alignment**: The upstream PR #14 was merged on 2021-08-26, and the google/fonts PR #3635 was merged on 2021-08-27 -- the very next day, confirming Aaron Bell rebuilt fonts from this exact state.
3. **PR #3635 body** explicitly references the upstream repo and states fonts were rebuilt from the UFR-converted version.
4. **No subsequent commits** exist in the upstream repo after this merge, so this is unambiguously the correct commit.

Note: The earlier v2.000 onboarding used commit `64880dda` (PR #6 tip), but the v2.001 update rebuilt everything from the later PR #14 state (`3be4f55`), making the current METADATA.pb reference correct.

## Note on Exo vs Exo 2

There are two distinct font families:
- **Exo** (this family) at `ofl/exo/` -- upstream repo: NDISCOVER/Exo-1.0
- **Exo 2** at `ofl/exo2/` -- a separate redesign with its own upstream repo

This investigation covers only "Exo" (the original).

## Conclusion

- **Status**: Complete
- **Confidence**: HIGH
- **Repository URL**: https://github.com/NDISCOVER/Exo-1.0 (verified)
- **Commit**: `3be4f55b626129f17a3b82677703e48c03dc2052` (verified -- HEAD of repo, matches the v2.001 update in google/fonts PR #3635)
- **Config**: `sources/config.yaml` (exists in upstream repo at the referenced commit)
- **Override config needed**: No (upstream has a valid config.yaml)

All three fields in the METADATA.pb source block (repository_url, commit, config_yaml) are correct and verified. No changes needed.
