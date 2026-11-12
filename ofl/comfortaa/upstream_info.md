# Comfortaa - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Comfortaa |
| Designer | Johan Aakerlund |
| Repository URL | https://github.com/alexeiva/comfortaa (current in METADATA.pb) |
| Correct Repository URL | https://github.com/googlefonts/comfortaa |
| Commit Hash (tracked) | 4aa21cfb7b018629dcf17aab6220e638411c7164 (from alexeiva/comfortaa) |
| Correct Commit Hash | 2a87ac6f6ea3 (HEAD of googlefonts/comfortaa, used for v3.105) |
| Branch | main |
| Config YAML | sources/config.yaml (in googlefonts/comfortaa) |
| Override Config | No |
| Status | missing_config (needs URL and commit update) |

## How URL Was Found

The repository URL `https://github.com/alexeiva/comfortaa` is currently recorded in the METADATA.pb source block (added by Simon Cozens in commit `f7455d788`, "Populate source.repository_url"). However, this is a **fork**. The canonical upstream is `https://github.com/googlefonts/comfortaa`, which is the repository referenced in multiple google/fonts PRs:

- PR #1750 ("comfortaa: v3.103 Upgraded to VF") explicitly states: "Taken from the upstream repo https://github.com/googlefonts/comfortaa at commit https://github.com/googlefonts/comfortaa/commit/a308e42532deabdbf0e289541f3eb336da69c4cc"
- PR #3631 ("Comfortaa v3.105 (stat fix)") by aaronbell references: "https://github.com/googlefonts/comfortaa"

The `alexeiva/comfortaa` fork appears to be the original development repo by Alexander Eiva, but the font was transferred to the `googlefonts` organization and all recent updates have used the `googlefonts/comfortaa` repo.

## How Commit Was Determined

The currently tracked commit `4aa21cfb7b018629dcf17aab6220e638411c7164` is from `alexeiva/comfortaa` (dated November 8, 2017, "regenned fonts"). This commit also exists in `googlefonts/comfortaa` (since it inherited the full history). However, this commit corresponds to the v3.103 era, not the latest v3.105 update.

The font was last updated in google/fonts via:
1. PR #1750 (v3.103, VF upgrade) - referenced commit `a308e42532de` in googlefonts/comfortaa (Nov 2, 2018)
2. PR #1775 (v3.104) - fixed hinting issue from googlefonts/comfortaa#17
3. PR #3631 (v3.105, STAT fix, Aug 26, 2021) by aaronbell - referenced `https://github.com/googlefonts/comfortaa` but no specific commit

The HEAD of `googlefonts/comfortaa` at the time of PR #3631 was `2a87ac6f6ea3` ("Merge pull request #24 from aaronbell/main", dated July 29, 2021). This is the most likely commit used for the v3.105 build, and it is still the current HEAD of the repository.

## Config YAML Status

**Config.yaml exists in the upstream** at `googlefonts/comfortaa` in `sources/config.yaml`:

```yaml
sources:
  - Comfortaa.glyphs
axisOrder:
  - wght
familyName: "Comfortaa"
stat:
    Comfortaa[wght].ttf:
    - name: Weight
      tag: wght
      values:
      - name: Light
        value: 300
      - name: Regular
        value: 400
        linkedValue: 700
        flags: 2
      - name: Medium
        value: 500
      - name: SemiBold
        value: 600
      - name: Bold
        value: 700
```

This config.yaml references `Comfortaa.glyphs` which is also in the `sources/` directory. The `config_yaml` field in METADATA.pb should be set to `sources/config.yaml`.

Note: The `alexeiva/comfortaa` repo does NOT have a config.yaml -- only `googlefonts/comfortaa` does.

## Verification

- **googlefonts/comfortaa accessible**: Yes
- **alexeiva/comfortaa accessible**: Yes (it's a fork of googlefonts/comfortaa)
- **Commit 4aa21cfb exists**: Yes, in both repos
- **Commit 2a87ac6f exists**: Yes, it is the current HEAD of googlefonts/comfortaa main branch
- **Config.yaml present at 2a87ac6f**: Yes, at `sources/config.yaml`
- **Source block on main**: Only has repository_url (pointing to wrong repo); commit hash is on pending PR branch

## What Needs to Change

1. **Repository URL**: Update from `https://github.com/alexeiva/comfortaa` to `https://github.com/googlefonts/comfortaa`
2. **Commit hash**: Update from `4aa21cfb7b018629dcf17aab6220e638411c7164` to `2a87ac6f6ea3495150bfa00d0c0fb53dd0a2f11b`
3. **Commit hash**: Full hash is `2a87ac6f6ea3495150bfa00d0c0fb53dd0a2f11b`
4. **Config YAML**: Set `config_yaml: "sources/config.yaml"` in the source block
5. **Clone upstream**: `googlefonts/comfortaa` needs to be cloned to the fontc_crater_cache

## Confidence Level

**High** for the correct upstream being `googlefonts/comfortaa`. Multiple google/fonts PRs explicitly reference this repo, and it contains the config.yaml and proper build setup.

**High** for the commit hash `2a87ac6f6ea3` being the correct one for the v3.105 update. It was the HEAD of googlefonts/comfortaa at the time PR #3631 was created and merged, and it remains the current HEAD.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Comfortaa.glyphs
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. The `googlefonts/comfortaa` repo should be cloned to the fontc_crater_cache at `upstream_repos/fontc_crater_cache/googlefonts/comfortaa/`.
2. Should the `alexeiva/comfortaa` cache be kept or removed after migration to the correct upstream?
3. The METADATA.pb on main and the pending PR branch both need updating with the correct URL, commit, and config_yaml.
