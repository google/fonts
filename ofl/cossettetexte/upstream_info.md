# Cossette Texte - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cossette Texte |
| Repository URL | https://github.com/googlefonts/cossette-fonts |
| Commit Hash | ee99cea3c23039e31865c3c37bd7d716278e546b |
| Branch | main |
| Config YAML | sources/config-texte.yaml |
| Designer | Cossette |
| License | OFL |
| Date Added | 2025-07-29 |

## How URL Found

The repository URL `https://github.com/googlefonts/cossette-fonts` is documented directly in the METADATA.pb `source {}` block added when the font was onboarded. The copyright strings in the font entries also reference this repository URL.

## How Commit Determined

The commit hash `ee99cea3c23039e31865c3c37bd7d716278e546b` is explicitly stated in the google/fonts commit message (ca5e6235b, authored by Marc Foley on 2025-09-30):

> "Taken from the upstream repo https://github.com/googlefonts/cossette-fonts at commit https://github.com/googlefonts/cossette-fonts/commit/ee99cea3c23039e31865c3c37bd7d716278e546b."

This commit is also the only commit (HEAD) of the upstream repository ("Merge pull request #2 from googlefonts/url"). The upstream repo has only a single commit.

## Config YAML Status

The config file `sources/config-texte.yaml` exists in the upstream repository at the referenced commit. It contains:

```yaml
familyName: Cossette Texte
sources:
  - CossetteTexte-Regular.ufo
  - CossetteTexte-Bold.ufo
buildVariable: false
includeSourceFixes: true
```

This is a valid gftools-builder configuration pointing to UFO sources.

## Verification

- **Repository accessible**: Yes - cloned at `upstream_repos/fontc_crater_cache/googlefonts/cossette-fonts/`
- **Commit exists**: Yes - `ee99cea` is HEAD (and only commit) of the repo
- **Config exists at commit**: Yes - `sources/config-texte.yaml` is present
- **Source files present**: Yes - UFO sources for Regular and Bold weights
- **Font files match**: Binary .ttf files are mapped via `files {}` entries in METADATA.pb

## Confidence Level

**HIGH** - All data is fully documented in the METADATA.pb source block and confirmed by the google/fonts commit message. The upstream repo has only one commit, making verification trivial.

## Open Questions

None.
