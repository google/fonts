# Investigation Report: Red Hat Display

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Red Hat Display |
| **Status** | complete |
| **Repository URL** | https://github.com/RedHatOfficial/RedHatFont |
| **Commit Hash** | `32287097803f6c58136b60bc7a4a594a7fcbd689` |
| **Config YAML** | `source/Proportional/RedHatDisplay/config.yaml` |
| **Confidence** | MEDIUM |

## Current State in google/fonts

The METADATA.pb at `ofl/redhatdisplay/METADATA.pb` has:
```
source {
  repository_url: "https://github.com/bghryct/RedHatDisplay"
  commit: "fd36df3a3ad95084fe777597ed4b5c19961b3631"
  files { ... }
  branch: "main"
}
```

The URL `https://github.com/bghryct/RedHatDisplay` returns **HTTP 404** — the repository has been deleted. The bghryct GitHub account (Mirko Velimirovic / Abyss Type Company) still exists with 121 public repos, but the three Red Hat per-family repos have been removed.

## How the Correct URL Was Found

The Red Hat font family has a complex repository history:

1. **RedHatOfficial/RedHatFont** — The original official repo, maintained since 2019. Contains all three families (Display, Mono, Text).
2. **jeremymickel/RedHatFonts** — Used for the Version 1.023 update (google/fonts PRs #4946, #4945, #4947 in 2022).
3. **bghryct/RedHatDisplay** (and /RedHatMono, /RedHatText) — Per-family repos created by Mirko Velimirovic for the Version 1.030 update. Now deleted.
4. **RedHatOfficial/RedHatFont PR #69** — On 2025-03-06, the bghryct changes were merged back into RedHatOfficial/RedHatFont via this PR.

The canonical, surviving repository is `https://github.com/RedHatOfficial/RedHatFont` (HTTP 200).

## How the Commit Hash Was Identified

The original onboarding commit in google/fonts (PR #8500, merged 2024-11-20):
```
commit 105f8a8f7b4a7a48cf21cd39bb11a2d14f920fd6
Author: Emma Marichal
Date: 2024-11-15

    Red Hat Display: Version 1.030 added

    Taken from the upstream repo https://github.com/bghryct/RedHatDisplay at commit
    https://github.com/bghryct/RedHatDisplay/commit/fd36df3a3ad95084fe777597ed4b5c19961b3631.
```

The original commit `fd36df3` was in the now-deleted `bghryct/RedHatDisplay` repo and does **not exist** in `RedHatOfficial/RedHatFont`. However, the same content was merged into RedHatOfficial/RedHatFont on 2025-03-06 via PR #69 (from bghryct/master):

```
commit 32287097803f6c58136b60bc7a4a594a7fcbd689
Author: Zack Hawkins
Date: Thu Mar 6 11:40:44 2025 -0500

    Merge pull request #69 from bghryct/master

    Update Red Hat Font sources
```

This is tagged as `4.1.0`. The merge brought in two commits by Mirko Velimirovic (bghryct) from 2024-11-26 containing the new fonts and build instructions.

### Why MEDIUM Confidence

The original bghryct commit hashes are unverifiable since the repos are deleted. Commit `3228709` is the merge commit that incorporated the equivalent content into RedHatOfficial/RedHatFont. The binary files at this commit should match what was onboarded, but the exact original hashes cannot be cross-referenced.

## Verification

### Config YAML
`source/Proportional/RedHatDisplay/config.yaml` exists at commit `3228709`:
```yaml
sources:
  - RedHatDisplay.glyphs
  - RedHatDisplay-Italic.glyphs
familyName: "Red Hat Display"
cleanUp: true
buildOTF: true
```

Source files: `source/Proportional/RedHatDisplay/RedHatDisplay.glyphs` and `RedHatDisplay-Italic.glyphs`

### Font File Paths
In RedHatOfficial/RedHatFont at commit `3228709`:
- `fonts/Proportional/RedHatDisplay/variable/RedHatDisplay[wght].ttf`
- `fonts/Proportional/RedHatDisplay/variable/RedHatDisplay-Italic[wght].ttf`

Note: The old bghryct repo used `fonts/variable/` (flat), while the RedHatOfficial repo uses `fonts/Proportional/RedHatDisplay/variable/` (organized by family).

### URL Verification
- `https://github.com/bghryct/RedHatDisplay` → HTTP 404 (deleted)
- `https://github.com/RedHatOfficial/RedHatFont` → HTTP 200 (active)

### Branch
The repo uses `master` (not `main`).

## What Needs to Change

In `ofl/redhatdisplay/METADATA.pb`, the source block should be updated:
1. Fix `repository_url` from `bghryct/RedHatDisplay` to `RedHatOfficial/RedHatFont`
2. Update `commit` from `fd36df3...` to `32287097803f6c58136b60bc7a4a594a7fcbd689`
3. Add `config_yaml: "source/Proportional/RedHatDisplay/config.yaml"`
4. Update `source_file` paths from `fonts/variable/` to `fonts/Proportional/RedHatDisplay/variable/`
5. Change `branch` from `main` to `master`
