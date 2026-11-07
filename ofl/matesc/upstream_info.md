# Mate SC — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/etunni/mate"
  commit: "2ea8febc952610379af663b1651411493d34beea"
  config_yaml: "sources/matesc.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/matesc/ttf/MateSC-Regular.ttf"
    dest_file: "MateSC-Regular.ttf"
  }
  branch: "master"
}
```

The source block was already fully populated. The `repository_url` and `commit` fields were added by the gftools-packager commit (dbbe08276, 2023-02-24). The `config_yaml` field was added later by commit 53995c52a (2025-03-25). The `branch` field was removed in that same commit but subsequently restored by commit f19b6da7d.

## Repository Analysis

- **Repository**: https://github.com/etunni/mate
- **Owner**: Eduardo Rodriguez Tunni (etunni)
- **Default branch**: master
- **Total commits**: 1 (the entire repo consists of a single merge commit)
- **Only commit**: `2ea8febc952610379af663b1651411493d34beea` (2023-02-24) — "Merge pull request #1 from emmamarichal/master"

The repository was set up by merging PR #1, submitted by Emma Marichal, which added the complete Mate family sources (Mate, Mate Italic, and Mate SC) along with compiled font files, config files, and documentation.

### Source files

- `sources/MateSC.glyphs` — Glyphs source for Mate SC (familyName: "Mate SC", dated 2023-02-22)
- `sources/Mate.glyphs` — Glyphs source for Mate Regular
- `sources/Mate-Italic.glyphs` — Glyphs source for Mate Italic
- `sources/matesc.yaml` — gftools-builder config for Mate SC
- `sources/mate.yaml` — gftools-builder config for Mate (Regular + Italic)

### Compiled fonts in upstream

- `fonts/matesc/ttf/MateSC-Regular.ttf` — Pre-compiled TTF
- `fonts/matesc/otf/MateSC-Regular.otf`
- `fonts/matesc/webfonts/MateSC-Regular.woff2`

## Onboarding History

1. **Initial onboarding** (2015-03-07): Mate SC was first added to Google Fonts in the initial commit (90abd17b4). No upstream repo existed at that time.

2. **Upstream repo creation and update** (2023-02-24): Emma Marichal created the upstream repository structure and submitted PR #1 to etunni/mate with cleaned source files, build configs, and compiled fonts. Eduardo Tunni merged it on the same day. Emma's PR comment: "Here you can find Mate and Mate SC upgrade. As usual, I cleaned the files, added missing kerning groups etc."

3. **google/fonts PR #5931** (2023-02-24, merged 2023-03-01): Submitted by Emma Marichal. Used gftools-packager to update Mate SC in google/fonts from upstream repo at commit `2ea8febc`. The PR contained two commits:
   - `dbbe08276`: "[gftools-packager] Mate SC: Version 1.003" — font binary update
   - `fd93ee8b5`: "Mate SC: description updated"

4. **Binary verification**: The `MateSC-Regular.ttf` in google/fonts has an identical SHA-256 hash (`7aa5db42e899619bf2ecac412fc5668a3ea5d5cdc0af05cf95656c10fdfb50a0`) to the file at `fonts/matesc/ttf/MateSC-Regular.ttf` in the upstream repo at the referenced commit. This confirms the commit hash is correct.

## Build Configuration

The upstream repo contains `sources/matesc.yaml` at the referenced commit:

```yaml
sources:
  - MateSC.glyphs
outputDir: "../fonts/matesc"
```

This is a valid gftools-builder configuration. The source path (`MateSC.glyphs`) is relative to the config file's location in the `sources/` directory. The output directory points to `fonts/matesc/` relative to the repo root.

The `config_yaml` field in METADATA.pb correctly points to `sources/matesc.yaml`.

## Findings

- **Source block is complete and correct.** All fields (repository_url, commit, config_yaml, files, branch) are populated with accurate values.
- **Commit hash verified.** The upstream repo has only one commit, which is exactly the one referenced in METADATA.pb. The binary font file in google/fonts matches the one in the upstream repo byte-for-byte.
- **Config file verified.** The `sources/matesc.yaml` file exists at the referenced commit and contains a valid gftools-builder configuration pointing to the `MateSC.glyphs` source file.
- **No corrections needed.** The existing metadata is accurate and complete.

Note: Mate SC shares the upstream repository (etunni/mate) with the "Mate" family, which has its own separate config at `sources/mate.yaml`.

## Recommended Source Block

The current source block is correct. No changes are needed.

```
source {
  repository_url: "https://github.com/etunni/mate"
  commit: "2ea8febc952610379af663b1651411493d34beea"
  config_yaml: "sources/matesc.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/matesc/ttf/MateSC-Regular.ttf"
    dest_file: "MateSC-Regular.ttf"
  }
  branch: "master"
}
```
