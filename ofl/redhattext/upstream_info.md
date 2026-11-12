# Investigation Report: Red Hat Text

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Red Hat Text |
| **Status** | complete |
| **Repository URL** | https://github.com/RedHatOfficial/RedHatFont |
| **Commit Hash** | `32287097803f6c58136b60bc7a4a594a7fcbd689` |
| **Config YAML** | `source/Proportional/RedHatText/config.yaml` |
| **Confidence** | MEDIUM |

## Current State in google/fonts

The METADATA.pb at `ofl/redhattext/METADATA.pb` has:
```
source {
  repository_url: "https://github.com/bghryct/RedHatText"
  commit: "dfbc50b16e27d5be1986c3ec79534460a74c1370"
  files { ... }
  branch: "main"
}
```

The URL `https://github.com/bghryct/RedHatText` returns **HTTP 404** — the repository has been deleted.

## How the Correct URL Was Found

See the [Red Hat Display investigation](red-hat-display.md) for the full repository history. All three Red Hat families share the same upstream repo `https://github.com/RedHatOfficial/RedHatFont`.

The bghryct per-family repos were created by Mirko Velimirovic for the Version 1.030 update, then merged back into RedHatOfficial/RedHatFont via PR #69 on 2025-03-06.

## How the Commit Hash Was Identified

The original onboarding commit in google/fonts (PR #8501, merged 2024-11-20):
```
commit 5586f40517c878eae7b9bdf37257a0fa69c3f653
Author: Emma Marichal
Date: 2024-11-15

    Red Hat Text: Version 1.030 added

    Taken from the upstream repo https://github.com/bghryct/RedHatText at commit
    https://github.com/bghryct/RedHatText/commit/dfbc50b16e27d5be1986c3ec79534460a74c1370.
```

The original commit `dfbc50b` was in the now-deleted `bghryct/RedHatText` repo and does **not exist** in `RedHatOfficial/RedHatFont`. The equivalent content is at commit `32287097803f6c58136b60bc7a4a594a7fcbd689` (merge of PR #69 from bghryct/master, tagged `4.1.0`).

### Why MEDIUM Confidence

Same reasoning as Red Hat Display — the original bghryct commit hashes are unverifiable since the repos are deleted. Commit `3228709` is the merge that incorporated the equivalent content.

## Verification

### Config YAML
`source/Proportional/RedHatText/config.yaml` exists at commit `3228709`:
```yaml
sources:
  - RedHatText.glyphs
  - RedHatText-Italic.glyphs
familyName: "Red Hat Text"
buildOTF: true
```

Source files: `source/Proportional/RedHatText/RedHatText.glyphs` and `RedHatText-Italic.glyphs`

### Font File Paths
In RedHatOfficial/RedHatFont at commit `3228709`:
- `fonts/Proportional/RedHatText/variable/RedHatText[wght].ttf`
- `fonts/Proportional/RedHatText/variable/RedHatText-Italic[wght].ttf`

Note: The old bghryct repo used `fonts/variable/` (flat), while the RedHatOfficial repo uses `fonts/Proportional/RedHatText/variable/` (organized by family).

### URL Verification
- `https://github.com/bghryct/RedHatText` → HTTP 404 (deleted)
- `https://github.com/RedHatOfficial/RedHatFont` → HTTP 200 (active)

### Branch
The repo uses `master` (not `main`).

## What Needs to Change

In `ofl/redhattext/METADATA.pb`, the source block should be updated:
1. Fix `repository_url` from `bghryct/RedHatText` to `RedHatOfficial/RedHatFont`
2. Update `commit` from `dfbc50b...` to `32287097803f6c58136b60bc7a4a594a7fcbd689`
3. Add `config_yaml: "source/Proportional/RedHatText/config.yaml"`
4. Update `source_file` paths from `fonts/variable/` to `fonts/Proportional/RedHatText/variable/`
5. Change `branch` from `main` to `master`
