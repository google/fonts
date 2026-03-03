# Investigation: Bitcount Grid Double Ink

- **Family name**: Bitcount Grid Double Ink
- **Slug**: bitcountgriddoubleink
- **Designer**: Petr van Blokland
- **Category**: DISPLAY
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
    source_file: "fonts/ttf/variable/BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
}
```

The source block is complete with repository URL, commit hash, file mappings, and branch. No `config_yaml` field is set.

## Repository Verification

- **Repository URL**: https://github.com/petrvanblokland/TYPETR-Bitcount
- **Cached at**: upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount
- **Remote verified**: Yes, remote URL matches `https://github.com/petrvanblokland/TYPETR-Bitcount`

## Commit Verification

- **Referenced commit**: `89e7994f73b7f5ced80e7cf493d40be9e66ff82f`
- **Commit message**: "Merge pull request #37 from petrvanblokland/fix-ligatures"
- **Commit date**: 2025-09-05 10:53:08 +0100
- **Author**: Simon Cozens
- **Is HEAD of main**: Yes (no newer commits exist in the repository)

### Timeline Cross-check

| Event | Date | Details |
|-------|------|---------|
| Original onboarding (v1.0) | 2025-01-17 | Commit `c743b20` by Yanone, referenced upstream commit `af0818e` |
| Upstream commit `89e7994` | 2025-09-05 10:53 | Merge PR #37 fixing ligatures, rebuilt fonts |
| google/fonts update (v1.001) | 2025-09-05 15:21 | Commit `5d1b8f3` by Emma Marichal, references `89e7994` |
| google/fonts PR #8960 merged | 2025-09-05 15:56 | Merge commit `380d625` by Emma Marichal |

The v1.001 update was performed the same day as the upstream merge commit. Emma Marichal took the pre-built font binary from the upstream repo at commit `89e7994` shortly after Simon Cozens merged the ligature fix. The commit message explicitly states the upstream commit hash.

### Binary Verification

The font binary in google/fonts exactly matches the pre-built binary at commit `89e7994` in the upstream repo:

- **SHA-256**: `6da42b0c3bef339d827afcb4f8bf3aa90b780b18cfe752e468771757d5a42c4c`
- Both `fonts/ttf/variable/BitcountGridDoubleInk[...].ttf` in upstream and `ofl/bitcountgriddoubleink/BitcountGridDoubleInk[...].ttf` in google/fonts produce the same hash.

This confirms that the pre-built binary was copied directly from the upstream repository, not rebuilt from sources.

## Source Files in Upstream

The upstream repo contains buildable sources at `sources/`:

- `sources/Bitcount_Template.designspace` (the main design source)
- `sources/ufo/` (UFO source directories)
- `sources/features/` (OpenType feature files)
- `sources/config.yaml` (upstream config, contains only `familyName: Bitcount` -- generic for the entire Bitcount superfamily)
- `sources/build/` (build scripts)

The designspace file was verified to exist at the referenced commit `89e7994`.

## Config.yaml Analysis

### Upstream config.yaml (`sources/config.yaml`)

```yaml
familyName: Bitcount
```

This is a minimal config that only specifies the family name as "Bitcount" (the root name of the entire superfamily). It does not reference sources or specify build parameters suitable for building the "Bitcount Grid Double Ink" variant individually.

### Override config.yaml (in google/fonts)

An override `config.yaml` was added to the google/fonts family directory on 2026-02-16 (commit `f6c68379a`):

```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Double Ink
buildVariable: true
buildOTF: false
```

This override config properly references the designspace source file and sets the correct family name for this specific variant. Since an override config exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## Onboarding Method

The font was onboarded using **pre-built binaries** from the upstream repository, not built from sources. The METADATA.pb `files {}` mappings copy the pre-built TTF from `fonts/ttf/variable/` in the upstream repo. This is consistent with the Bitcount superfamily's approach -- the upstream repo maintains pre-built font files alongside the sources.

## Summary

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/petrvanblokland/TYPETR-Bitcount |
| **Commit** | `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` |
| **Commit verified** | Yes (binary SHA-256 match confirmed) |
| **Config** | Override config.yaml in google/fonts |
| **config_yaml in METADATA.pb** | Correctly omitted (auto-detected) |
| **Status** | complete |
| **Confidence** | HIGH |

All metadata is correct. The repository URL, commit hash, and file mappings are verified. The override config.yaml is properly set up for building from sources. No changes needed to METADATA.pb.
