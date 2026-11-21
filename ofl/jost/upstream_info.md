# Investigation: Jost

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jost |
| Slug | jost |
| License Dir | ofl |
| Repository URL | https://github.com/indestructible-type/Jost |
| Commit Hash | 35f141c970538f1ed0f235789c19156b3ce2a762 |
| Config YAML | override config.yaml in google/fonts |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/indestructible-type/Jost"
  commit: "35f141c970538f1ed0f235789c19156b3ce2a762"
  files {
    source_file: "fonts/variable/Jost[wght].ttf"
    dest_file: "Jost[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Jost-Italic[wght].ttf"
    dest_file: "Jost-Italic[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

The fonts were added to google/fonts on 2021-09-22 via commit `91b26e2e0` (PR #3831, "Jost: Version 3.710 added"). The PR commit message states multiple attempts were made and references commits from `https://github.com/aaronbell/Jost`:
- First attempt: `d4c4291c3a8b759c0823f15416582f5b6bf6c414`
- Final commit used: `f5029c3f20e310ef9f7a9c9c08fd808fd707db82` ("Updating Copyright string", 2021-09-10)

The repository was later renamed: `aaronbell/Jost` → `indestructible-type/Jost`. Both the `aaronbell` commits (`d4c4291c` and `f5029c3f`) were confirmed to exist in the `indestructible-type/Jost` local clone (same git history, just renamed owner).

The commit hash currently in METADATA.pb (`35f141c9`) was set by commit `83026eb5b` ("sources info for Jost: Version 3.710 (PR #3831)"). The commit `35f141c9` ("Create inUse.md", 2021-02-20) predates the actual onboarding commit `f5029c3f` (2021-09-10). This means the current METADATA.pb has an **older** commit than the one actually used for onboarding.

The upstream repository at `https://github.com/indestructible-type/Jost` is cached at `upstream_repos/fontc_crater_cache/indestructible-type/Jost` with 120 commits of history. No `config.yaml` exists in the upstream repo.

An override `config.yaml` was created in the google/fonts family directory by commit `83026eb5b`, containing:
```yaml
buildVariable: true
sources:
  - sources/designspace/jostGF.designspace
  - sources/designspace/jostGF-Italic.designspace
  - sources/designspace/jost.designspace
```

## Conclusion

The repository URL is correct (pointing to the renamed repo `indestructible-type/Jost`). However, the commit hash `35f141c9` is wrong — it predates the actual onboarding. The correct commit is `f5029c3f20e310ef9f7a9c9c08fd808fd707db82` (as stated in PR #3831). An override `config.yaml` already exists in the google/fonts family directory. The commit hash needs to be corrected in METADATA.pb.
