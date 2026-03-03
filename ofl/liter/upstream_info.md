# Liter — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/skugiz/liter"
  commit: "3808843f982fae783aedd11d2f6ed8956f37fa04"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Liter-Regular.ttf"
    dest_file: "Liter-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

The upstream repository is at `https://github.com/skugiz/liter`, maintained by Anton Skugarov (skugiz@gmail.com). The repository was created using the `googlefonts/googlefonts-project-template`.

**Repository structure at commit `3808843`:**

- `sources/liter.glyphs` — Glyphs source file
- `sources/config.yaml` — gftools-builder configuration
- `fonts/ttf/Liter-Regular.ttf` — Pre-built TTF binary
- `fonts/webfonts/Liter-Regular.woff2` — Pre-built WOFF2
- `OFL.txt` — SIL Open Font License
- `documentation/` — Promo images and description HTML
- `Makefile` — Build automation
- `.github/workflows/build.yaml` — CI build workflow

**config.yaml contents:**

```yaml
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: true
# removeOutlineOverlaps: false
sources:
  - liter.glyphs
familyName: Liter
```

The config references `liter.glyphs` (relative to the `sources/` directory), which was confirmed to exist at the referenced commit.

**Commit history (full):**

| Hash | Date | Description |
|------|------|-------------|
| `3808843` | 2025-01-16 | Updates authors name in AUTHORS.txt (initial/root commit) |
| `c309900` | 2025-11-12 | Kerning fix (colon/slash) and cedillacomb position fix |
| `cbacd5b` | 2025-11-12 | Small fixed spacing |
| `bb5f6a9` | 2025-11-12 | Merge PR #11 (small fixes) |

The repository has only 4 commits total, with `3808843` being the root commit. This is notable because the onboarding PR (#8819) referenced a different commit hash `4bcb5b1fcac534445cb40ac31c1c4c5669fcbbc6`, which no longer exists in the repository.

## Onboarding History

**PR #8819** — "Liter: Version 1.004; ttfautohint (v1.8.4.7-5d5b) added"
- Author: Emma Marichal (@emmamarichal)
- Merged: 2025-01-14 by Marc Foley (@m4rc1e)
- Body stated: "Taken from the upstream repo https://github.com/skugiz/liter at commit https://github.com/skugiz/liter/commit/4bcb5b1fcac534445cb40ac31c1c4c5669fcbbc6"
- The font was added to google/fonts with the commit message: "Liter: Version 1.004; ttfautohint (v1.8.4.7-5d5b) added"
- Date added: 2025-01-09

**Related PRs:**
- **PR #8820** — "Liter: Update families.csv" (merged 2025-01-09) — Added article and classification tags
- **PR #9072** — "Liter: designer updated in metadata.pb" (merged 2025-02-13) — Corrected designer spelling
- **PR #9190** — "Liter- Author spelling" (merged 2025-03-12) — Another spelling correction (Aleksandr -> Alexandr)

**Commit hash discrepancy:**

The original onboarding commit `4bcb5b1` no longer exists in the upstream repository. The repository appears to have been reset/force-pushed after the font was already merged into google/fonts. The earliest surviving commit `3808843` (dated 2025-01-16, two days after the PR merge) is the root commit of the current repository.

The batch 2/4 commit (`4ad8ac68`, 2025-03-31) updated the METADATA.pb source block, changing the commit hash from `4bcb5b1` to `3808843` and adding the `config_yaml` field. This data came from the fontc_crater targets.json file.

**Binary verification:**

The `Liter-Regular.ttf` in google/fonts and the one at commit `3808843` in the upstream repo have identical MD5 hashes (`a1ebbed47d71a738ac473c8758b1d3b8`), confirming that the font binary was not altered in the repository reset. The current commit hash `3808843` is a valid reference for the same font content that was originally onboarded.

## Build Configuration

A `config.yaml` file exists in the upstream repository at `sources/config.yaml` at the referenced commit. The METADATA.pb correctly points to this path via `config_yaml: "sources/config.yaml"`. The configuration builds static TTF from the `liter.glyphs` source file.

No override config.yaml is needed in google/fonts since the upstream repo already has one.

## Findings

1. **Source block is complete and correct.** The current METADATA.pb source block has all required fields: `repository_url`, `commit`, `files` mappings, `branch`, and `config_yaml`.

2. **Commit hash is valid despite original being lost.** The original onboarding commit `4bcb5b1` was lost when the upstream repository was reset/force-pushed. The current commit `3808843` (the root commit of the rebuilt repo) contains identical font binaries, as confirmed by MD5 hash comparison. This is the best available reference.

3. **Font binary match confirmed.** The `Liter-Regular.ttf` in google/fonts matches exactly with the version at commit `3808843` in the upstream repo.

4. **config.yaml is present and correct.** The upstream repo has a valid gftools-builder config at `sources/config.yaml` that correctly references the `liter.glyphs` source file.

5. **Newer upstream work exists.** Commits from November 2025 (PR #11) added kerning fixes and spacing adjustments. These changes have not been incorporated into google/fonts and would need a separate update/QA process.

6. **Single-weight font.** Liter is a single-weight (Regular 400) sans-serif family supporting Latin and Cyrillic scripts.

## Recommended Source Block

The current source block in METADATA.pb is correct and complete. No changes are needed:

```
source {
  repository_url: "https://github.com/skugiz/liter"
  commit: "3808843f982fae783aedd11d2f6ed8956f37fa04"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Liter-Regular.ttf"
    dest_file: "Liter-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
