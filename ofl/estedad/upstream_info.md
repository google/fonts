# Estedad

**Status**: `complete`
**Date**: 2026-04-27
**Designer**: Amin Abedi, Fontamin
**License**: OFL
**METADATA.pb**: `ofl/estedad/METADATA.pb`
**Model**: Claude Opus 4.7 (1M context)

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/aminabedi68/Estedad |
| Commit | `69e879f78a4a1c7c4594baf7da13ba1c9f65ffd3` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field. Verified canonical: the upstream is owned by Amin Abedi (`aminabedi68`), whose GitHub email is `aminabedi68@gmail.com`. The font's `name` ID 9 (Designer) reads "Amin Abedi", confirming the repo owner is the actual designer. The studio "Fontamin" is listed as sole entry in `AUTHORS.txt` (`Fontamin <hifontamin@gmail.com>`). No third-party fork is more canonical; releases continue to be cut from this repo (latest: `Estedad-v8.5`, 2026-03-20).

### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field. The onboarding commit message (`55ca157f7` "Estedad: Version 8.5 added") explicitly cites this hash. Verified upstream: it is the merge commit of PR #38 ("Add Estedad", from `emmamarichal/master`), authored 2026-03-31T23:48:19Z by Amin Abedi.

### Config YAML
Found `sources/config.yaml` in upstream repository at the recorded commit hash. Configuration uses `Estedad.glyphs` as source, `wght` axisOrder, with full STAT table covering 9 named instances Thin (100) through Black (900).

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/aminabedi68/Estedad`
- `commit`: `69e879f78a4a1c7c4594baf7da13ba1c9f65ffd3`
- `branch`: `master`
- `config_yaml`: `sources/config.yaml` (added 2026-04-27 by this commit)

### Font binary verification
The shipping binary `ofl/estedad/Estedad[wght].ttf` (328340 bytes, md5 `284743ae983adab00bdcc5148669cf27`) is **byte-identical** to `fonts/variable/Estedad[wght].ttf` at upstream commit `69e879f78`. Font metadata confirms the version:
- `head.fontRevision`: `8.5`
- `name` ID 5: `Version 8.5`
- `name` ID 3: `8.5;amin;Estedad-Regular`
- `name` ID 9 (Designer): `Amin Abedi`
- `name` ID 0 (Copyright): `Copyright 2026 The Estedad Project Authors (https://github.com/aminabedi68/Estedad)`

### Upstream commit metadata
- Author: Amin Abedi `<aminabedi68@gmail.com>`
- Date: 2026-03-31T23:48:19Z
- Subject: "Merge pull request #38 from emmamarichal/master" (description: "Add Estedad")
- Parents: `97d10596b3a260c040336199c2e83a6305d37663`, `c0514924d2cbca83895bac41d86c179564418056`

### Recent upstream/main activity (post-onboarding)
- `55ca157f7` (Emma Marichal, 2026-04-01) — "Estedad: Version 8.5 added": initial onboarding of v8.5 binaries from upstream commit `69e879f78`.
- `5dd7677db` (Emma Marichal, 2026-04-03) — "Reorder designer name in METADATA.pb": adjusted `designer:` field; current value `"Amin Abedi, Fontamin"` matches the upstream evidence (Amin Abedi as primary designer per font name table; Fontamin as studio per AUTHORS.txt).
- `b869de54c` (Emma Marichal, 2026-04-24) — "Add Arabic subset to METADATA.pb": added `subsets: "arabic"` (current METADATA.pb confirmed to contain it).

None of those three commits required source-block changes — `repository_url` and `commit` were already correctly recorded by the onboarding `gftools-packager` run.

## Initial state
- METADATA.pb contained a complete `source { ... }` block (repository_url, commit, branch, file mappings) but `config_yaml` was not set.
- No `upstream_info.md` existed for this family.
- No override `config.yaml` in `ofl/estedad/`.

## Actions taken
- Validated the existing `repository_url` is the canonical upstream (designer `aminabedi68` matches font name table; releases continue to ship from this repo).
- Validated the existing `commit` hash by md5-comparing the upstream font binary at that commit against the binary shipping in google/fonts — byte-identical match (328340 bytes, md5 `284743ae...`).
- Located `sources/config.yaml` in the upstream repo at the recorded commit; added `config_yaml: "sources/config.yaml"` to the source block so gftools-builder can use it directly.
- Created this `upstream_info.md` documenting provenance.

## Final state
- Provenance fully documented.
- Source block now includes `config_yaml: "sources/config.yaml"`. All other fields verified correct.
- No override `config.yaml` is required — upstream provides a working one.

## Open follow-up
- Mirror `aminabedi68/Estedad` into `/home/fsanches/compartilhado/upstream_repos/repo_archive/aminabedi68/` when disk space permits (currently 21 GB free, just above the 15 GB threshold).

## Confidence

**High**: repository_url verified canonical via designer/owner cross-check; commit hash verified by md5-identical font binary at that commit; upstream `config.yaml` confirmed to exist at recorded commit.
