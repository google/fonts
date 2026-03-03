# Investigation Report: Lisu Bosa

**Model**: Claude Opus 4.6

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lisu Bosa |
| Designer | SIL International |
| License | OFL |
| Repository URL | https://github.com/silnrsi/font-lisu-bosa |
| Commit Hash | `95b4da9504f8ba528e001dbfb23adafa314388e3` |
| Branch | master |
| Config | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## METADATA.pb Source Block (current in main)

The METADATA.pb in the main branch of google/fonts contained a source block with `repository_url` and `archive_url` pointing to the v2.000 release, but no `commit` hash and no `config_yaml`. The source block was originally generated from an `upstream.yaml` file that was merged into METADATA.pb by Simon Cozens in commit `66f91f10` (2024-04-03).

A commit hash (`95b4da9504f8ba528e001dbfb23adafa314388e3`) was added in the `sources_info_2026-02-25` branch (commit `9a14639f3`) but had not yet been merged into google/fonts main at the time of this investigation.

## Onboarding History

### Initial Addition (PR #6510)

Lisu Bosa was added to Google Fonts via PR #6510, authored by Emma Marichal and merged by Rosalie Wagner on 2023-07-06. The commit message read:

> [gftools-packager] Lisu Bosa: Version 2.000 added
> Lisu Bosa Version 2.000 taken from the upstream repo https://github.com/silnrsi/font-lisu-bosa at commit https://github.com/silnrsi/font-lisu-bosa/commit/.

Notably, the commit hash was empty in the URL (the message ended with "/commit/."), indicating gftools-packager failed to capture the commit hash, likely because the fonts were sourced from the release archive rather than a specific git commit.

The onboarding commit (`c2e8f431`) included 18 TTF files (16 weight/style variants), METADATA.pb, DESCRIPTION.en_us.html, OFL.txt, and an upstream.yaml file.

### Related Issue

PR #6510 referenced GitHub issue #4354 ("SIL fonts onboarding (Summary)"), which tracked the onboarding of multiple SIL International fonts into Google Fonts.

## Upstream Repository Analysis

### Repository Structure

The upstream repository at `https://github.com/silnrsi/font-lisu-bosa` used SIL's `smith` build system (wscript-based), not gftools-builder. The repository structure included:

- `source/LisuBosaUpright.designspace` -- upright family (ExtraLight to Black)
- `source/LisuBosaItalic.designspace` -- italic family (ExtraLight Italic to Black Italic)
- `source/LisuBosaLoloUpright.designspace` -- auxiliary "Lolo" RIBBI subset (upright)
- `source/LisuBosaLoloItalic.designspace` -- auxiliary "Lolo" RIBBI subset (italic)
- `source/masters/` -- 6 UFO masters (Regular, ExtraLight, Black, Italic, ExtraLightItalic, BlackItalic)
- `source/master.feax` -- SIL extended feature file (simple kern lookup only)
- `wscript` -- smith build configuration

### Build System

The project used SIL's smith toolchain with `wscript`. The wscript compiled fonts from two designspace files (Upright and Italic) using the smith `designspace()` command, generating OpenType features from `.feax` files. The `.feax` format was SIL's extended feature syntax processed by `pysilfont`.

However, the `.feax` file was minimal (just a kern feature lookup), and the designspace/UFO sources were standard format. This made the project compatible with gftools-builder via an override config.yaml.

### Tags and Releases

The v2.000 tag (also tagged `c2.000`) pointed to commit `95b4da9` (2023-02-22, "Update release date"). The release archive `LisuBosa-2.000.zip` contained pre-built TTF binaries that were directly copied into google/fonts via gftools-packager.

### Font Files from Release Archive

The upstream.yaml confirmed the fonts came from the release archive:
- `archive: https://github.com/silnrsi/font-lisu-bosa/releases/download/v2.000/LisuBosa-2.000.zip`
- Files were mapped from `LisuBosa-2.000/*.ttf` to the google/fonts family directory

## Commit Hash Verification

The commit hash `95b4da9504f8ba528e001dbfb23adafa314388e3` was verified as the correct reference:

1. **Tag alignment**: The v2.000 tag pointed to this commit, and the release archive referenced in upstream.yaml was from the v2.000 release.
2. **Timeline consistency**: The tag was created on 2023-02-22, well before the PR #6510 merge date of 2023-07-06.
3. **No font changes after tag**: Between commit `95b4da9` (v2.000) and the merge date, only documentation/nobuild commits were made: `5c56c72` (FAQ links), `efe4592` (docs), `fc9454c` (URLs update) -- all marked `[nobuild]`.
4. **Binary file sizes matched**: The TTF file sizes in google/fonts matched those from the release archive (confirmed by the onboarding commit stat output).

**Confidence: HIGH** -- The fonts were taken from a tagged release archive, and no source changes occurred between the tag and the onboarding.

## Config.yaml Status

The upstream repository had no `config.yaml` file. It used the smith build system (`wscript`). No override `config.yaml` existed in the google/fonts family directory either.

However, the sources were gftools-builder compatible:
- Two designspace files (`LisuBosaUpright.designspace` and `LisuBosaItalic.designspace`)
- Standard UFO masters in `source/masters/`
- Simple kern-only `.feax` file (kernpairs are embedded in the UFOs)

An override `config.yaml` could be created for gftools-builder to build from the designspace sources. The config would need to reference both `source/LisuBosaUpright.designspace` and `source/LisuBosaItalic.designspace`.

Note: The "Lolo" designspace variants (`LisuBosaLoloUpright.designspace` and `LisuBosaLoloItalic.designspace`) were for a separate auxiliary "Lisu Bosa Lolo" family and should NOT be included in the config for the main "Lisu Bosa" family.

## Files in google/fonts

The family directory at `ofl/lisubosa/` contained:
- 16 TTF files (8 weights x 2 styles: upright + italic, from ExtraLight to Black)
- METADATA.pb
- DESCRIPTION.en_us.html
- OFL.txt

No `upstream_info.md` or `config.yaml` existed in the directory.

## Recommended Actions

1. **Add commit hash**: Add `commit: "95b4da9504f8ba528e001dbfb23adafa314388e3"` to the source block (already in the pending `sources_info_2026-02-25` branch).
2. **Create override config.yaml**: Create a gftools-builder config.yaml in `ofl/lisubosa/` referencing `source/LisuBosaUpright.designspace` and `source/LisuBosaItalic.designspace`.
3. **Add upstream_info.md**: Include this investigation report in the family directory.
