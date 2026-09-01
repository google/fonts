# Investigation Report: Heebo

## Summary

Heebo is a variable Hebrew/Latin sans-serif typeface designed by Oded Ezer. It was updated to Version 3.100 on 2023-11-24 by Emma Marichal using gftools-packager. The upstream repository, config.yaml, and commit hash are all well-documented and verified. The source block in METADATA.pb is complete and correct.

## Key Findings

| Field               | Value |
|---------------------|-------|
| **Family Name**     | Heebo |
| **Designer**        | Oded Ezer |
| **Repository URL**  | https://github.com/OdedEzer/heebo |
| **Commit Hash**     | `76c7d538568d3e6d7f052a12c5675c84430df25f` |
| **Config YAML**     | `sources/config.yaml` |
| **Branch**          | `master` |
| **Status**          | **complete** |
| **Confidence**      | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/heebo/METADATA.pb` contains a fully populated source block with:
- `repository_url`: `https://github.com/OdedEzer/heebo`
- `commit`: `76c7d538568d3e6d7f052a12c5675c84430df25f`
- `branch`: `master`
- `config_yaml`: `sources/config.yaml`
- File mappings for OFL.txt and `Heebo[wght].ttf`

### Git History in google/fonts

The font has a long history in google/fonts. The most recent binary update was via commit `804ab16a8ff8ac0072e7c5ecc34e381b4a710177` on 2023-11-24:
```
[gftools-packager] Heebo: Version 3.100 added
* Heebo Version 3.100 taken from the upstream repo
  https://github.com/OdedEzer/heebo at commit
  https://github.com/OdedEzer/heebo/commit/76c7d538568d3e6d7f052a12c5675c84430df25f.
```

This commit was authored by Emma Marichal (bonjour@emmamarichal.fr). It updated the variable font binary, METADATA.pb, OFL.txt, and added upstream.yaml.

Previous binary updates:
- `902785a6e` (2020-06-03): Heebo v3.001 added (#2482)
- `62c8640cc` (2020-05-06): Heebo v3.000 added (#2444)

The `config_yaml` field was added later in commit `19cdcec59` (2025-03-31) as part of a batch port from fontc_crater targets.

### Upstream Repository Verification

The cached repository at `fontc_crater_cache/OdedEzer/heebo/` has been verified:
- Remote: `https://github.com/OdedEzer/heebo`
- Current branch: `master`
- The repository contains exactly one commit: `76c7d538568d3e6d7f052a12c5675c84430df25f`
- This commit is "Merge pull request #35 from emmamarichal/master" titled "Fixed vavvav-hb yodyod-hb (added anchors)", dated 2023-11-23

The single-commit nature of the cached repo suggests it was cloned with `--depth 1` at the referenced commit, or the upstream repo has been force-pushed/squashed. Regardless, the referenced commit is confirmed to be the HEAD of the master branch.

### Config YAML Verification

The file `sources/config.yaml` exists at the referenced commit and contains:
```yaml
sources:
  - Heebo.glyphs
axisOrder:
  - wght
familyName: Heebo
stat:
  Heebo[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Thin
      value: 100
    ...
    - name: Black
      value: 900
```

The source file `sources/Heebo.glyphs` is present. The output directory `fonts/variable/` contains the expected `Heebo[wght].ttf`.

### Source Files

- `sources/Heebo.glyphs` -- Glyphs source file
- `sources/config.yaml` -- gftools-builder config
- `sources/old ufos/` -- Legacy UFO sources (directory present)

### Onboarding Timeline

- 2016-06-20: Originally added to Google Fonts
- 2020-05-06: Updated to v3.000
- 2020-06-03: Updated to v3.001
- 2023-11-23: PR #35 merged in upstream (commit `76c7d53`)
- 2023-11-24: Updated to v3.100 in google/fonts by Emma Marichal

The gftools-packager commit message explicitly references the upstream commit hash, and the timeline is consistent (upstream merge one day before google/fonts update).

## Conclusion

The source block in METADATA.pb is complete and fully verified. The repository URL, commit hash, and config_yaml path are all correct. The font was built from `sources/Heebo.glyphs` using the gftools-builder configuration at `sources/config.yaml`. No changes needed.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/OdedEzer/heebo"
  commit: "76c7d538568d3e6d7f052a12c5675c84430df25f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Heebo[wght].ttf"
    dest_file: "Heebo[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```
