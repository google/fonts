# Investigation: Briem Hand

## Summary

| Field | Value |
|-------|-------|
| Family Name | Briem Hand |
| Slug | briem-hand |
| License Dir | ofl |
| Repository URL | https://github.com/SorkinType/Briem-Hand |
| Commit Hash | 7b991840508c9a90632354034ed0a72002836c05 |
| Config YAML | sources/config.yaml |
| Status | needs_correction |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/SorkinType/Briem-Hand"
  commit: "7b991840508c9a90632354034ed0a72002836c05"
  archive_url: "https://github.com/SorkinType/Briem-Hand/releases/download/v1.004/Briem-Hand-v1.004.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/BriemHand[wght].ttf"
    dest_file: "BriemHand[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Git History in google/fonts

The font directory has been updated multiple times:

1. `379bcfca1` (2024-05-16) — `One more missing join (bf)` — direct TTF edit
2. `d619ba521` (after 2024-03-28) — `And again` — direct TTF edit
3. `2beab1628` (after 2024-03-28) — `Fix astroke` — direct TTF edit
4. `099159dd0` (2023-11-30) — `[gftools-packager] Briem Hand: Version 1.002 added`
5. `2f2518247` (2024-03-28) — `Briem Hand: Version 1.003 added` (upstream commit: `bd68ecf`)
6. `6df879b16` (2024-03-27) — `Briem Hand: Version 1.003 added` (upstream commit: `24564101f1`)
7. `eef42261c` (2024-03-27) — `Briem Hand: Version 1.003 added` (upstream commit: `3f9aa7c9`)

The Version 1.003 update went through multiple attempts (commits `eef42261c`, `6df879b16`, `2f2518247`). The final accepted commit `2f2518247` references upstream commit `bd68ecf84950b0c2e975716cce88c1b43b99d138` (dated 2024-03-28, "Remove axis mappings custom parameter").

After the 1.003 packager update, three manual TTF edits were made directly to `ofl/briemhand/BriemHand[wght].ttf` without a gftools-packager run (commits `2beab1628`, `d619ba521`, `379bcfca1`).

### METADATA.pb Commit Hash History

The METADATA.pb was modified by commit `19cdcec59` (`[Batch 1/4] port info from fontc_crater targets list`, 2025-03-31), which changed the commit field from `68fedd7eb5d65c2c1490300719ef8b1fa51fbcd5` to `7b991840508c9a90632354034ed0a72002836c05` and added `config_yaml: "sources/config.yaml"`. This batch update ported data from the fontc_crater targets list.

Commit timeline analysis:
- `bd68ecf` (2024-03-28): actual upstream commit used for the 1.003 packager run
- `68fedd7` (2024-05-10): "Bump version to 1.004" — set as METADATA.pb commit before the batch update, but NEWER than the actual 1.003 onboarding
- `7b991840` (2024-10-30): "Missing metrics" — current METADATA.pb commit, MUCH NEWER than the 1.003 onboarding

The `archive_url` points to `v1.004`, which corresponds to commit `68fedd7`, not the actual onboarding commit.

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/SorkinType/Briem-Hand`. All three commits (`7b991840`, `68fedd7`, `bd68ecf`) exist and were verified. The `sources/config.yaml` file exists at all three commits.

The `sources/config.yaml` is a complex fontprimer-based recipe that builds multiple variants of Briem Hand (variable, statics, and "Classic Briem Guides" educational variants).

### Assessment

The current METADATA.pb commit (`7b991840`, October 2024) is significantly newer than the actual onboarding commit. The TTFs currently in google/fonts were based on the 1.003 packager run (commit `bd68ecf`, March 2024) plus subsequent manual edits. The `archive_url` references v1.004 which does not correspond to the actual onboarded version.

This situation is complex:
- The manual post-packager edits (commits `2beab1628`, `d619ba521`, `379bcfca1`) mean the current TTFs don't correspond to any single upstream commit
- The `config_yaml` field is correctly set to `sources/config.yaml` (which exists at the referenced commit)
- The commit hash needs correction but the "correct" hash is ambiguous given the post-packager manual edits

## Conclusion

The source block needs correction. The commit hash `7b991840` (October 2024) is newer than the actual onboarding. The most defensible onboarding commit is `bd68ecf84950b0c2e975716cce88c1b43b99d138` (March 28, 2024), which is the upstream commit explicitly referenced in the final accepted 1.003 packager commit. However, the subsequent manual TTF edits to google/fonts (through May 2024) are not reflected in any upstream commit. This should be flagged for review by Eben Sorkin (SorkinType), the font engineer who managed the onboarding.
