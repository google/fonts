# Investigation Report: Bitcount Grid Double

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Confidence**: HIGH

## Family Metadata

- **Family Name**: Bitcount Grid Double
- **Designer**: Petr van Blokland
- **Category**: DISPLAY
- **Date Added**: 2025-01-10
- **License**: OFL
- **Font File**: `BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf`

## Source Block (Current in METADATA.pb)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "af0818eaeb3b0839806ea19134fc18f317cdcf5a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf"
    dest_file: "BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Repository Verification

- **Repository URL**: https://github.com/petrvanblokland/TYPETR-Bitcount
- **Remote verified**: Yes, matches cached repo at `upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount`
- **Repository accessible**: Yes

## Commit Verification

- **Commit**: `af0818eaeb3b0839806ea19134fc18f317cdcf5a`
- **Commit date**: 2025-01-13
- **Commit message**: "Update fixAnchors.py"
- **Author**: petrvanblokland (buro@petr.com)
- **Branch**: main (confirmed, commit is on main branch)
- **Commits after referenced**: 17 additional commits on main since this commit

### Onboarding Provenance

The initial onboarding commit in google/fonts was `bb009d354` (2025-01-17, by Yanone), with the message:

> Bitcount Grid Double: Version 1.0 added
>
> Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/af0818eaeb3b0839806ea19134fc18f317cdcf5a.
>
> Resolves #5468

This was merged via PR #8959 on 2025-06-06. The commit explicitly references the same hash `af0818eae` that is recorded in METADATA.pb, confirming the commit hash is correct.

A subsequent rebuild was performed by Simon Cozens (`ce6029c68`, 2025-06-19) as part of PR #9587 ("bitcount-grid-double-rebuild"), with message "Fix italic feature, fixes ots-sanitizer". This updated the binary from 168,092 to 168,224 bytes. The font binary currently in google/fonts (168,224 bytes, dated 2025-06-20) matches this rebuild.

## Source Files at Referenced Commit

The upstream repo at commit `af0818eae` contained:

- **Designspace**: `sources/Bitcount_Template.designspace` (confirmed present)
- **UFO sources**: Multiple UFOs in `sources/ufo/`, including:
  - `Bitcount_Grid_Double.ufo`
  - `Bitcount_Grid_Double-Italic.ufo`
  - `Bitcount-LayerElements.ufo`
  - `Bitcount-LayerElements-Italic.ufo`
  - `Bitcount-VariationPixels.ufo`
  - Plus many other Bitcount variant UFOs (Mono, Prop, Single, etc.)
- **Pre-built binary**: `fonts/ttf/variable/BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf` (confirmed present)
- **Upstream config.yaml**: `sources/config.yaml` (contains only `familyName: Bitcount`)

## Config Verification

### Upstream config.yaml (at referenced commit)

Located at `sources/config.yaml`, contains:
```yaml
familyName: Bitcount
```

This is a minimal config that does not specify sources or build targets, and uses a generic family name "Bitcount" rather than the specific sub-family "Bitcount Grid Double".

### Override config.yaml (in google/fonts)

An override `config.yaml` exists at `ofl/bitcountgriddouble/config.yaml` with contents:

```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Double
buildVariable: true
buildOTF: false
```

This override was added in commit `f6c68379a` / `b7dbad8dc` (2026-02-16) as part of a batch operation to add override configs for 50 font families. The override is necessary because:

1. The upstream `sources/config.yaml` uses the generic name "Bitcount" and does not specify source paths
2. The override correctly references `sources/Bitcount_Template.designspace` and specifies the correct family name "Bitcount Grid Double"
3. The override appropriately sets `buildVariable: true` and `buildOTF: false`

Since an override `config.yaml` exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## METADATA.pb Completeness

| Field | Value | Status |
|-------|-------|--------|
| `repository_url` | `https://github.com/petrvanblokland/TYPETR-Bitcount` | Present, verified |
| `commit` | `af0818eaeb3b0839806ea19134fc18f317cdcf5a` | Present, verified via onboarding commit message |
| `branch` | `main` | Present, verified |
| `config_yaml` | (omitted) | Correct: override config.yaml in google/fonts |
| `files` | OFL.txt + font binary | Present |

## Summary

The source metadata for Bitcount Grid Double is complete and correct. The repository URL points to the valid upstream repo by Petr van Blokland. The commit hash `af0818eae` was confirmed as the exact commit used for onboarding, as explicitly cited in the gftools-packager onboarding commit message by Yanone (2025-01-17). The upstream repo contains gftools-builder compatible sources (.designspace + .ufo), but the upstream `sources/config.yaml` was too generic for this specific sub-family. An appropriate override `config.yaml` was added to the google/fonts family directory, making the `config_yaml` field unnecessary in METADATA.pb. No further action is needed.

## Config

- **Override config.yaml in google/fonts**: Yes
- **config_yaml in METADATA.pb**: Correctly omitted (auto-detected)

## Conclusion

**Status**: complete
**Confidence**: HIGH
**Action needed**: None. All source metadata is present and verified.
