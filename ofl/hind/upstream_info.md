# Investigation Report: Hind

## Summary

Hind is a Devanagari and Latin sans-serif font family designed by Indian Type Foundry (Manushi Parikh), first added to Google Fonts in 2015 and updated to v2.001 in May 2017 (PR #890). The upstream repository at `https://github.com/itfoundry/hind` uses UFO source files with a custom build system (AFDKO-based `build.py` with UFOInstanceGenerator). The repo has 5 weight styles (Light through Bold). No config.yaml exists; the build system predates gftools-builder and uses a specialized Devanagari pipeline. An override config.yaml could potentially be created but would need careful testing given the complex build process.

## Key Findings

| Field             | Value                                                                 |
|-------------------|-----------------------------------------------------------------------|
| Family Name       | Hind                                                                  |
| Designer          | Indian Type Foundry                                                   |
| Repository URL    | https://github.com/itfoundry/hind                                    |
| Commit Hash       | 6caef5262dc5bee3e033207082a073a6a1d172d6                              |
| Config YAML       | Needs override config.yaml (upstream has custom AFDKO build system)   |
| Status            | missing_config                                                        |
| Confidence        | MEDIUM                                                                |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb in google/fonts has a minimal source block:
- `repository_url: "https://github.com/itfoundry/hind"`
- **Missing**: `commit` field, `config_yaml` field

The source block was added by Simon Cozens in commit `474a446c0` (2024-01-14, "More upstreams (g,h)") with only the repository URL.

Key METADATA.pb fields:
- Designer: Indian Type Foundry
- License: OFL
- Category: SANS_SERIF
- Date added: 2014-06-25
- Fonts: 5 weights (Light 300, Regular 400, Medium 500, SemiBold 600, Bold 700)
- Subsets: devanagari, latin, latin-ext
- Primary script: Deva

### Git History in google/fonts

1. **Initial onboarding** (`90abd17b4`, 2015-03-07): "Initial commit" - the original addition of Hind fonts.

2. **Update to v2.001** (PR #890, `8ea6ba161`, 2017-05-16): "hotfix-hind: v2.001 added" by Marc Foley. Updated all 5 TTF files and the DESCRIPTION. Also corrected filename casing from `Hind-Semibold.ttf` to `Hind-SemiBold.ttf`. The PR body is empty, providing no reference to an upstream commit.

3. **Filename rename** (`d774fc079`, 2017-05-15): "Rename various Semibold -> SemiBold" - precedes the v2.001 update.

The font binaries were last modified in commit `8ea6ba161` (v2.001, 2017-05-16). This is the current version in Google Fonts.

### Upstream Repository Analysis

The cached repo at `fontc_crater_cache/itfoundry/hind` is clean and up to date with origin.

**Repository structure**:
- `masters/Hind_0.ufo`, `masters/Hind_1.ufo` - Two master UFO files
- `masters/Hind_0.vfb`, `masters/Hind_1.vfb` - FontLab VFB master files
- `styles/{Light,Regular,Medium,SemiBold,Bold}/font.ufo` - Per-style instance UFOs
- `build.py` - Custom build script
- `config.py` - Build configuration
- `build/Hind-{Bold,Light,Medium,Regular,SemiBold}.otf` - Compiled OTF outputs
- Feature files: `family.fea`, `family_classes.fea`, `family_extension.fea`, `family_tables.fea`
- Other: `itf.py`, `reference.py`, `FontMenuNameDB`, `GlyphOrderAndAliasDB`

**No config.yaml** for gftools-builder exists.

**Latest commit**: `6caef52` (2014-11-21, "Compile 2.000") - This is the most recent commit in the repository. The repo has not been updated since November 2014.

### Build System

The upstream `build.py` is an AFDKO-based build system that:
1. Generates OpenType classes from masters
2. Resets style/instance directories
3. Generates instances using `UFOInstanceGenerator.py` (Adobe tool)
4. Matches mI (Devanagari i-matra) variants to base glyphs
5. Compiles OTFs using `makeotf`

Dependencies (from README.md):
- AFDKO version 2.5 build 63209 or newer
- `UFOInstanceGenerator.py` from Adobe
- Python modules from Adobe

This build system predates gftools-builder and is **not directly compatible**. The UFO sources could potentially be processed by gftools-builder with an override config.yaml, but the complex Devanagari-specific processing (mI matching, custom feature code) may not produce identical results.

### Commit Hash Determination

The repository's latest commit is `6caef5262dc5bee3e033207082a073a6a1d172d6` (2014-11-21, "Compile 2.000"). However, the google/fonts v2.001 update happened in May 2017 (PR #890), and the repo shows version 2.000 as the latest. This creates a discrepancy:

- The repo has `Compile 2.000` as the last commit (2014-11-21)
- google/fonts has v2.001 (added 2017-05-16)
- The v2.001 font files in google/fonts may have been compiled outside this repo or from a different branch/fork

Since the repo has only one branch and the latest commit is from 2014, the v2.001 binaries in google/fonts were likely compiled separately (perhaps by Marc Foley as a hotfix) using the sources from this repo but with additional modifications. The latest commit `6caef52` is the best reference for the upstream source state, even though the actual v2.001 compilation may have involved additional steps not captured in the repo.

**Confidence: MEDIUM** - The commit hash is the latest in the repo and represents the most complete source state, but there is a version mismatch between the repo (v2.000) and google/fonts (v2.001).

### No Override config.yaml in google/fonts

There is no `config.yaml` override file in `ofl/hind/` in google/fonts.

## Conclusion

**Status: missing_config**

The source block in METADATA.pb has the correct repository URL but is missing the `commit` field. The commit hash `6caef5262dc5bee3e033207082a073a6a1d172d6` (the latest and only meaningful reference point) should be added, with a note about the version discrepancy. An override config.yaml for gftools-builder could be created using the UFO master files, but the complex Devanagari-specific build pipeline (mI matching, custom feature generation, AFDKO instance generation) means the output may differ from the current v2.001 binaries. The build system uses `masters/Hind_0.ufo` and `masters/Hind_1.ufo` as source masters. Note that the repo has not been updated since 2014, while the fonts in google/fonts are v2.001 from 2017.
