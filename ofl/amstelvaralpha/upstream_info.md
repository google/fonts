# Amstelvar Alpha

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: needs_investigation
**Designer**: David Berlow
**METADATA.pb path**: `ofl/amstelvaralpha/METADATA.pb` (does not exist)

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | `https://github.com/googlefonts/amstelvar` |
| Commit | `b490f475bb83` (last font update before google/fonts PR #1184 merge) |
| Config YAML | -- |
| Branch | main |

## Context

Amstelvar Alpha is an **Early Access** family in google/fonts. It has an `EARLY_ACCESS.category` file but **no METADATA.pb** file at all. The family was never fully promoted to the Google Fonts catalog. The directory contains only:

- `AmstelvarAlpha-VF.ttf` (128,312 bytes)
- `DESCRIPTION.en_us.html`
- `EARLY_ACCESS.category` (content: "Serif")
- `OFL.txt`

The upstream repo is archived and the font project has evolved significantly beyond the "Alpha" version that was served through Early Access.

## How the Repository URL Was Found

The `DESCRIPTION.en_us.html` file explicitly links to `https://github.com/TypeNetwork/fb-Amstelvar`. Using the GitHub API, this URL now redirects to `https://github.com/googlefonts/amstelvar` (the repo was transferred from the TypeNetwork organization to googlefonts). The repo is currently **archived**.

The upstream repo's `METADATA.yml` also confirms: `repository url: https://github.com/typenetwork/Amstelvar`.

## How the Commit Hash Was Identified

The google/fonts history for `ofl/amstelvaralpha/` shows exactly 4 commits:

1. `d95e5ec65` -- "Add Amstelvar to Early Access (#655)" -- merged 2017-03-28 by davelab6
2. `c0899f11c` -- "ofl/amstelvaralpha/AmstelvarAlpha-VF.ttf Updated" (squash of PR #1184)
3. `0eb39d391` -- "ofl/amstelvaralpha/AmstelvarAlpha-VF.ttf Updated (#1184)" -- merged 2017-08-30 by davelab6
4. `6bda16478` -- "Format HTML with new html formatter" (only touched DESCRIPTION.en_us.html)

**Initial onboarding (PR #655)**: The font binary had git blob SHA `fec678154d` and size 106,184 bytes. This exactly matches the `fonts/AmstelvarAlpha-VF.ttf` file at upstream commit `2357d7bf4d51` (2017-03-27, "Delete AmstelvarAlpha-VF-2017-01-23.ttf"). The font file was a pre-compiled binary checked into the upstream repo, not built via any CI/config pipeline.

**Update (PR #1184)**: The font binary was updated to blob SHA `11da618ab4` and size 128,312 bytes. This exactly matches `fonts/AmstelvarAlpha-VF.ttf` at upstream commit `b490f475bb83` (2017-08-10, "build default version without dollar point jump"). This was the last commit to touch the font file before the google/fonts merge on 2017-08-30.

Both blob SHA and file size matches are exact, providing high confidence in the commit identification.

## How Config YAML Was Resolved

There is **no `config.yaml`** anywhere in the upstream repository (neither at the onboarding-era commits nor at the current HEAD). The font was built using a custom `fontmake` + `fonttools varLib` pipeline via a shell script (`scripts/build.sh`):

```bash
fontmake -o ttf-interpolatable -m AmstelvarAlpha.designspace --no-production-names
fonttools varLib AmstelvarAlpha.designspace
mv AmstelvarAlpha-VF.ttf ../fonts/AmstelvarAlpha-VF.ttf
```

The sources at the onboarding commit (`2357d7bf4d51`) were UFO files organized in two directories:
- `sources/1-drawing/` -- 26 `.ufo` masters plus `AmstelvarAlpha.designspace` and `AmstelvarAlpha.fea`
- `sources/2-build/` -- 29 `.ufo` masters plus `AmstelvarAlpha.fea`

At the update commit (`b490f475bb83`), the structure had evolved to include a `sources/BETA/` directory with additional axis combinations.

The project uses `.designspace` + `.ufo` sources, which are theoretically compatible with gftools-builder, but the build process was custom and predates gftools-builder entirely (2017). An override `config.yaml` could potentially be created, but given the complexity of the designspace (many parametric axes) and the fact that the project has evolved far beyond this alpha version, it may not be practical.

## Conclusion

Amstelvar Alpha is an **Early Access** family with no METADATA.pb. The upstream repository is `https://github.com/googlefonts/amstelvar` (archived, formerly `TypeNetwork/fb-Amstelvar`). The font binary currently in google/fonts was taken from upstream commit `b490f475bb83` (2017-08-10), confirmed by exact blob SHA match.

Key considerations:
- **No METADATA.pb exists** -- this is an Early Access family that was never fully onboarded to the catalog
- **No config.yaml** -- the font was built with custom fontmake scripts, not gftools-builder
- **Repo is archived** -- the upstream repository has been archived and is no longer actively developed
- **Pre-compiled binary** -- the font was checked into the upstream repo as a pre-built binary, not generated through a reproducible build pipeline
- The repo has since evolved to a non-Alpha version ("Amstelvar" proper) with significantly different sources and more refined designspaces, but this newer version has not been pushed to google/fonts

Creating a source block would require first creating a METADATA.pb for this family. Given the Early Access status and archived upstream, this family may be a candidate for delisting rather than full metadata enrichment.
