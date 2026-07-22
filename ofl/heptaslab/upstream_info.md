# Investigation Report: Hepta Slab

## Summary

Hepta Slab is a variable weight slab-serif revival designed by Mike LaGattuta. The font was initially onboarded from `mjlagattuta/Hepta-Slab` at commit `4401d23` (v1.100) and later updated by Aaron Bell from his fork `aaronbell/Hepta-Slab` at commit `8dd0f95` (v1.102). The current METADATA.pb source block points to `mjlagattuta/Hepta-Slab` but is missing a commit hash, and the `files` path references `fonts/variable/HeptaSlab[wght].ttf` which no longer exists at the tip of the `mjlagattuta` repo. The upstream repo has a `.glyphs` source file but no `config.yaml`; an override `config.yaml` already exists in the google/fonts family directory.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Hepta Slab |
| Designer           | Mike LaGattuta |
| Repository URL     | https://github.com/mjlagattuta/Hepta-Slab |
| Upstream Commit    | `4401d23f516b412f1b8472fe705b37b8712b2ecd` (initial onboarding, v1.100) |
| Update Commit      | `8dd0f95d35d6e691e3006e7a32aaef0cdb84acc9` (from `aaronbell/Hepta-Slab` fork, v1.102) |
| Config YAML        | Override `config.yaml` in google/fonts (references `sources/HeptaSlab.glyphs`) |
| Source Files       | `sources/HeptaSlab.glyphs` |
| Status             | needs_correction |
| Confidence         | MEDIUM |

## Investigation Details

### Upstream Repository

The upstream repository is https://github.com/mjlagattuta/Hepta-Slab. It is cached locally at `upstream_repos/fontc_crater_cache/mjlagattuta/Hepta-Slab/`. The remote is valid and the repo has 111 commits on the `master` branch.

The repo contains:
- `sources/HeptaSlab.glyphs` -- Glyphs source file
- `fonts/HeptaSlab-VF.ttf` -- Variable font binary
- `fonts/HeptaSlabHairline-Regular.ttf` -- Hairline standalone binary
- No `config.yaml` or `config.yml`

### Onboarding History

**Initial onboarding (v1.100)**:
- google/fonts commit: `593c6a0b28cd09e0941c12d8fc5dbffcaf12f481` (2019-07-30)
- Author: Mike LaGattuta, committed by Marc Foley
- Commit message: "Taken from the upstream repo https://github.com/mjlagattuta/Hepta-Slab at commit https://github.com/mjlagattuta/Hepta-Slab/commit/4401d23f516b412f1b8472fe705b37b8712b2ecd"
- Commit `4401d23` exists in the `mjlagattuta` repo and is dated 2019-02-11 ("Add macro for scaling metrics keys"), the HEAD of the master branch

**Update (v1.102, PR #3785)**:
- google/fonts commit: `acfa4ad65f631d60c3473f1a2726716aa1467e0f` (2021-09-30)
- Author: Aaron Bell
- Commit message references: "upstream repo https://github.com/aaronbell/Hepta-Slab at commit https://github.com/aaronbell/Hepta-Slab/commit/8dd0f95d35d6e691e3006e7a32aaef0cdb84acc9"
- Commit `8dd0f95` does NOT exist in the `mjlagattuta/Hepta-Slab` repo -- it is from Aaron Bell's fork (`aaronbell/Hepta-Slab`)
- The `aaronbell/Hepta-Slab` fork is NOT in the local cache

### Source Block Issues

The current METADATA.pb source block has several issues:

1. **Missing commit hash**: No `commit` field in the source block
2. **Incorrect files path**: References `fonts/variable/HeptaSlab[wght].ttf` but this path does not exist at HEAD of `mjlagattuta/Hepta-Slab`. The `fonts/variable/` directory existed in older commits (with `HeptaSlab-VF.ttf`, not `HeptaSlab[wght].ttf`) but was removed in commit `39e6a5b` (2019-02-11).
3. **Fork discrepancy**: The most recent font update came from `aaronbell/Hepta-Slab` (a fork), but the source block points to the original `mjlagattuta/Hepta-Slab`. The fork likely has a different directory structure with the `fonts/variable/HeptaSlab[wght].ttf` naming.

### Config YAML

An override `config.yaml` was added to the google/fonts family directory in commit `5ddf312e6` (2026-02-20) with the content:
```yaml
sources:
  - sources/HeptaSlab.glyphs
```

This correctly references the `.glyphs` source file in the `mjlagattuta/Hepta-Slab` repo.

### File Path History

The `fonts/variable/` directory in the `mjlagattuta` repo contained `HeptaSlab-VF.ttf` (not `HeptaSlab[wght].ttf`) from commits `bb93812` through `39e6a5b`, after which the variable font was moved to `fonts/HeptaSlab-VF.ttf`. The `HeptaSlab[wght].ttf` filename convention likely came from the `aaronbell/Hepta-Slab` fork, which cannot be verified without access to that repository.

## Conclusion

**Status: needs_correction**

The source block needs correction:
1. The `commit` field should be added. Since the font was last updated from `aaronbell/Hepta-Slab`, the situation is complex -- the `files` block references paths from that fork, not from `mjlagattuta/Hepta-Slab`. If we keep pointing to `mjlagattuta/Hepta-Slab`, the commit should be `4401d23` (the initial onboarding commit, which is HEAD of the repo), but then the `files` path is incorrect.
2. The `files` source_file path `fonts/variable/HeptaSlab[wght].ttf` does not exist in `mjlagattuta/Hepta-Slab` at any commit. This path likely came from the `aaronbell/Hepta-Slab` fork.
3. Since the override config.yaml is already in place and gftools-builder will compile from `sources/HeptaSlab.glyphs`, the `files` block (which maps pre-compiled binaries) could potentially be removed in favor of a build-from-source approach.
4. Investigation of the `aaronbell/Hepta-Slab` fork would clarify the v1.102 update commit, but disk space constraints prevent cloning it.
