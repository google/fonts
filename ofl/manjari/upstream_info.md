# Manjari — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://gitlab.com/smc/fonts/manjari"
  commit: "8948773e572ce0b58d93b0f120f561a0b02e9853"
  files {
    source_file: "build/Manjari-Regular.ttf"
    dest_file: "Manjari-Regular.ttf"
  }
  files {
    source_file: "build/Manjari-Bold.ttf"
    dest_file: "Manjari-Bold.ttf"
  }
  files {
    source_file: "build/Manjari-Thin.ttf"
    dest_file: "Manjari-Thin.ttf"
  }
  branch: "master"
}
```

An override `config.yaml` also exists in the google/fonts family directory:
```yaml
buildVariable: false
sources:
  - sources/Manjari-Thin.ufo
  - sources/Manjari-Regular.ufo
  - sources/Manjari-Bold.ufo
```

## Repository Analysis

The upstream repository is hosted on GitLab at `https://gitlab.com/smc/fonts/manjari`. It is maintained by Santhosh Thottingal. The cached clone is at `upstream_repos/fontc_crater_cache/smc/fonts/manjari/`.

The repository was originally on GitHub at `https://github.com/smc/manjari` (referenced in the v1.710 onboarding commit), but was later migrated to GitLab under the SMC (Swathanthra Malayalam Computing) organization's font group.

### Repository structure (at referenced commit `8948773`):

- `sources/Manjari-Thin.ufo` — UFO source for Thin weight
- `sources/Manjari-Regular.ufo` — UFO source for Regular weight
- `sources/Manjari-Bold.ufo` — UFO source for Bold weight
- `sources/features/` — OpenType feature files
- `sources/svgs/` — SVG source artwork
- `Makefile` — Build system using fontmake
- `requirements.txt` — Python dependencies
- `VERSION` — Contains "2.0.0" at the referenced commit
- `build/` — Gitignored; build output directory for generated fonts

No `config.yaml` exists in the upstream repository (neither at the referenced commit nor at HEAD). The upstream build system uses a Makefile that invokes fontmake directly.

The repo has 539 total commits. HEAD is at version 2.2.0, significantly newer than the referenced version 2.0.0.

## Onboarding History

### Initial onboarding (v1.710)

Commit `d07892912` by Marc Foley on 2019-01-07 added Manjari v1.710 to Google Fonts. The commit message stated it was taken from `https://github.com/smc/manjari` at release `Version1.710`. This was the original GitHub location before the GitLab migration.

### Version 2.000 update

PR #3155, titled "Manjari: Version 2.000 added," was authored by Viviana Monsalve (vv-monsalve) and merged on 2021-03-10. The PR body stated:

> Manjari Version 2.000 taken from the upstream repo https://gitlab.com/smc/fonts/manjari.git at commit daba7c592ea3d51358c2c1368bb9d09c8a6e2c37.

The hash `daba7c5` is an annotated tag object (`Version2.000`), not a commit. When dereferenced, it points to commit `8948773e572ce0b58d93b0f120f561a0b02e9853` ("Version update: 2.0.0", dated 2021-03-06). This is the actual commit used for the onboarding.

The commit `59eed8e65` updated the three TTF files and added an `upstream.yaml` file.

### Source metadata evolution

1. **2024-03-04** (`c891a9b`): Simon Cozens added repository_url to METADATA.pb (pointing to the old GitHub URL `https://github.com/smc/manjari`).
2. **2024-04-03** (`66f91f1`): Simon Cozens merged upstream.yaml into METADATA.pb, updating the URL to `https://gitlab.com/smc/fonts/manjari`, adding file mappings, and setting branch to `tags/Version2.000`.
3. **2025-11-21** (`2dc7250`): Felipe Sanches added the commit hash `8948773` (correctly dereferencing the tag to its underlying commit), changed branch from `tags/Version2.000` to `master`, and added the override `config.yaml`.

## Build Configuration

The upstream repository does not have a `config.yaml`. It uses a Makefile-based build system that invokes fontmake to build individual UFO sources into TTF/OTF outputs.

An override `config.yaml` was added to the google/fonts family directory in commit `2dc7250` (2025-11-21). It specifies:
- `buildVariable: false` (three separate static masters, not a variable font)
- Three UFO sources: `sources/Manjari-Thin.ufo`, `sources/Manjari-Regular.ufo`, `sources/Manjari-Bold.ufo`

This override config is appropriate for gftools-builder/fontc compatibility. Since the override exists locally, no `config_yaml` field is needed in METADATA.pb.

## Findings

1. **Source block is complete and correct.** The repository URL, commit hash, file mappings, and branch are all properly set.

2. **Commit hash is correct.** The METADATA.pb commit `8948773` is the actual commit underlying the `Version2.000` tag (`daba7c5`), which was referenced in PR #3155. The tag was an annotated tag object; the METADATA.pb correctly records the underlying commit hash rather than the tag object hash.

3. **Override config.yaml is in place.** Since the upstream repo lacks a config.yaml, the override in google/fonts correctly defines the gftools-builder configuration.

4. **Upstream has newer versions.** The upstream repo has progressed to version 2.2.0 (with changes including dotted circle rendering fixes, version bumps, and CI updates). These newer versions have not been onboarded to Google Fonts and would need separate review.

5. **Repository migrated from GitHub to GitLab.** The original onboarding (v1.710) used the GitHub URL `https://github.com/smc/manjari`. The v2.000 update correctly used the GitLab URL. The current METADATA.pb has the correct GitLab URL.

6. **No action needed.** The source block and override config are complete and accurate as previously set up.

## Recommended Source Block

The current source block is correct. No changes are needed:

```
source {
  repository_url: "https://gitlab.com/smc/fonts/manjari"
  commit: "8948773e572ce0b58d93b0f120f561a0b02e9853"
  files {
    source_file: "build/Manjari-Regular.ttf"
    dest_file: "Manjari-Regular.ttf"
  }
  files {
    source_file: "build/Manjari-Bold.ttf"
    dest_file: "Manjari-Bold.ttf"
  }
  files {
    source_file: "build/Manjari-Thin.ttf"
    dest_file: "Manjari-Thin.ttf"
  }
  branch: "master"
}
```

With the existing override `config.yaml` in the google/fonts family directory (no `config_yaml` field needed in METADATA.pb).
