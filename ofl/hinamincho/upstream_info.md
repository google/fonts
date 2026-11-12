# Investigation Report: Hina Mincho

## Summary

Hina Mincho is a Japanese serif/display font designed by Satsuyako, first added to Google Fonts in 2021-04-14 (PR #3312) and updated to Version 1.100 on 2021-06-09 (PR #3486). The upstream repository at `https://github.com/satsuyako/Hina-Mincho` has buildable source files (.glyphs format at the onboarding commit, later migrated to .glyphspackage). The onboarding commit `7642eb4` is explicitly referenced in the PR body and verified. The repo has no config.yaml; it uses a custom `build.py` that requires the Glyphs application. An override config.yaml is needed for gftools-builder compatibility.

## Key Findings

| Field             | Value                                                                 |
|-------------------|-----------------------------------------------------------------------|
| Family Name       | Hina Mincho                                                           |
| Designer          | Satsuyako                                                             |
| Repository URL    | https://github.com/satsuyako/Hina-Mincho                             |
| Commit Hash       | 7642eb499ceef47074cb344a4800a537bce19c60                              |
| Config YAML       | Needs override config.yaml (upstream has custom build.py, not gftools)|
| Status            | missing_config                                                        |
| Confidence        | HIGH                                                                  |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb in google/fonts already has a source block with:
- `repository_url: "https://github.com/satsuyako/Hina-Mincho"`
- File mappings: `fonts/ttf/HinaMincho-Regular.ttf` -> `HinaMincho-Regular.ttf`, `OFL.txt`, `DESCRIPTION.en_us.html`
- `branch: "master"`
- **Missing**: `commit` field and `config_yaml` field

The source block was initially added by Simon Cozens in commit `2423d2aef` (2023-12-14, "Update upstreams") with just the repository_url, then expanded in commit `66f91f10f` (2024-04-03, "Merge upstream.yaml into METADATA.pb") with file mappings and branch.

### Git History in google/fonts

1. **Initial onboarding** (PR #3312, `bf63dbc0b`, 2021-04-21): "Hina Mincho: Version 1.000; ttfautohint (v1.8.3) added" by Aaron Bell. The commit body references upstream commit `f159a133f9aa8bdbc2f610bef25f0408f3b6ec76`. Added the font file (14.7 MB), METADATA.pb, OFL.txt, DESCRIPTION.en_us.html, and upstream.yaml.

2. **Update to v1.100** (PR #3486, `0bac7827e`, 2021-06-09): "Hina Mincho: Version 1.100 added" by Aaron Bell. The commit body references upstream commit `7642eb499ceef47074cb344a4800a537bce19c60`. The font file was reduced from 14.7 MB to 6.4 MB (dehinted).

The font binary was last modified in commit `0bac7827e`. This is the current version in Google Fonts.

### Upstream Repository Analysis

The cached repo at `fontc_crater_cache/satsuyako/Hina-Mincho` is clean and up to date with origin.

**At the onboarding commit (7642eb4, 2021-06-09)**:
- Source file: `sources/Hina-Mincho.glyphs` (Glyphs 2 format)
- Build script: `build.py` (custom, requires Glyphs application via JSTalk/NSConnection)
- Output: `fonts/ttf/HinaMincho-Regular.ttf`
- No config.yaml for gftools-builder

**Current state (HEAD)**:
The repository has continued development after the onboarding:
- `e58a3ee` / `846bfe6` (2022-06-05): Character corrections
- `6fdbb79` (2024-02-23): Glyph fix
- `a770f32` (2025-06-03): Kanji character fix
- `edab42b` (2025-07-24): Migrated source to `.glyphspackage` format
- `d231dd4` (2025-07-24): Cleanup
- `8b0fed8` (2025-10-15): README update
- `4811379` (2026-01-15): Glyph mapping fix

The source has been significantly updated since the onboarding commit, including a format migration from `.glyphs` to `.glyphspackage`.

### Build System

The upstream `build.py` is a custom script that:
1. Uses the Glyphs application (via JSTalk/NSConnection on macOS) to export TTF
2. Post-processes fonts with fontTools (GASP table, DSIG stub, head flags)

This is **not compatible** with gftools-builder. An override config.yaml would be needed. At the onboarding commit (7642eb4), the source file is `sources/Hina-Mincho.glyphs`, which is a standard Glyphs format file that gftools-builder can process.

### Commit Verification

The commit `7642eb499ceef47074cb344a4800a537bce19c60` is:
- A merge commit: "Merge pull request #4 from aaronbell/master" (2021-06-09)
- Content: Dehinted the font, updated build.py, updated source
- Explicitly referenced in PR #3486 body: "taken from the upstream repo ... at commit ..."
- The commit date (2021-06-09) matches the PR merge date in google/fonts (2021-06-09)

This is verified as the correct onboarding commit for the current version.

### No Override config.yaml in google/fonts

There is no `config.yaml` override file in `ofl/hinamincho/` in google/fonts.

## Conclusion

**Status: missing_config**

The source block in METADATA.pb has the correct repository URL but is missing the `commit` field. The commit hash `7642eb499ceef47074cb344a4800a537bce19c60` should be added. An override config.yaml for gftools-builder is needed since the upstream uses a custom Glyphs-application-based build script. The config would reference `sources/Hina-Mincho.glyphs` at the onboarding commit. Note that the upstream repo has continued active development with character fixes and a source format migration to .glyphspackage; any update from upstream would need separate review.
