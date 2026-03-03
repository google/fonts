# Anek Devanagari

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/anekdevanagari/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/EkType/Anek |
| Commit | `34074c6b406f4112e20c7ad10254a6e954d0324b` |
| Config YAML | `sources/AnekDevanagari/builder.yaml` |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/EkType/Anek` is already recorded in the METADATA.pb `source` block. It is also confirmed by the copyright string in the font metadata: "Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)". The gftools-packager commit message in google/fonts (`ac1371ad5`) explicitly states the font was "taken from the upstream repo https://github.com/EkType/Anek". The cached repo at `EkType/Anek` confirms the remote matches.

## How the Commit Hash Was Identified

The commit hash `34074c6b406f4112e20c7ad10254a6e954d0324b` is recorded in the METADATA.pb `source` block and matches the gftools-packager commit message for PR #4305:

> "Anek Devanagari Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b."

This commit is "Merge pull request #3 from yanone/main" dated 2022-02-14, which is on the `main` branch. It was the latest commit at the time of the google/fonts merge on 2022-02-18.

### Onboarding history

There were two onboarding attempts:

1. **PR #4276** (commit `eed6654ae`, earlier attempt): Referenced upstream commit `634384ab` (2022-02-09, "Merge pull request #2 from yanone/main"). The source block was removed during this PR.
2. **PR #4305** (commit `ac1371ad5`, merged 2022-02-18): The final onboarding, referencing the newer upstream commit `34074c6b` (2022-02-14, "Merge pull request #3 from yanone/main"). The source metadata was added via commit `7d9f2e35d` which references PR #4305.

The recorded commit `34074c6b` is correct and corresponds to the final onboarding.

## How Config YAML Was Resolved

The config path `sources/AnekDevanagari/builder.yaml` is recorded in the METADATA.pb `source` block. Verified at commit `34074c6b`:

- The file `sources/AnekDevanagari/builder.yaml` exists
- Its contents reference `Masters/AnekDevanagari.designspace` as the source
- The designspace file and 9 UFO masters are present in `sources/AnekDevanagari/Masters/`
- Build settings: variable TTF only (no static, no OTF, no webfont), with `includeSourceFixes: true`

The `files` mapping in the source block correctly maps the built output:
- `fonts/AnekDevanagari/variable/AnekDevanagari[wdth,wght].ttf` -> `AnekDevanagari[wdth,wght].ttf`
- `OFL.txt` -> `OFL.txt`
- `DESCRIPTION.en_us.html` -> `DESCRIPTION.en_us.html`

No override config.yaml exists in the google/fonts family directory.

## Conclusion

The source block for Anek Devanagari is complete and accurate. The repository URL, commit hash, config YAML path, and branch are all correct and verified. This is one of several script-specific variants in the EkType/Anek mono-repo, each with its own builder.yaml and designspace under `sources/Anek{Script}/`. No changes needed.
