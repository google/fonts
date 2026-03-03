# Investigation Report: Bitcount Grid Single Ink

**Family slug:** bitcountgridsingleink
**Family directory:** `ofl/bitcountgridsingleink`
**Date:** 2026-03-03
**Model:** Claude Opus 4.6

## Summary

| Field | Value |
|---|---|
| **Repository URL** | https://github.com/petrvanblokland/TYPETR-Bitcount |
| **Commit** | `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` |
| **Config** | Override `config.yaml` in google/fonts (local) |
| **Status** | Complete |
| **Confidence** | HIGH |

## METADATA.pb Source Block

The METADATA.pb already contains a complete source block:

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "89e7994f73b7f5ced80e7cf493d40be9e66ff82f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
}
```

No `config_yaml` field is set, which is correct because an override config.yaml exists locally in the google/fonts family directory.

## Repository Verification

- **Remote URL:** https://github.com/petrvanblokland/TYPETR-Bitcount (confirmed via `git remote -v`)
- **Cached at:** `upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount`
- **Repo is clean:** Yes (no local modifications)

## Commit Verification

The referenced commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` was verified:

- **Author:** Simon Cozens (simon@simon-cozens.org)
- **Date:** Fri Sep 5 10:53:08 2025 +0100
- **Message:** "Merge pull request #37 from petrvanblokland/fix-ligatures"
- **This is the latest commit in the repo** (HEAD of main). No newer commits exist after it.

### Binary File Match

The font binary at the referenced commit matches exactly what is in google/fonts:

| Location | Size | SHA256 |
|---|---|---|
| Upstream @ `89e7994` | 276,416 bytes | `278c3a8da7298e23b9e93289c6a4efa9d92797aeb7d18f445d93dc0f3c08bb82` |
| google/fonts | 276,416 bytes | `278c3a8da7298e23b9e93289c6a4efa9d92797aeb7d18f445d93dc0f3c08bb82` |

Identical SHA256 hashes confirm the binary was taken directly from this commit.

## Onboarding History

This family was onboarded in two stages:

1. **Version 1.0 (Jan 2025):** Committed by Yanone (post@yanone.de) on 2025-01-17, referencing upstream commit `af0818ea`. This resolved issue #5468.
2. **Version 1.001 (Sep 2025):** Committed by Emma Marichal (bonjour@emmamarichal.fr) on 2025-09-05, referencing upstream commit `89e7994f`. Merged via PR #8962 (`gftools_packager_ofl_bitcountgridsingleink`).

The current binary and METADATA.pb reflect the Version 1.001 update from PR #8962.

## Source Files

The upstream repo at commit `89e7994` contains:

- **Designspace:** `sources/Bitcount_Template.designspace` -- a shared template designspace for the entire Bitcount family
- **UFO sources:** `sources/ufo/` -- contains multiple UFO directories for different element layers
- **Pre-built binaries:** `fonts/ttf/variable/` -- contains pre-compiled variable TTFs for all Bitcount variants
- **Upstream config.yaml:** `sources/config.yaml` -- contains only `familyName: Bitcount` (minimal, for the base Bitcount family only)

The upstream `sources/config.yaml` is insufficient for building "Bitcount Grid Single Ink" specifically, as it only declares `familyName: Bitcount`.

## Override config.yaml

A local override `config.yaml` exists in the google/fonts family directory with the following content:

```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Single Ink
buildVariable: true
buildOTF: false
```

This override was added by commit `f6c68379a` ("Add override config.yaml for 50 font families") on 2026-02-16 as part of a batch operation to enable google-fonts-sources to discover this family as a fontc_crater build target.

The override correctly:
- Points to `sources/Bitcount_Template.designspace` (which exists at the referenced commit)
- Sets the specific family name "Bitcount Grid Single Ink"
- Configures variable font build only (no OTF)

## Conclusions

The source metadata for Bitcount Grid Single Ink is complete and accurate:

1. **Repository URL** is correct and verified.
2. **Commit hash** `89e7994f` is verified -- the binary at this commit matches google/fonts exactly (identical SHA256).
3. **Override config.yaml** exists locally in google/fonts, so no `config_yaml` field is needed in METADATA.pb.
4. **No action needed** -- all source metadata is in order.

## Notes

- This family is part of the larger Bitcount project by Petr van Blokland, which produces many variants (Bitcount, Bitcount Grid Single, Bitcount Grid Single Ink, Bitcount Grid Double, Bitcount Prop Single, etc.) from a shared template designspace.
- The upstream repo has a `sources/config.yaml` but it only sets `familyName: Bitcount` and does not cover the other Bitcount variants. The override config in google/fonts addresses this gap for this specific variant.
- The font was added to Google Fonts on 2025-01-10 (per `date_added` in METADATA.pb) and updated to Version 1.001 on 2025-09-05.
