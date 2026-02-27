# Investigation Report: Halant

## Summary

Halant is a Devanagari + Latin serif family designed by Indian Type Foundry (Vivek Sadamate, Ninad Kale for Devanagari; Jonny Pinhorn for Latin). It was first added to Google Fonts in the initial commit (2015-03-07) and updated to v1.101 via PR #888 (2017-05-08). The upstream repository at `itfoundry/halant` contains UFO sources and a custom Python build system, but no gftools-builder config.yaml or designspace file. The repo has a single commit producing v2.000, while Google Fonts serves v1.101 -- meaning the v2.000 sources were never onboarded. The repo uses AFDKO's `makeotf` via a custom `build.py` script, not gftools-builder.

## Key Findings

| Field              | Value                                                     |
|--------------------|-----------------------------------------------------------|
| Family Name        | Halant                                                    |
| Designer           | Indian Type Foundry                                       |
| License            | OFL                                                       |
| Date Added         | 2014-08-27                                                |
| Repository URL     | https://github.com/itfoundry/halant                       |
| Commit Hash        | 5991cb7b8f338a3676e349dd6f3bb3358467cb69                  |
| Branch             | master                                                    |
| Config YAML        | None (custom build system, not gftools-builder compatible) |
| Source Types       | UFO (masters/Halant_0.ufo, masters/Halant_1.ufo)         |
| Weights            | Light, Regular, Medium, SemiBold, Bold                    |
| Google Fonts Ver.  | 1.101                                                     |
| Upstream Repo Ver. | 2.000                                                     |
| Status             | **missing_config**                                        |
| Confidence         | HIGH                                                      |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb on the main branch of google/fonts has no source block. A source block was added on the `sources_info_2026-02-25` branch (commit 9a14639f3) but has not yet been merged.

### Git History in google/fonts

The font was added in the initial commit `90abd17b4f` (2015-03-07) by Dave Crossland. Key subsequent changes:

1. **1e0cfec75** (2017-05-08) - Marc Foley: "hotfix-halant: v1.101 added (#888)" -- Updated all 5 TTFs, renamed Semibold to SemiBold in filenames, updated DESCRIPTION and METADATA.
2. **d774fc079** (2017-05-15) - Dave Crossland: "Rename various Semibold -> SemiBold" -- File rename.
3. **76adaf1d2** (2021-11-01) - m4rc1e: deploy commit (appears to be a GitHub Pages deploy, not a font update).

The current TTFs in google/fonts are version 1.101, last modified by PR #888.

### Upstream Repository Analysis

The repository `itfoundry/halant` is cached at `upstream_repos/fontc_crater_cache/itfoundry/halant/`. It contains:

- **Single commit**: `5991cb7b8f` (2014-11-21) by Liang Hai: "Compile 2.000"
- **Source files**: Two UFO masters (`masters/Halant_0.ufo`, `masters/Halant_1.ufo`) and five style instances (`styles/{Light,Regular,Medium,SemiBold,Bold}/font.ufo`)
- **Build system**: Custom `build.py` using AFDKO's `makeotf`, `UFOInstanceGenerator.py`, and internal `itf.py` module -- NOT gftools-builder compatible
- **Build output**: OTF files only (`build/Halant-{Light,Regular,Medium,SemiBold,Bold}.otf`), no TTFs
- **No config.yaml**, no designspace file

### Version Mismatch

Google Fonts has version 1.101, but the only commit in the upstream repo produces version 2.000. This means:
- The v1.101 fonts were likely compiled from an earlier state of the sources not captured in this repo, or from a different build process
- The v2.000 upstream sources have never been onboarded to Google Fonts
- The commit hash `5991cb7` is still the correct reference for the repo since it is the only commit

### Build Compatibility

The repo uses a custom build pipeline dependent on:
- AFDKO (Adobe Font Development Kit for OpenType)
- `UFOInstanceGenerator.py` from Adobe
- Custom Python modules (`itf.py`, `config.py`, `reference.py`)

This is NOT compatible with gftools-builder. Creating an override config.yaml would require a designspace file, which does not exist. The UFO sources could theoretically be used with a designspace, but creating one from scratch would require understanding the interpolation space (the two masters and five instances).

## Conclusion

The upstream repository is correctly identified. The commit hash `5991cb7b8f338a3676e349dd6f3bb3358467cb69` is the only commit in the repo. The sources use UFO format with a custom build pipeline, and no config.yaml or designspace file exists, making gftools-builder compilation non-trivial. A designspace would need to be authored to enable gftools-builder support.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/itfoundry/halant"
  commit: "5991cb7b8f338a3676e349dd6f3bb3358467cb69"
}
```

### Status: missing_config

The repository has UFO sources but uses a custom build system without config.yaml or designspace. Creating an override config would require authoring a designspace file to define the interpolation space.
