# Investigation: Francois One

## Summary

| Field | Value |
|---|---|
| **Family Name** | Francois One |
| **Designer** | Vernon Adams |
| **License** | OFL |
| **Repository URL** | https://github.com/googlefonts/francoisoneFont |
| **Commit** | `09ca2d148ed2ae88b0b89b5309f5eedd1daa2e0c` |
| **Config YAML** | `sources/config.yaml` |
| **Status** | complete |
| **Confidence** | HIGH |

## METADATA.pb Current State

The METADATA.pb already has a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/francoisoneFont"
  commit: "09ca2d148ed2ae88b0b89b5309f5eedd1daa2e0c"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

### Upstream Repository: googlefonts/francoisoneFont

- **Created**: March 13, 2017 (not a fork)
- **Description**: "Francois One Font by Vernon Adams"
- **Commit count**: 30 commits total
- **Default branch**: `main`
- **Latest commit**: `09ca2d1` (April 4, 2024) by Simon Cozens -- "Add very simple builder config.yaml"

### Source Files

The repository contains `.glyphs` sources for gftools-builder:

- `sources/FrancoisOne.glyphs` -- the main source file (last modified in commit `3fa7536`, Oct 5, 2016)
- `sources/config.yaml` -- gftools-builder config (added in commit `09ca2d1`, April 4, 2024)

The config.yaml is minimal:
```yaml
sources:
  - FrancoisOne.glyphs
```

### Binary Verification

The font binary in google/fonts (`FrancoisOne-Regular.ttf`, 79,356 bytes, Version 2.000) matches exactly the binary in the upstream repo at `fonts/FrancoisOne-Regular.ttf`:

- SHA256: `700fb5e4a5b6edb14dde2dcd481e5a9cac14281579cf42500170bae7cddd3609`

The binary was first added to the upstream repo in commit `3fa7536` (Oct 5, 2016) by Marc Foley ("fonts | sources: fixed meta data according to checklist.md") and has not been modified since.

## Google Fonts Commit History

| Commit | Date | Author | Description |
|---|---|---|---|
| `90abd17` | Mar 7, 2015 | Dave Crossland | Initial commit (v1.000) |
| `34f4f3e` | Dec 2, 2016 | Marc Foley | v2.000 added (PR #429) |
| `9f4b3e9` | Feb 22, 2023 | Emma Marichal | gftools-packager v3.000 update (PR #5919) |
| `e79f34c` | Jun 16, 2023 | Rosalie Wagner | Revert of v3.000 update (PR #6384) |
| `c8a4f85` | Jan 14, 2024 | Simon Cozens | Added source block to METADATA.pb |
| `19cdcec` | Mar 31, 2025 | Felipe Sanches | Added commit hash and config_yaml from fontc_crater |

### Key Events

1. **v1.000 (2015)**: Original font added via initial repository import.

2. **v2.000 (Dec 2016, PR #429)**: Marc Foley updated the font to v2.000. The PR description simply says "francoisone: v2.000 added" and references Thomas Jockin. The binary was compiled from the `.glyphs` source file in the googlefonts/francoisoneFont upstream repo at or around commit `3fa7536`.

3. **v3.000 attempt (Feb 2023, PR #5919)**: Emma Marichal submitted a v3.000 update via gftools-packager, sourced from `Fonthausen/francoisoneFont` (a fork chain: googlefonts -> dsweetnich -> anna-richard -> aoifemooney -> Fonthausen) at commit `10ee754`. This was merged on Feb 23, 2023.

4. **v3.000 revert (Jun 2023, PR #6384)**: Rosalie Wagner reverted the v3.000 update with the explanation: "Since we onboard Freeman (#6241) as the update of Francois, and this update is too close to Freeman, I revert this PR to go back to original files (in sync with what is in prod)." The Fonthausen/francoisoneFont repository has since been deleted (returns 404).

5. **Source block added (Jan 2024)**: Simon Cozens added the `repository_url` to METADATA.pb pointing to googlefonts/francoisoneFont.

6. **Config + commit added (Mar 2025)**: The commit hash and config_yaml were ported from the fontc_crater targets list.

## Commit Hash Analysis

The referenced commit `09ca2d1` (April 4, 2024) is the latest commit in the repository. This is the commit where Simon Cozens added the `config.yaml` file. The source `.glyphs` file itself was last modified in commit `3fa7536` (Oct 5, 2016) by Marc Foley.

Between the binary-producing commit (`3fa7536`) and the referenced commit (`09ca2d1`), the changes were:
- `20d782d` (Oct 5, 2016): Updated AUTHOR.txt and CONTRIBUTORS.txt
- `9a3ff8e` / `c512be5` (Sep 26, 2016): Vietnamese fix by CrystalType (predates the binary commit)
- `f93620c` (Nov 2, 2016): Removed Reserved Font Names from OFL.txt
- `09ca2d1` (Apr 4, 2024): Added config.yaml

None of these changes affect the .glyphs source file or the compiled binary. Using `09ca2d1` as the reference commit is appropriate because it is the latest state of the repo and includes the config.yaml needed for gftools-builder.

## Fork Chain

The repository has an interesting fork chain:
1. `googlefonts/francoisoneFont` (source of truth, created Mar 2017)
2. `dsweetnich/francoisoneFont` (fork, May 2017 -- spacing/kerning work)
3. `anna-richard/francoisoneFont` (fork, Sep 2017 -- kerning work, 2017)
4. `aoifemooney/francoisoneFont` (fork, Jan 2018 -- kerning fixes, 2018)
5. `Fonthausen/francoisoneFont` (fork, Feb 2023 -- v3.000 update attempt, now deleted)

The fork chain contains significant kerning/spacing work done in 2017-2018 by dsweetnich, anna-richard, and aoifemooney. This work was eventually used for the v3.000 update attempt (PR #5919), which was reverted. None of these forks affect the currently-serving v2.000 binary.

## Conclusion

The METADATA.pb source block is complete and correct:
- **Repository URL**: `https://github.com/googlefonts/francoisoneFont` -- the canonical upstream repo containing v2.000 sources
- **Commit**: `09ca2d148ed2ae88b0b89b5309f5eedd1daa2e0c` -- latest commit, includes the config.yaml and matches the serving binary
- **Config YAML**: `sources/config.yaml` -- present in the repo at the referenced commit

No changes needed.
