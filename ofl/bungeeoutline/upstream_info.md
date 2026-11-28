# Investigation Report: Bungee Outline

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bungee Outline |
| Designer | David Jonathan Ross |
| Repository URL | https://github.com/djrrb/Bungee |
| Commit Hash | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Branch | master |
| Config YAML | N/A (override in google/fonts) |
| Date Added | 2016-06-20 |
| License | OFL |
| Status | complete |

## How URL Found

The repository URL `https://github.com/djrrb/Bungee` is recorded in METADATA.pb. All Bungee variants (Bungee, Bungee Hairline, Bungee Inline, Bungee Outline, Bungee Shade, Bungee Spice, Bungee Tint) share this single upstream repository. The URL was added by Viviana Monsalve during the v2.000 update on 2024-05-30.

## How Commit Determined

The commit `eb03cf69adab5094f6b84e95357789cdf3bfeb99` is explicitly stated in the google/fonts commit message:

```
d3d22093c Bungee Outline: Version 2.000 added
Taken from the upstream repo https://github.com/djrrb/Bungee at commit
https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99.
```

This commit was authored by Viviana Monsalve on 2024-05-30.

**Cross-verification**: The commit `eb03cf69` corresponds exactly to the upstream `v2.000` release tag. The METADATA.pb also references `archive_url: "https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip"`, confirming the fonts were taken from the v2.000 release archive. The same commit hash is used for Bungee Inline, Bungee Shade, and Bungee Spice, all of which were updated to v2.000 on the same date.

### History

- **v1.001** (2017-05-23): Originally added by Marc Foley (`ca9abdfc4`, PR #1002)
- **v2.000** (2024-05-30): Updated by Viviana Monsalve (`d3d22093c`) from upstream commit `eb03cf69` / v2.000 release

## Config YAML Status

**No config.yaml in upstream repo** at any commit. The Bungee project uses a custom build pipeline with assembly scripts (`assembleSources.py`, etc.) that transform raw UFO sources in `sources/1-drawing/` into buildable UFOs in `sources/2-build/`, followed by `fontmake` compilation. This is not compatible with standard gftools-builder.

**Override config.yaml** exists in google/fonts at `ofl/bungeeoutline/config.yaml`:
```yaml
sources:
  - sources/2-build/Bungee_Basic/Bungee-Outline.ufo
familyName: Bungee Outline
buildStatic: true
buildOTF: false
```

This override points to `sources/2-build/Bungee_Basic/Bungee-Outline.ufo` which exists at the recorded commit `eb03cf69`. Note that the `sources/2-build/` directory was removed from the upstream repo 3 commits later (in `7ffc5a64` "remove /fonts folders and /2-build folder"), so this override config only works with the recorded commit hash.

## Verification

- **Repository URL**: Valid, accessible GitHub repository
- **Commit hash exists**: Confirmed `eb03cf69` exists in the upstream repo
- **Tag alignment**: Commit `eb03cf69` is exactly the `v2.000` release tag
- **Source files at commit**: `sources/2-build/Bungee_Basic/Bungee-Outline.ufo` exists at this commit
- **Override config**: Correctly references existing source path at the recorded commit
- **Binary source**: METADATA.pb uses `archive_url` pointing to v2.000 release zip; the binary was taken from `Bungee_Basic/BungeeOutline-Regular.ttf` within the archive

## Confidence Level

**HIGH** - The commit hash is explicitly stated in the google/fonts commit message and aligns exactly with the upstream v2.000 release tag. All data is consistent.

## Open Questions

None. The data is fully consistent and verified.
