# BJCree

**Status**: `complete`
**Date**: 2026-04-27
**Designer**: SIL International (Bill Jancewicz, Peter Martin, Sharon Correll)
**License**: OFL
**METADATA.pb**: `ofl/bjcree/METADATA.pb`
**Model**: Claude Opus 4.7 (1M context)

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/silnrsi/font-bjcree |
| Commit | `7476fb691e64eff8956faf2bd68911cb3e1c65b7` |
| Config YAML | (none — see Build Pipeline) |
| Branch | `main` |
| Archive URL | https://github.com/silnrsi/font-bjcree/releases/download/v7.000/BJCree-7.000.zip |
| Release tag | `v7.000` (2026-02-11) |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field. Verified canonical: `silnrsi` is the SIL Non-Roman Script Initiative GitHub org, and BJCree is an SIL-published typeface. WebFetch of `https://github.com/silnrsi/font-bjcree` confirms the repository is active with default branch `main`, latest release `v7.000`. No newer fork or canonical alternative was found.

### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field. Mirrored upstream into the repo archive at `/home/fsanches/compartilhado/upstream_repos/repo_archive/silnrsi/font-bjcree.git` and verified:
- Commit `7476fb691e64eff8956faf2bd68911cb3e1c65b7` exists, currently HEAD of `main`.
- Author: LornaSIL <lorna_evans@sil.org>, 2026-03-11.
- Message: "Update makedocs to create temporary productsite directory."
- Tag `v7.000` points to an earlier commit (`5f901e4`, "Commit rebuilt documentation"), but the `references/` ttf binaries match across both — `7476fb691` is a docs-tooling commit on top.

### Binary verification
MD5 of `ofl/bjcree/BJCree-Regular.ttf` matches `references/BJCree-Regular.ttf` blob at the recorded commit (both `8bc789625a659af13ad20b11f47a632c`). All four shipped TTFs report `head.fontRevision = 7.0` and name table `Version 7.000`, consistent with the v7.000 release.

### Config YAML
No `config.yaml` (gftools-builder format) exists in the upstream repo. The repo uses SIL's own build pipeline (`smith` / `wscript`, `makedocs`, `preflight`). Sources are present (`source/BJCree.designspace`, `source/masters/BJCree-{Regular,Bold}.ufo/`), so a gftools-builder override is feasible but not currently provided. No override `config.yaml` in `ofl/bjcree/` either.

## Evidence

### METADATA.pb source block (current)
- `repository_url`: `https://github.com/silnrsi/font-bjcree`
- `commit`: `7476fb691e64eff8956faf2bd68911cb3e1c65b7`
- `archive_url`: `https://github.com/silnrsi/font-bjcree/releases/download/v7.000/BJCree-7.000.zip`
- `branch`: `main`
- `config_yaml`: (not set)

### google/fonts history
- Onboarding commit: `c9a51e82b` — "BJCree: Version 7.000 added" (Emma Marichal, 2026-03-26). Commit body explicitly cites `silnrsi/font-bjcree` at `7476fb691...`.
- Subsequent commits (article, primary_script, category fix, name normalization) — see "Recent upstream activity" below.

### Upstream repo archive
- Mirrored at `silnrsi/font-bjcree.git` (added 2026-04-27 by this investigation).
- Commit `7476fb691...` verified.
- v7.000 release tag verified.

## Initial state
- METADATA.pb already had a complete source block (URL, commit, branch, archive_url, files list) added at onboarding.
- No `upstream_info.md` existed.

## Actions taken
- Mirrored `silnrsi/font-bjcree` into the permanent repo archive.
- Verified commit `7476fb691` exists and produces the binaries currently shipped (MD5 match via `references/BJCree-Regular.ttf`).
- Confirmed font version 7.000 matches release tag.
- Confirmed no upstream `config.yaml`; documented SIL's smith-based build pipeline.
- Authored this `upstream_info.md`.

## Final state
- METADATA.pb source block is correct and verified — no changes required.
- No override `config.yaml` added; upstream uses SIL's smith pipeline (not gftools-builder).
- Repo is mirrored in the archive for long-term provenance.

## Recent upstream activity (post-onboarding, in google/fonts)
- `c9a51e82b` (Emma Marichal, 2026-03-26): BJCree: Version 7.000 added — initial onboarding from `silnrsi/font-bjcree@7476fb691`.
- `ed93d1d12` (Emma Marichal): added `article/ARTICLE.en_us.html`.
- `023c5eec4` (Emma Marichal): added `primary_script: "Cans"`.
- `b977700ca` (Emma Marichal, 2026-03-27): "BJCree: Change font category from SANS_SERIF to SERIF" — corrected category. The Latin glyphs in v7.000 are based on URW++ C059 (New Century Schoolbook), so SERIF is the correct classification per the FONTLOG.
- `e1ecf218b` (Emma Marichal, 2026-04-16): "Rename 'BJ Cree' to 'BJCree' in METADATA.pb" — display-name normalization to match the upstream font family name (`name` ID 1 = `BJCree`).

## Confidence
**High**: Repository URL canonical (silnrsi org); commit hash verified against upstream mirror; binaries confirmed identical (MD5) to upstream `references/`; font version (`7.000`) matches release tag.
