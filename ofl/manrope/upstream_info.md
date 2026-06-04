# Investigation Report: Manrope

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Manrope |
| **Status** | complete |
| **Repository URL** | https://github.com/aaronbell/manrope |
| **Commit Hash** | `6f81ebecdf65e4463b798cc07b16a4f8d5216917` |
| **Config YAML** | `sources/config.yaml` |
| **Confidence** | HIGH |

## Current State in google/fonts

The METADATA.pb at `ofl/manrope/METADATA.pb` has:
```
source {
  repository_url: "https://github.com/sharanda/manrope"
}
```

The URL `https://github.com/sharanda/manrope` returns **HTTP 404** — the repository has been deleted.

No commit hash or config_yaml is recorded.

## How the Correct URL Was Found

The font's copyright string references `https://github.com/sharanda/manrope` (the original repo by designer Mikhail Sharanda). After Sharanda's repo was deleted, the active development fork is `https://github.com/aaronbell/manrope`, which returns **HTTP 200**.

Aaron Bell himself authored PR #3642 in google/fonts and explicitly linked to `https://github.com/aaronbell/manrope` in the PR body:
> Font repro updated to the UFR format (https://github.com/aaronbell/manrope). PR'd to upstream. Font files rebuilt.

### Repository Fork Chain

- `sharanda/manrope` — Original repo by Mikhail Sharanda (designer). Now **deleted/404**.
- `davelab6/manrope` — Fork (now the "root" after sharanda deleted theirs).
- `aaronbell/manrope` — Fork of davelab6/manrope. Aaron Bell did the UFR conversion and the google/fonts update. **Active development repo.**

## How the Commit Hash Was Identified

The last commit that modified the font binary in google/fonts:
```
commit 8f9a401dbb3793e0d1264b15d96aa253f05280f5
Author: Aaron <aaronbell@users.noreply.github.com>
Date:   Thu Aug 26 05:54:14 2021 -0700

    Manrope v4.504 (stat fix) (#3642)

    * Updated to UFR, fonts rebuilt
    * stripping statics
```

This was merged on 2021-08-26. The HEAD of `aaronbell/manrope` master branch is commit `6f81ebe` ("Rebuilding Static instances with autohinting", 2021-07-22), which is the latest commit and predates the google/fonts merge.

## Verification

### Binary File Match
SHA256 of `Manrope[wght].ttf`:
- google/fonts: `d0639be45d0af36e798172419d7bd173c4bd4f29e2b76cbb69db1d11bf8b0a40`
- aaronbell/manrope at 6f81ebe (`fonts/variable/`): `d0639be45d0af36e798172419d7bd173c4bd4f29e2b76cbb69db1d11bf8b0a40`

**Byte-identical match.** This confirms `6f81ebe` is the exact commit used for onboarding.

### Config YAML
The file `sources/config.yaml` exists at commit `6f81ebe`:
```yaml
sources:
  - Manrope.glyphs
axisOrder:
  - wght
familyName: Manrope
stat:
  Manrope[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: ExtraLight
      value: 200
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
    - name: ExtraBold
      value: 800
```

Source file: `sources/Manrope.glyphs`

### URL Verification
- `https://github.com/sharanda/manrope` → HTTP 404 (deleted)
- `https://github.com/aaronbell/manrope` → HTTP 200 (active)

## What Needs to Change

In `ofl/manrope/METADATA.pb`, the source block should be updated:
1. Fix `repository_url` from `sharanda/manrope` to `aaronbell/manrope`
2. Add `commit: "6f81ebecdf65e4463b798cc07b16a4f8d5216917"`
3. Add `config_yaml: "sources/config.yaml"`

## How the Wrong URL Got There

The `source { repository_url: "https://github.com/sharanda/manrope" }` block was added by Simon Cozens in commit `6392e4f` ("Update upstreams", 2023-12-14), likely from a bulk automated update that pulled the URL from the font's copyright string.
