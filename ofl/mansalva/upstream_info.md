# Mansalva — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/carolinashort/mansalva"
  commit: "192d65ff2d1560ff6399abde05904d910965d483"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Mansalva-Regular.ttf"
    dest_file: "Mansalva-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

The source block was ported in batch commit `4ad8ac680` ("[Batch 2/4] port info from fontc_crater targets list") on 2025-03-31, which imported data from the fontc_crater target.json file.

## Repository Analysis

- **Repository**: https://github.com/carolinashort/mansalva
- **Default branch**: master
- **Designer**: Carolina Short
- **Repo status**: Clean, up to date with remote

The upstream repository has an unusual structure: it contains only a single commit (`192d65ff`), which is a merge commit ("Merge pull request #9 from emmamarichal/master"). The repository history was apparently rewritten/force-pushed at some point, collapsing all prior history into this single commit.

**Repository structure at commit `192d65f`:**
- `sources/Mansalva.glyphs` — Glyphs source file (1.5 MB)
- `sources/config.yaml` — gftools-builder configuration
- `sources/Old versions/Mansalva.glyphs` — older version of the source
- `fonts/ttf/Mansalva-Regular.ttf` — compiled TTF binary (355,776 bytes)
- `fonts/otf/Mansalva-Regular.otf` — compiled OTF binary
- `fonts/webfonts/Mansalva-Regular.woff2` — compiled WOFF2
- `documentation/` — promotional images and documentation
- `OFL.txt`, `AUTHORS.txt`, `CONTRIBUTORS.txt`, `README.md`

## Onboarding History

### Initial onboarding (v2.002) — 2019-08-29

Mansalva was first added to Google Fonts by Marc Foley in commit `a5784483f`:
- Commit message: "mansalva: v2.002 added."
- Referenced upstream commit: `81e372e4ff993e02533ef976b36156c0c6ba9505` (no longer exists in the repo due to history rewrite)
- Added `Mansalva-Regular.ttf` (114,844 bytes), `METADATA.pb`, `OFL.txt`, and `DESCRIPTION.en_us.html`

### Update (v2.112) — 2022-10-14

Emma Marichal updated Mansalva to version 2.112 via PR #5373, merged by Rosalie Wagner:
- PR title: "Mansalva: Version 2.112; ttfautohint (v1.8.4.7-5d5b) added"
- PR body referenced upstream commit `2237a60711d5abb1371f693b352cd54ae705e0e8` (also no longer exists in repo)
- The merged commit in google/fonts (`18679c226`) updated the reference to `192d65ff2d1560ff6399abde05904d910965d483`
- Updated `Mansalva-Regular.ttf` from 114,844 bytes to 355,776 bytes
- Added `upstream.yaml` (later merged into METADATA.pb in commit `66f91f10f`)

The commit hash discrepancy between the PR body (`2237a607`) and the final google/fonts commit (`192d65f`) is explained by the fact that Emma Marichal's PR #9 to the upstream repo was merged during the process, creating a new merge commit `192d65f` that became the new HEAD. The METADATA.pb was updated to reference this final state.

### Binary verification

The TTF binary in google/fonts (`Mansalva-Regular.ttf`, SHA-256: `613ca294f0a364fd282a06d5e8a65db5d8f2bb8b834f8b21437a53cf70dafb8a`) is byte-identical to the file at `fonts/ttf/Mansalva-Regular.ttf` in the upstream repo at commit `192d65f`. This confirms the commit hash is correct.

## Build Configuration

The upstream repo has a `sources/config.yaml` at the referenced commit with the following content:

```yaml
sources:
  - Mansalva.glyphs
familyName: Mansalva
buildVariable: False
```

This is a valid gftools-builder configuration that references `Mansalva.glyphs` (located in the same `sources/` directory). The METADATA.pb correctly points to `sources/config.yaml`.

## Findings

1. **Source block is complete and correct.** The repository URL, commit hash, branch, config_yaml path, and file mappings are all accurate.
2. **Commit hash verified.** The referenced commit `192d65ff2d1560ff6399abde05904d910965d483` is the HEAD of the master branch, and the font binary matches byte-for-byte.
3. **Config.yaml verified.** The `sources/config.yaml` file exists at the referenced commit and contains valid gftools-builder configuration.
4. **History rewrite noted.** The upstream repo had its history rewritten to a single commit. Earlier commit hashes referenced in onboarding messages (`81e372e4` from 2019, `2237a607` from the 2022 PR body) no longer exist. This is not a problem for the current state, as the METADATA.pb correctly references the current HEAD.
5. **No action needed.** The source block is already complete with all required fields.

## Recommended Source Block

The current source block is correct and complete. No changes are needed:

```
source {
  repository_url: "https://github.com/carolinashort/mansalva"
  commit: "192d65ff2d1560ff6399abde05904d910965d483"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Mansalva-Regular.ttf"
    dest_file: "Mansalva-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```
