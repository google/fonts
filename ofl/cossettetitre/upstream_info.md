# Cossette Titre - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cossette Titre |
| Repository URL | https://github.com/googlefonts/cossette-fonts |
| Commit Hash | ee99cea3c23039e31865c3c37bd7d716278e546b |
| Branch | main |
| Config YAML | sources/config-titre.yaml |
| Designer | Cossette |
| License | OFL |
| Date Added | 2025-07-29 |

## How URL Found

The repository URL `https://github.com/googlefonts/cossette-fonts` is documented in the METADATA.pb `source {}` block. This is a shared repository that contains both Cossette Texte and Cossette Titre font families. The copyright strings in the font entries also reference this repository.

## How Commit Determined

The commit hash `ee99cea3c23039e31865c3c37bd7d716278e546b` is explicitly stated in the google/fonts commit message (98a7dc08b, authored by Marc Foley on 2025-09-30):

> "Taken from the upstream repo https://github.com/googlefonts/cossette-fonts at commit https://github.com/googlefonts/cossette-fonts/commit/ee99cea3c23039e31865c3c37bd7d716278e546b."

This is the same commit used for Cossette Texte, which makes sense as both families share the same repository. The commit is HEAD (and the only commit) of the upstream repository.

## Config YAML Status

The config file `sources/config-titre.yaml` exists in the upstream repository at the referenced commit. It contains:

```yaml
familyName: Cossette Titre
sources:
  - CossetteTitre-Regular.ufo
  - CossetteTitre-Bold.ufo
buildVariable: false
includeSourceFixes: true
```

This is a valid gftools-builder configuration pointing to UFO sources.

## Verification

- **Repository accessible**: Yes - cloned at `upstream_repos/fontc_crater_cache/googlefonts/cossette-fonts/`
- **Commit exists**: Yes - `ee99cea` is HEAD (and only commit) of the repo
- **Config exists at commit**: Yes - `sources/config-titre.yaml` is present
- **Source files present**: Yes - UFO sources for Regular and Bold weights
- **Font files match**: Binary .ttf files are mapped via `files {}` entries in METADATA.pb

## Confidence Level

**HIGH** - All data is fully documented in the METADATA.pb source block and confirmed by the google/fonts commit message. The upstream repo has only one commit, making verification trivial.

## Open Questions

None.

## Recent upstream/main activity (post-investigation)

- **2025-08-06** — Marc Foley, commit [`a5cda7bc1`](https://github.com/google/fonts/commit/a5cda7bc1) ("Cossette Titre: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added"): initial v1.001 onboarding via gftools-packager from `m4rc1e/cossette-fonts@7a3a7d62f4eac78d1ac722d25def17c67d9bb445` (Marc's fork).
- **2025-08-06** — Emma Marichal, commit [`ead3c04c6`](https://github.com/google/fonts/commit/ead3c04c6) ("Update METADATA.pb"): same-day metadata fix.
- **2025-09-16** — Dave Crossland, commit [`e1d8333ee`](https://github.com/google/fonts/commit/e1d8333ee) ("Update Cossette repo and articles"): migrated `repository_url` from `cossette/cossette-fonts` to `googlefonts/cossette-fonts`. Same commit affected the sibling `cossettetexte` family.
