# Investigation Report: Bungee Inline

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bungee Inline |
| Designer | David Jonathan Ross |
| Repository URL | https://github.com/djrrb/Bungee |
| Commit Hash | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Branch | master |
| Config YAML | N/A (override in google/fonts) |
| Date Added | 2016-06-20 |
| License | OFL |
| Status | complete |

## How URL Found

The repository URL `https://github.com/djrrb/Bungee` is recorded in METADATA.pb and was added as part of the upstream metadata by Viviana Monsalve on 2024-05-30 during the v2.000 update. The URL is clearly correct as the Bungee project by David Jonathan Ross (djrrb) is well-known and the repo contains all Bungee variant sources.

## How Commit Determined

The commit `eb03cf69adab5094f6b84e95357789cdf3bfeb99` was recorded in the google/fonts commit message for the v2.000 update:

```
dccf62125 Bungee Inline: Version 2.000 added
Taken from the upstream repo https://github.com/djrrb/Bungee at commit
https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99.
```

This commit was made by Viviana Monsalve on 2024-05-30.

**Cross-verification**: The commit `eb03cf69` in the upstream repo corresponds exactly to the `v2.000` release tag. The commit itself is "Bump fontbakery" by Just van Rossum, dated 2024-05-30. The METADATA.pb also references `archive_url: "https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip"` which aligns with this being the v2.000 release. The binary fonts were taken from this release archive (pre-built), not compiled from source via gftools-builder.

### History

- **v1.001** (2017-05-23): Originally added by Marc Foley (`af0dce45e`)
- **v2.000** (2024-05-30): Updated by Viviana Monsalve (`dccf62125`) from upstream commit `eb03cf69` / v2.000 release

## Config YAML Status

**No config.yaml in upstream repo** at any commit. The Bungee project uses a custom build pipeline:
1. Assembly scripts (`assembleSources.py`, `assembleRotatedSources.py`, `assembleColorSources.py`) process raw UFO sources from `sources/1-drawing/` into buildable UFOs in `sources/2-build/`
2. `fontmake` compiles the assembled UFOs
3. The `build.sh` script orchestrates the entire process

This is not compatible with standard gftools-builder.

**Override config.yaml** exists in google/fonts at `ofl/bungeeinline/config.yaml`:
```yaml
sources:
  - sources/2-build/Bungee_Basic/Bungee-Inline.ufo
familyName: Bungee Inline
buildStatic: true
buildOTF: false
```

This override points to `sources/2-build/Bungee_Basic/Bungee-Inline.ufo` which exists at the recorded commit `eb03cf69`. The `sources/2-build/` directory was removed from the upstream repo 3 commits later (in `7ffc5a64`), so the override config only works with the recorded commit hash.

## Verification

- **Repository URL**: Valid, accessible GitHub repository
- **Commit hash exists**: Confirmed `eb03cf69` exists in the upstream repo
- **Tag alignment**: Commit `eb03cf69` is exactly the `v2.000` release tag
- **Source files at commit**: `sources/2-build/Bungee_Basic/Bungee-Inline.ufo` exists at this commit
- **Override config**: Correctly references existing source path at the recorded commit
- **Binary source**: METADATA.pb uses `archive_url` pointing to v2.000 release zip; the binary `BungeeInline-Regular.ttf` was taken from `Bungee_Basic/BungeeInline-Regular.ttf` within the archive

## Confidence Level

**HIGH** - The commit hash is explicitly stated in the google/fonts commit message and aligns exactly with the upstream v2.000 release tag. The override config.yaml correctly references source files that exist at this commit.

## Open Questions

None. The data is fully consistent and verified.
