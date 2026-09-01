# Investigation: Bitcount Ink

- **Family name**: Bitcount Ink
- **Slug**: bitcountink
- **Designer**: Petr van Blokland
- **Category**: Display
- **Date added**: 2025-01-10
- **Model**: Claude Opus 4.6

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "89e7994f73b7f5ced80e7cf493d40be9e66ff82f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Repository

- **URL**: https://github.com/petrvanblokland/TYPETR-Bitcount
- **Verified**: Yes, remote matches cached clone at `upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount`
- **Branch**: main
- **Total commits**: 229
- **Shared repo**: This repository contains sources for multiple Bitcount family variants (Ink, Grid Double, Grid Single, Prop Double, Prop Single, etc.)

## Commit Verification

- **Referenced commit**: `89e7994f73b7f5ced80e7cf493d40be9e66ff82f`
- **Commit message**: "Merge pull request #37 from petrvanblokland/fix-ligatures"
- **Commit date**: 2025-09-05 10:53:08 +0100
- **Commit author**: Simon Cozens
- **Is HEAD**: Yes, this commit is the current HEAD of the main branch
- **Exists in repo**: Yes

### Cross-verification

The onboarding commit in google/fonts (`c020967`) was authored by Emma Marichal on 2025-09-05 with message "Bitcount Ink: Version 1.001 added". The commit body explicitly states:

> Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/89e7994f73b7f5ced80e7cf493d40be9e66ff82f.

The upstream commit `89e7994` was created the same day (2025-09-05) as the onboarding, just hours earlier. The font binary sizes match exactly:

- **Upstream at 89e7994**: 314,728 bytes
- **google/fonts**: 314,728 bytes

This confirms that the binary was taken directly from the upstream repo at this exact commit. The font was a pre-built binary copied from `fonts/ttf/variable/` in the upstream repo, not compiled from sources via gftools-builder.

The merge PR in google/fonts was #8963 (`gftools_packager_ofl_bitcountink`), merged by Emma Marichal on 2025-09-05.

## google/fonts Commit History

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `f6c6837` | 2026-02-16 | (batch) | Add override config.yaml for 50 font families |
| `6053438` | 2025-09-05 | Emma Marichal | update OFL link |
| `856b2ad` | 2025-09-05 | Emma Marichal | add article |
| `c020967` | 2025-09-05 | Emma Marichal | Bitcount Ink: Version 1.001 added |

## Source Files

The upstream repository contains `.designspace` and `.ufo` sources at:

- `sources/Bitcount_Template.designspace` -- a template designspace with 5 axes (wght, ELXP, ELSH, slnt, CRSV)
- `sources/ufo/` -- 15 UFO directories for all Bitcount variants:
  - `Bitcount_Grid_Double.ufo`, `Bitcount_Grid_Double-Italic.ufo`
  - `Bitcount_Grid_Single.ufo`, `Bitcount_Grid_Single-Italic.ufo`
  - `Bitcount_Mono_Double.ufo`, `Bitcount_Mono_Double-Italic.ufo`
  - `Bitcount_Mono_Single.ufo`, `Bitcount_Mono_Single-Italic.ufo`
  - `Bitcount_Prop_Double.ufo`, `Bitcount_Prop_Double-Italic.ufo`
  - `Bitcount_Prop_Single.ufo`, `Bitcount_Prop_Single-Italic.ufo`
  - `Bitcount-LayerElements.ufo`, `Bitcount-LayerElements-Italic.ufo`
  - `Bitcount-VariationPixels.ufo`

Pre-built font binaries exist at `fonts/ttf/variable/` (13 variable font files for all variants).

## Config (Build Configuration)

### Upstream config.yaml

A `sources/config.yaml` file exists in the upstream repo at the referenced commit, but it contains only:

```yaml
familyName: Bitcount
```

This is a minimal config with a generic family name ("Bitcount") that does not specify "Bitcount Ink". It lacks the `sources` key pointing to the designspace file.

### Override config.yaml (google/fonts)

An override `config.yaml` exists at `ofl/bitcountink/config.yaml` in google/fonts (added in commit `f6c6837` on 2026-02-16):

```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Ink
buildVariable: true
buildOTF: false
```

This override correctly:
- Points to the designspace source file (`sources/Bitcount_Template.designspace`)
- Sets the specific family name "Bitcount Ink"
- Enables variable font builds and disables OTF builds

### config_yaml in METADATA.pb

No `config_yaml` field is present in the METADATA.pb source block, which is correct. Since a local override `config.yaml` exists in the google/fonts family directory, google-fonts-sources auto-detects it and the field can be omitted.

## Notes

- The font was onboarded as a pre-built binary, not compiled from sources. The binary in google/fonts was copied directly from the upstream repo's `fonts/ttf/variable/` directory.
- The font has 11 axes: CRSV, ELSH, ELXP, SZP1, SZP2, XPN1, XPN2, YPN1, YPN2, slnt, wght. However, the designspace template only defines 5 axes (wght, ELXP, ELSH, slnt, CRSV). The additional size and position axes (SZP1, SZP2, XPN1, XPN2, YPN1, YPN2) are likely added through the build process or the "Ink" layer compositing.
- This is one of many Bitcount variants sharing the same upstream repository. The override config specifies "Bitcount Ink" as the family name to distinguish it from other variants.
- There was a rebuild PR #9572 (merged 2025-06-19) titled "Update Bitcount Ink 1.001" but it affected different files (larger binary sizes, likely other Bitcount variants like Grid Double Ink or Prop Double Ink), not the Bitcount Ink font itself.

## Status

- **repository_url**: Correct
- **commit**: Verified (matches onboarding, binary sizes identical, same-day commit)
- **config**: Override config.yaml present in google/fonts (correct approach given upstream's minimal config)
- **config_yaml field**: Correctly omitted from METADATA.pb
- **Overall**: **COMPLETE**
- **Confidence**: **HIGH**
