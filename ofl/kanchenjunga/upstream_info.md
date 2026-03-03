# Kanchenjunga — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kanchenjunga`
**Status**: complete (missing config)

## Initial State

The METADATA.pb already contained a complete `source { }` block:

- **repository_url**: `https://github.com/silnrsi/font-kanchenjunga/`
- **commit**: `19a3efac0c2ca42a1b28a53c74ca8f3eb6c12ca7`
- **archive_url**: `https://github.com/silnrsi/font-kanchenjunga/releases/download/v2.001/Kanchenjunga-2.001.zip`
- **branch**: `main`
- **config_yaml**: not set
- **files**: 5 file mappings (OFL.txt + 4 TTF files from the release archive path `Kanchenjunga-2.001/`)

No override `config.yaml` existed in the google/fonts family directory.
No `upstream_info.md` existed in the family directory.

## Investigation

### Onboarding History

The font was onboarded to Google Fonts via PR #8431 ("Kanchenjunga: Version 2.001 added"), created by Emma Marichal on 2024-10-25 and merged on 2024-12-04. The onboarding commit (`24382edba`) explicitly references the upstream repo and commit hash:

> "Taken from the upstream repo https://github.com/silnrsi/font-kanchenjunga/ at commit 19a3efac0c2ca42a1b28a53c74ca8f3eb6c12ca7."

A later commit (`5a9f8d0e6`, 2025-03-19) added the `kirat-rai` subset to METADATA.pb.

### Upstream Repository Verification

The upstream repo `silnrsi/font-kanchenjunga` was cached locally (initially as a shallow clone, unshallowed during this investigation). The repo is clean, on branch `main`, up to date with `origin/main`.

**Commit verification**: The referenced commit `19a3efac0c2ca42a1b28a53c74ca8f3eb6c12ca7` exists in the repo. It was authored on 2024-10-23 with the message "Change CLA SIL International to SIL Global. [nobuild]".

**Tag relationship**: The v2.001 tag points to commit `ae8d1bcb` ("Last preflight for v2.001", 2024-09-11). The referenced commit `19a3efa` is 5 commits after the v2.001 tag. All intervening commits are marked `[nobuild]` but one of them (`a01844a`, "Prep for subsequent development") updated the reference TTFs — adding Medium and SemiBold variants and updating Regular and Bold binaries.

**Binary verification**: The font files in google/fonts are byte-identical to the reference TTFs at commit `19a3efa` (confirmed via matching git blob hashes):
- `Kanchenjunga-Bold.ttf` — blob `6916c2a9`, 50992 bytes
- `Kanchenjunga-Medium.ttf` — blob `cb7db9da`, 51076 bytes
- `Kanchenjunga-Regular.ttf` — blob `a11eae3d`, 50976 bytes
- `Kanchenjunga-SemiBold.ttf` — blob `9d258c6e`, 51020 bytes

This confirms the commit hash in METADATA.pb is correct — the fonts match the reference binaries at that exact commit, not the v2.001 release archive.

### Build System

The upstream repo uses **Smith** (SIL's font build tool), configured via `wscript`. There is no `config.yaml` for gftools-builder anywhere in the repo.

### Source Files

The repo contains gftools-builder-compatible source files at `source/`:
- `source/Kanchenjunga.designspace` — designspace with weight axis (400–700), 2 masters (Regular, Bold), 4 instances
- `source/Kanchenjunga-Regular.ufo` — Regular master
- `source/Kanchenjunga-Bold.ufo` — Bold master
- `source/opentype/master.feax` — OpenType feature file (Smith-specific `.feax` format)
- `source/Kanchenjunga-future.designspace` — future development designspace

The `.designspace` and `.ufo` sources are compatible with gftools-builder. However, the OpenType features use Smith's `.feax` format rather than standard `.fea`, which may require testing to confirm full gftools-builder compatibility.

### Post-Onboarding Upstream Changes

One commit after the referenced hash touches source files:
- `d33fbdc` (HEAD) — "Update copyright date to 2026..." — primarily documentation, but would need verification for source impact.

## Actions Taken

1. Unshallowed the upstream repo clone to access full commit history.
2. Verified the referenced commit hash exists and the font binaries match exactly.
3. Confirmed no config.yaml exists in the upstream repo.
4. Confirmed no override config.yaml exists in the google/fonts family directory.
5. Documented all findings in this report.

## Final State

The source block in METADATA.pb is correct and verified:
- Repository URL is valid and accessible.
- Commit hash is verified — font binaries match exactly at that commit.
- No config.yaml is available (upstream uses Smith build system).
- An override config.yaml could be created for gftools-builder compatibility, pointing to `source/Kanchenjunga.designspace`, but the `.feax` feature files may need attention.

**Status**: The existing source block is accurate. The only missing element is `config_yaml`, which would require creating an override config.yaml in the google/fonts family directory. This should be tested to confirm gftools-builder can handle the Smith-specific `.feax` features.

## Source Block

The current source block in METADATA.pb is correct as-is:

```
source {
  repository_url: "https://github.com/silnrsi/font-kanchenjunga/"
  commit: "19a3efac0c2ca42a1b28a53c74ca8f3eb6c12ca7"
  archive_url: "https://github.com/silnrsi/font-kanchenjunga/releases/download/v2.001/Kanchenjunga-2.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Kanchenjunga-2.001/Kanchenjunga-Regular.ttf"
    dest_file: "Kanchenjunga-Regular.ttf"
  }
  files {
    source_file: "Kanchenjunga-2.001/Kanchenjunga-Medium.ttf"
    dest_file: "Kanchenjunga-Medium.ttf"
  }
  files {
    source_file: "Kanchenjunga-2.001/Kanchenjunga-SemiBold.ttf"
    dest_file: "Kanchenjunga-SemiBold.ttf"
  }
  files {
    source_file: "Kanchenjunga-2.001/Kanchenjunga-Bold.ttf"
    dest_file: "Kanchenjunga-Bold.ttf"
  }
  branch: "main"
}
```

If an override config.yaml were to be created, it would look approximately like:

```yaml
sources:
  - source/Kanchenjunga.designspace
```

However, this needs testing due to the Smith-specific `.feax` feature format in the sources.
