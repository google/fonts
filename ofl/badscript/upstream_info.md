# Bad Script

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Designer**: Gaslight (Roman Shchyukin)

## Source Data

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| repository_url   | https://github.com/alexeiva/badscript                    |
| commit           | dca2962433a2b5817f1e716d6731a743440fbd79                 |
| config_yaml      | sources/config.yaml                                      |
| branch           | master                                                   |
| family_dir       | ofl/badscript                                            |

## Repository URL Verification

The repository URL `https://github.com/alexeiva/badscript` was verified as accessible. The remote lists `refs/heads/master` at `d0e3e937`. The cached clone at `upstream_repos/fontc_crater_cache/alexeiva/badscript` matched the remote after fetch. The METADATA.pb `source` block already contained this URL, added by Emma Marichal in commit `0827c33e` (2024-11-08) as part of PR #8476.

## Commit Verification

The commit `dca2962433a2b5817f1e716d6731a743440fbd79` was verified as present in the upstream repository. It is a merge commit dated 2024-11-08 with the message "Merge pull request #6 from emmamarichal/master". This merge brought in exported fonts (reorganized from `fonts/BadScript-Regular.ttf` to `fonts/ttf/BadScript-Regular.ttf` and added OTF/WOFF2 variants) and updated `.glyphs` sources.

The commit hash was explicitly referenced in the google/fonts commit body: "Taken from the upstream repo https://github.com/alexeiva/badscript at commit dca2962433a2b5817f1e716d6731a743440fbd79." This commit was introduced in google/fonts by Emma Marichal in commit `0827c33e` and merged via PR #8476 on 2024-11-13 by Viviana Monsalve.

Binary verification confirmed an exact match: the TTF file at `fonts/ttf/BadScript-Regular.ttf` in the upstream repo at commit `dca2962` has SHA-256 hash `40ec737eee65ec4efbc24ae636fa31d7d84d1ccca83ab54cd555edb72cb3eaf0`, which is identical to the file in `ofl/badscript/BadScript-Regular.ttf` in google/fonts.

Two newer commits exist on upstream master after the referenced commit (`819ce99` and `d0e3e93`, both from 2025-05-21, "fixes #7" and "regenerated fonts v2.005"). These post-date the google/fonts merge and are not yet incorporated.

## Config Verification

The upstream repository contained `sources/config.yaml` at the referenced commit with the following content:

```yaml
sources:
  - BadScript.glyphs
familyName: Bad Script
cleanUp: true
```

This is a valid gftools-builder configuration referencing the Glyphs source file `sources/BadScript.glyphs`, which was also verified to exist at the referenced commit. The `config_yaml: "sources/config.yaml"` field in METADATA.pb was added by the Batch 1/4 commit (`19cdcec5`, 2025-03-31) which ported data from the fontc_crater targets list. No override config.yaml was needed since the upstream repo already had one.

## Provenance History

| Date       | Event                                              | Commit/PR                   |
|------------|----------------------------------------------------|-----------------------------|
| 2015-03-07 | Initial commit in google/fonts                     | `90abd17b`                  |
| 2016-10-06 | v2.000 added (by m4rc1e)                           | `b44c3c58`                  |
| 2024-11-08 | Update to Version 2.000 from upstream (by emmamarichal) | `0827c33e` (PR #8476) |
| 2024-11-13 | PR #8476 merged by vv-monsalve                     | `d2ebba07`                  |
| 2025-03-31 | config_yaml and primary_script added (Batch 1/4)   | `19cdcec5`                  |

## Conclusion

All source metadata for Bad Script was already complete and correct in METADATA.pb. The repository URL, commit hash, branch, file mappings, and config_yaml path were all verified. The commit hash `dca2962` matched the binary TTF exactly. The upstream repo contained a valid `sources/config.yaml` at the referenced commit, so no override was required. No changes to METADATA.pb are needed.
