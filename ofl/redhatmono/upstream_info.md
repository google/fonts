# Investigation Report: Red Hat Mono

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Red Hat Mono |
| **Status** | complete |
| **Repository URL** | https://github.com/RedHatOfficial/RedHatFont |
| **Commit Hash** | `32287097803f6c58136b60bc7a4a594a7fcbd689` |
| **Config YAML** | `source/Mono/config.yaml` |
| **Confidence** | MEDIUM |

## Current State in google/fonts

The METADATA.pb at `ofl/redhatmono/METADATA.pb` has:
```
source {
  repository_url: "https://github.com/bghryct/RedHatMono"
  commit: "a0f2a7032143500e44dfd569d09ba30414d51a1c"
  files { ... }
  branch: "main"
}
```

The URL `https://github.com/bghryct/RedHatMono` returns **HTTP 404** — the repository has been deleted.

## How the Correct URL Was Found

See the [Red Hat Display investigation](red-hat-display.md) for the full repository history. All three Red Hat families share the same upstream repo `https://github.com/RedHatOfficial/RedHatFont`.

The bghryct per-family repos were created by Mirko Velimirovic for the Version 1.030 update, then merged back into RedHatOfficial/RedHatFont via PR #69 on 2025-03-06.

## How the Commit Hash Was Identified

The original onboarding commit in google/fonts (PR #8502, merged 2024-11-20):
```
commit 988131b4198915eee3df709d1f63abb01b5d1155
Author: Emma Marichal
Date: 2024-11-15

    Red Hat Mono: Version 1.030 added

    Taken from the upstream repo https://github.com/bghryct/RedHatMono at commit
    https://github.com/bghryct/RedHatMono/commit/a0f2a7032143500e44dfd569d09ba30414d51a1c.
```

The original commit `a0f2a70` was in the now-deleted `bghryct/RedHatMono` repo and does **not exist** in `RedHatOfficial/RedHatFont`. The equivalent content is at commit `32287097803f6c58136b60bc7a4a594a7fcbd689` (merge of PR #69 from bghryct/master, tagged `4.1.0`).

### Why MEDIUM Confidence

Same reasoning as Red Hat Display — the original bghryct commit hashes are unverifiable since the repos are deleted. Commit `3228709` is the merge that incorporated the equivalent content.

## Verification

### Config YAML
`source/Mono/config.yaml` exists at commit `3228709`:
```yaml
sources:
  - RedHatMono.glyphs
  - RedHatMono-Italic.glyphs
familyName: "Red Hat Mono"
buildOTF: true
cleanUp: true
stat:
  RedHatMono[wght].ttf:
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
  - name: Italic
    tag: ital
    values:
    - name: Roman
      value: 0
      linkedValue: 1
      flags: 2
  RedHatMono-Italic[wght].ttf:
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
  - name: Italic
    tag: ital
    values:
    - name: Italic
      value: 1
```

Source files: `source/Mono/RedHatMono.glyphs` and `RedHatMono-Italic.glyphs`

### Font File Paths
In RedHatOfficial/RedHatFont at commit `3228709`:
- `fonts/Mono/variable/RedHatMono[wght].ttf`
- `fonts/Mono/variable/RedHatMono-Italic[wght].ttf`

Note: The old bghryct repo used `fonts/variable/` (flat), while the RedHatOfficial repo uses `fonts/Mono/variable/` (organized by family).

### URL Verification
- `https://github.com/bghryct/RedHatMono` → HTTP 404 (deleted)
- `https://github.com/RedHatOfficial/RedHatFont` → HTTP 200 (active)

### Branch
The repo uses `master` (not `main`).

## What Needs to Change

In `ofl/redhatmono/METADATA.pb`, the source block should be updated:
1. Fix `repository_url` from `bghryct/RedHatMono` to `RedHatOfficial/RedHatFont`
2. Update `commit` from `a0f2a70...` to `32287097803f6c58136b60bc7a4a594a7fcbd689`
3. Add `config_yaml: "source/Mono/config.yaml"`
4. Update `source_file` paths from `fonts/variable/` to `fonts/Mono/variable/`
5. Change `branch` from `main` to `master`
