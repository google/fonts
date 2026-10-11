# Investigation: JetBrains Mono

## Summary

| Field | Value |
|-------|-------|
| Family Name | JetBrains Mono |
| Slug | jetbrains-mono |
| License Dir | ofl |
| Repository URL | https://github.com/JetBrains/JetBrainsMono |
| Commit Hash | 19371302b95d218af43299bce79ddbddd0bc364d |
| Config YAML | sources/config.yaml |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/JetBrains/JetBrainsMono"
  commit: "19371302b95d218af43299bce79ddbddd0bc364d"
  files {
    source_file: "fonts/variable/JetBrainsMono[wght].ttf"
    dest_file: "JetBrainsMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/JetBrainsMono-Italic[wght].ttf"
    dest_file: "JetBrainsMono-Italic[wght].ttf"
  }
  ...
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The font was added to google/fonts on 2020-11-18 via commit `2e05c1cf0` (PR #2817, "JetBrains Mono: Version 2.211 added"). The PR commit message states: "JetBrains Mono Version 2.211 taken from the upstream repo https://github.com/JetBrains/JetBrainsMono at commit https://github.com/JetBrains/JetBrainsMono/commit/6a005ca77d9202aa12fc277aefa8f5bb4eb7f0cd."

The commit hash currently in METADATA.pb (`19371302b95d218af43299bce79ddbddd0bc364d`) was set by the "[Batch 1/4] port info from fontc_crater targets list" commit (`19cdcec59`, 2025-03-31) which imported commit hashes from fontc_crater's target.json. The commit `19371302` is dated January 31, 2025 (subject: "Merge pull request #714 from petryshkaCODE/Fix-typo"), which is well after the 2020 onboarding.

The local clone at `upstream_repos/fontc_crater_cache/JetBrains/JetBrainsMono` was fetched with `--depth 1`, so only the most recent commit (`19371302`) is available. The original onboarding commit `6a005ca77` cannot be verified from this shallow clone.

The upstream repository contains `sources/config.yaml` with the full gftools-builder configuration for JetBrains Mono (specifying `JetBrainsMono.glyphs` and `JetBrainsMono-Italic.glyphs` sources). This config was verified to exist in the shallow clone.

## Conclusion

The repository URL is correct. However, the commit hash `19371302` in METADATA.pb is incorrect — it points to a 2025 typo-fix commit, not the 2020 onboarding commit. The actual onboarding commit was `6a005ca77d9202aa12fc277aefa8f5bb4eb7f0cd` (as stated in PR #2817). The commit hash needs to be corrected to `6a005ca77d9202aa12fc277aefa8f5bb4eb7f0cd`. The `config_yaml` field correctly points to `sources/config.yaml`.
