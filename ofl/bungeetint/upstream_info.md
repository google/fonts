# Investigation Report: Bungee Tint

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bungee Tint |
| Designer | David Jonathan Ross |
| Repository URL | https://github.com/djrrb/Bungee |
| Commit Hash | `0ab742e49fc7725cd86089834d6460c489b9b2a6` |
| Branch | master |
| Config YAML | None (missing) |
| Date Added | 2024-07-18 |
| License | OFL |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/djrrb/Bungee` is recorded in METADATA.pb. All Bungee variants share this single upstream repository. The URL was set when Bungee Tint was first added to Google Fonts on 2024-07-18.

## How Commit Determined

The commit `0ab742e49fc7725cd86089834d6460c489b9b2a6` is explicitly stated in the google/fonts commit message:

```
fff14184d Bungee Tint: Version 2.001 added
Taken from the upstream repo https://github.com/djrrb/Bungee at commit
https://github.com/djrrb/Bungee/commit/0ab742e49fc7725cd86089834d6460c489b9b2a6.
```

This commit was authored by Viviana Monsalve on 2024-07-18.

**Cross-verification**: The commit `0ab742e4` is the HEAD of the master branch and corresponds to "Merge pull request #121 from vv-monsalve/QA-Bungee". It is NOT exactly the `v2.001` tag -- it is 17 commits after `v2.001` (`dbf8a1c4`). The commits between v2.001 and `0ab742e4` are all article/documentation changes (images, article templates, contributor list updates) -- no font source changes. The METADATA.pb references `archive_url: "https://github.com/djrrb/Bungee/releases/download/v2.001/Bungee-fonts.zip"`, confirming the actual fonts came from the v2.001 release archive.

### History and Context

Bungee Tint was formerly called "Bungee Color" and was renamed in PR #115 ("rename-color-to-tint"). The rename occurred between v2.000 and v2.001:

- **v2.000** (`eb03cf69`, 2024-05-30): Bungee Spice and other variants updated; "Bungee Color" name still used
- **v2.001** (`dbf8a1c4`): Version bump with rename to "Bungee Tint"
- **0ab742e4** (2024-07-18): HEAD at time of onboarding, article/QA changes after v2.001

Timeline of google/fonts commits:
- `fff14184d` (2024-07-18): "Bungee Tint: Version 2.001 added" by Viviana Monsalve
- `3c96c1458` (2024-07-18): "OFL license added"
- `2a8293b0d` (2024-07-18): "Bungee Tint article added"
- `35963e3ae` (2025-02-06): "Bungee Tint update" (article update by Emma Marichal)

## Config YAML Status

**No config.yaml in upstream repo** at any commit. The Bungee project uses a custom multi-step build pipeline:

1. `scripts/assembleSources.py` - Assembles basic font UFOs from drawing sources
2. `scripts/assembleColorSources.py` - Generates color font UFOs (both Bungee Tint and Bungee Spice)
3. `fontmake` - Compiles the assembled UFOs into TTFs
4. Post-processing with `gftools fix-nonhinting`

For Bungee Tint specifically, the `assembleColorSources.py` script generates `BungeeTint-Regular.ufo` from the base `Bungee-Regular.ufo` source with COLRv1 color layers applied. Unlike Bungee Spice, Bungee Tint does not need `maximum_color` post-processing.

**Critical issue**: At the recorded commit `0ab742e4`, the `sources/2-build/` directory does NOT exist -- it was removed in commit `7ffc5a64` ("remove /fonts folders and /2-build folder"), which is between `eb03cf69` (v2.000) and `0ab742e4` (HEAD). This means there are no pre-assembled UFO sources to point a config.yaml at. The buildable UFO only exists after running the assembly scripts.

**No override config.yaml** exists in google/fonts at `ofl/bungeetint/`.

### Comparison with Other Bungee Variants

The other Bungee variants (Inline, Outline, Shade, Spice) all use commit `eb03cf69` (v2.000) where `sources/2-build/` still existed, allowing override config.yaml files to point to pre-assembled UFOs. Bungee Tint uses a later commit where this directory is gone, making it impossible to create a simple config.yaml override.

### Possible Solutions

1. **Change the commit hash** to `eb03cf69` (v2.000) -- but Bungee Tint did not exist at that commit (it was still called "Bungee Color" and the rename happened after v2.000)
2. **Create an override config.yaml** pointing to `sources/1-drawing/Bungee-Regular.ufo` -- but this is the raw drawing source, not the assembled color font; gftools-builder cannot reproduce the color assembly pipeline
3. **Accept that this font cannot be built with gftools-builder** -- the custom build pipeline is not expressible as a config.yaml

## Verification

- **Repository URL**: Valid, accessible GitHub repository
- **Commit hash exists**: Confirmed `0ab742e4` exists in the upstream repo (it is HEAD of master)
- **Tag alignment**: Commit `0ab742e4` is 17 commits after `v2.001` tag, but the font binary came from the v2.001 release archive
- **Source files at commit**: Only `sources/1-drawing/` exists (raw drawing sources); `sources/2-build/` was removed
- **Binary source**: METADATA.pb uses `archive_url` pointing to v2.001 release zip; the binary was taken from `Bungee_Color/BungeeTint-Regular.ttf` within the archive

## Confidence Level

**HIGH** for repository URL and commit hash (explicitly stated in google/fonts commit message, commit verified in upstream).

**Note**: The commit hash `0ab742e4` is slightly imprecise as an onboarding reference -- the actual fonts came from the v2.001 release (`dbf8a1c4`), not from this later commit. However, since no font sources changed between these commits, this is a cosmetic discrepancy only.

## Open Questions

1. **Config.yaml feasibility**: The Bungee build pipeline uses custom assembly scripts that generate color font UFOs programmatically. This cannot be expressed as a standard gftools-builder config.yaml. Should this family be marked as "not buildable with gftools-builder" rather than "missing_config"?
2. **Commit hash precision**: Should the commit hash be updated to `dbf8a1c4` (the actual v2.001 tag) to more precisely identify the release used? The current hash `0ab742e4` is HEAD, which includes post-release documentation changes.
