# Investigation Report: BioRhyme Expanded

## Source Data

| Field | Value |
|-------|-------|
| Family Name | BioRhyme Expanded |
| Designer | Aoife Mooney |
| License | OFL |
| Repository URL | https://github.com/aoifemooney/makingbiorhyme |
| Commit | `b3c0488559ad7c42e11b71e65d255344faff63b9` |
| Branch | gh-pages |
| Config YAML | `sources/config.yaml` |
| Date Added | 2016-06-20 |
| Status | Complete |

## How URL Found

BioRhyme Expanded shares the same upstream repository as BioRhyme: `https://github.com/aoifemooney/makingbiorhyme`. The upstream repo originally included both normal-width and expanded-width font files. The copyright in METADATA.pb references "Aoife Mooney (aoifemooney@gmail.com www.aoifemooney.org)". The repository URL was added by Simon Cozens in the "Add more upstreams" commit and later confirmed in our project's source metadata additions.

## How Commit Determined

The commit hash `b3c0488559ad7c42e11b71e65d255344faff63b9` is the same commit used for BioRhyme proper. This is the HEAD (and only visible commit) on the `gh-pages` branch of the upstream repo. Since the repo history was squashed, this is the only commit we can reference.

### Important context

BioRhyme Expanded was never updated via gftools-packager. The static fonts currently in google/fonts date from the 2017 hotfix (commit `57523b5f6`, PR #983 by Marc Foley). The upstream repo's `old/Releases/2016_05_29/TTFS/` directory contains the original BioRhymeExpanded static fonts, confirming this is the correct upstream repo.

However, the current config.yaml in the upstream repo builds only the variable font `BioRhyme[wdth,wght].ttf` which includes the Expanded width range (wdth axis 100-125). The BioRhyme Expanded family in google/fonts represents the legacy static font version that has been functionally superseded by the BioRhyme variable font's width axis.

## Config YAML Status

**Found in upstream at `sources/config.yaml`**

The config.yaml at commit `b3c0488` builds a variable BioRhyme font with a width axis (100-125) that encompasses the Expanded width. It does not build separate BioRhymeExpanded static fonts. This means:

- The config.yaml is correct for the BioRhyme variable font
- BioRhyme Expanded's static fonts predate this config and were likely compiled manually or with older tooling
- The Expanded width range is now covered by the variable font's wdth axis

## METADATA.pb Source Block Status

The METADATA.pb in google/fonts HEAD does **not** have a source block. Our project added one via commit `4fd9e2392` ("Add source metadata to 125 METADATA.pb files"), but this change has not yet been merged into google/fonts upstream. The source block we added contains the repository_url, commit hash, and config_yaml path.

## History

1. **2016-06-20**: BioRhyme Expanded originally added to google/fonts (date_added)
2. **2017-05-23**: Static fonts added via hotfix (commit `57523b5f6`, PR #983 by Marc Foley), adding 5 static weight instances
3. **2023-09-20**: The sibling family BioRhyme was upgraded to a variable font with wdth+wght axes, effectively superseding BioRhyme Expanded
4. **2023-11-14**: Stroke and classification metadata added (commit `1db714082`)

## Verification

- [x] Repository URL is valid and accessible
- [x] Commit hash exists in upstream repo (HEAD of gh-pages)
- [x] Config.yaml exists at `sources/config.yaml` at the recorded commit
- [x] Upstream repo contains BioRhyme Expanded static fonts in `old/Releases/` directory
- [ ] Source block not yet in google/fonts METADATA.pb (pending PR)

## Confidence Level

**High** -- The repository URL and commit are correct. The upstream repo is confirmed to contain BioRhyme Expanded source files. The config.yaml builds the variable font that supersedes this family.

## Open Questions

1. Will BioRhyme Expanded eventually be deprecated/removed from google/fonts in favor of the BioRhyme variable font's width axis?
2. Should a separate config.yaml be created specifically for building BioRhyme Expanded static fonts, or is the current variable-only config sufficient?
