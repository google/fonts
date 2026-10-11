# Baloo Paaji 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete
- **Designer**: Ek Type

## Source Data

| Field | Value |
|---|---|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | `da523dfa21aa0e376253d61c21e39146dc55702a` |
| Config YAML | `builder/BalooPaaji2.yaml` |
| Branch | master |

## Investigation

### Repository URL

The METADATA.pb `source` block listed `repository_url` as `https://github.com/yanone/Baloo2-Variable`. This was verified as the correct upstream repository. The cached clone at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable` confirmed the remote URL matches.

Note: The copyright string in METADATA.pb references `https://github.com/EkType/Baloo2`, which is the original Baloo project by Ek Type. The variable font version was developed in the separate `yanone/Baloo2-Variable` repository by Yanone (post@yanone.de). An earlier version of the source block in METADATA.pb had incorrectly pointed to `https://github.com/EkType/Baloo2-Variable`; this was corrected in commit `6affde4be` (2025-09-24) to point to `yanone/Baloo2-Variable`.

### Commit Hash

The referenced commit `da523dfa21aa0e376253d61c21e39146dc55702a` was verified to exist in the upstream repository. It was authored on 2021-10-28 by Yanone with the message "Update BalooTammudu2[wght].ttf". This commit updated a different font binary (BalooTammudu2), not BalooPaaji2 itself.

The last commit that directly modified `fonts/variable/BalooPaaji2[wght].ttf` was `fae6801` (2021-10-28, three minutes earlier), with the message "Update BalooPaaji2[wght].ttf". Between `fae6801` and `da523df`, there were three intermediate commits updating other Baloo family binaries (BalooTamma2, BalooThambi2, BalooTammudu2). No changes to BalooPaaji2's sources or config occurred in these intermediate commits.

The google/fonts onboarding commit `54710b794` (2021-11-03, PR #3983) explicitly referenced this commit hash via gftools-packager: "Baloo Paaji 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa21aa0e376253d61c21e39146dc55702a." This confirms the hash used during onboarding, even though it was a batch update across multiple Baloo families and `da523df` was simply the latest commit at the time of packaging.

### Config YAML

The config file at `builder/BalooPaaji2.yaml` was confirmed to exist at the referenced commit. Its contents:

```yaml
sources:
  - ../sources/BalooPaaji2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The source file `sources/BalooPaaji2.glyphs` was also verified to exist at the referenced commit. No local override `config.yaml` existed in the google/fonts family directory (`ofl/baloopaaji2/`).

### Newer Upstream Commits

There were 8 commits after `da523df` on the master branch, including merge commits and a version bump to 1.701. These later changes were not part of the google/fonts onboarding and would require a separate review process.

## Conclusion

All source metadata was complete and correct. The repository URL pointed to the valid upstream repository (`yanone/Baloo2-Variable`). The commit hash matched the one used by gftools-packager during the Version 1.700 onboarding (PR #3983). The config file `builder/BalooPaaji2.yaml` existed at the referenced commit and contained a valid gftools-builder configuration pointing to `sources/BalooPaaji2.glyphs`. No override config.yaml was needed since the upstream repository already contained the config file. Status: **complete**.
