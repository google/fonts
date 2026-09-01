# Comme - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Comme |
| Designer | Vernon Adams |
| Repository URL | https://github.com/googlefonts/comme |
| Commit | `45a6e22afc31eb55a46c9b4da4a25ed374886ebf` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| Override Config | No |
| Date Added | 2023-03-29 |
| License | OFL |

## How URL Found

The repository URL `https://github.com/googlefonts/comme` was included in the METADATA.pb from the initial onboarding. The `upstream.yaml` file created during onboarding contained the URL, which was later merged into METADATA.pb by Simon Cozens (commit `66f91f10f`, April 2024). The URL is also referenced in the copyright string.

## How Commit Determined

The commit hash `45a6e22afc31eb55a46c9b4da4a25ed374886ebf` is explicitly stated in the onboarding commit message:

> "Comme Version 1.000;gftools[0.9.27] taken from the upstream repo https://github.com/googlefonts/comme at commit https://github.com/googlefonts/comme/commit/45a6e22afc31eb55a46c9b4da4a25ed374886ebf."

This was the onboarding by Emma Marichal (bonjour@emmamarichal.fr), committed on 2023-03-29 (commit `d17bdcb1d`).

The upstream repository has only a single commit ("Added Germandbls"), and this commit is the HEAD of the `main` branch. This makes verification completely unambiguous.

## Config YAML Status

The upstream repository has `sources/config.yaml` at the only commit:

```yaml
sources:
  - Comme.glyphs
axisOrder:
  - wght
familyName: "Comme"
stat:
  Comme[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Thin
      value: 100
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
    - name: Black
      value: 900
```

This is a variable font with a weight axis (100-900), and the config includes full STAT table definitions.

## Verification

- **Commit exists in upstream**: Yes - it is the only commit and HEAD of `main` branch
- **Branch matches**: Yes - `main` branch, matches METADATA.pb
- **Config YAML exists at commit**: Yes - `sources/config.yaml` exists
- **Font files match**: The variable font `Comme[wght].ttf` is produced from `Comme.glyphs` source
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/googlefonts/comme/`

## Confidence Level

**HIGH** - All data is fully verified. The onboarding commit message explicitly states the upstream URL and commit hash. The repo has only one commit, eliminating any ambiguity.

## Open Questions

None. All source data is complete and verified.
