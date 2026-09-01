# Investigation Report: Bitcount Grid Single

**Family Name:** Bitcount Grid Single
**Slug:** bitcountgridsingle
**Family Directory:** ofl/bitcountgridsingle
**Date Added:** 2025-01-10
**Designer:** Petr van Blokland
**Category:** DISPLAY
**Status:** complete
**Confidence:** HIGH
**Model:** Claude Opus 4.6

---

## Source Block (Current METADATA.pb)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "af0818eaeb3b0839806ea19134fc18f317cdcf5a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf"
    dest_file: "BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf"
  }
  branch: "main"
}
```

No `config_yaml` field is set in the source block. An override `config.yaml` exists in the google/fonts family directory.

## Repository

- **URL:** https://github.com/petrvanblokland/TYPETR-Bitcount
- **Cached at:** upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount
- **Remote verified:** Yes, matches `https://github.com/petrvanblokland/TYPETR-Bitcount`

## Commit Verification

- **Referenced commit:** `af0818eaeb3b0839806ea19134fc18f317cdcf5a`
- **Commit date:** 2025-01-13
- **Commit message:** "Update fixAnchors.py"
- **Author:** petrvanblokland (buro@petr.com)

The referenced commit modified `fixAnchors.py` (a helper script), not font sources directly. The preceding commit `e81fcb91c` (2025-01-06, "Rebuild fonts") was the last commit that rebuilt the font binaries before this one.

### Binary File Verification

The SHA-256 hash of `BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf` matched exactly between the google/fonts directory and the upstream repo at the referenced commit:

- **google/fonts hash:** `f28e3429f64e9f27b32c6819a7f7b0d58164cf2716fdb9c3df8a5b35187d41a4`
- **Upstream at af0818e hash:** `f28e3429f64e9f27b32c6819a7f7b0d58164cf2716fdb9c3df8a5b35187d41a4`

This confirms the binary file was taken directly from the upstream repo at the referenced commit without modification.

## Onboarding History

- **Onboarding commit in google/fonts:** `7f41474fc` (2025-01-17, "Bitcount Grid Single: Version 1.0 added")
- **Author:** Yanone (post@yanone.de)
- **Commit body:** "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit af0818eaeb3b0839806ea19134fc18f317cdcf5a. Resolves #5468"
- **PR:** #8961, merged 2025-06-06 by Emma Marichal (@emmamarichal)
- **Files added:** METADATA.pb, OFL.txt, font binary, ARTICLE.en_us.html

The onboarding was performed by Yanone using gftools-packager, taking the pre-built binary directly from the upstream repository. The commit message explicitly referenced the upstream repo and commit hash.

## Source Files

The upstream repo contains gftools-builder compatible sources:

- **Designspace:** `sources/Bitcount_Template.designspace` (template-style designspace with axes: wght, ELXP, ELSH, slnt, CRSV)
- **UFO sources:** 15 UFO directories under `sources/ufo/`, including `Bitcount_Grid_Single.ufo` and `Bitcount_Grid_Single-Italic.ufo`
- **Upstream config.yaml:** `sources/config.yaml` -- existed at the referenced commit but only contains `familyName: Bitcount` (the base family name, not the specific sub-family)

## Override config.yaml

An override `config.yaml` exists in the google/fonts family directory at `ofl/bitcountgridsingle/config.yaml`, added in commit `f6c68379a` (2026-02-16, "Add override config.yaml for 50 font families").

Contents:
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Single
buildVariable: true
buildOTF: false
```

This override is necessary because the upstream `sources/config.yaml` uses `familyName: Bitcount` (the generic family name), while this specific family variant requires `familyName: Bitcount Grid Single`. The Bitcount project produces multiple font families from the same template designspace, each with a different family name. The override config correctly specifies the sub-family name and references the shared designspace.

Since the override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## Additional Upstream Activity

Significant upstream development occurred after the referenced commit:
- 2025-01-18: SampleSlider updates
- 2025-01-31: JS animation demos
- 2025-04-20 through 2025-04-26: Documentation/demo page moves
- 2025-06-13: Position axes reworked (PR #35, axes now -100 to 100)
- 2025-06-18 through 2025-06-19: Version bumps, rule fixes
- 2025-09-05: Ligature fix (PR #37)

These later changes have not been incorporated into google/fonts and would require a separate review process.

## Summary

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | af0818eaeb3b0839806ea19134fc18f317cdcf5a |
| Commit Date | 2025-01-13 |
| Config | Override config.yaml in google/fonts |
| Binary Match | YES (SHA-256 verified) |
| Status | complete |
| Confidence | HIGH |

The source metadata for Bitcount Grid Single is complete and verified. The repository URL and commit hash are correct, the binary file matches exactly, and the override config.yaml properly specifies the sub-family name. No changes to METADATA.pb are needed.
