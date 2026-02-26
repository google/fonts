# Beth Ellen - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Beth Ellen |
| Repository URL | https://github.com/googlefonts/BethEllen |
| Commit Hash | d6c8d9b3871c432c6abfd71660885f16ddbce3e2 |
| Config YAML | (none) |
| Status | missing_config |
| Category | HANDWRITING |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/BethEllen` was already present in the METADATA.pb `source{}` block. It was first added by commit `f7455d788` ("Populate source.repository_url") and confirmed by the copyright string in the font metadata: "Copyright 2019 The Beth Ellen Project Authors (https://github.com/googlefonts/BethEllen)". An earlier commit `2bf30f384` also updated the font project URL to point to `googlefonts/BethEllen`.

## How the Commit Hash Was Determined

The commit hash `d6c8d9b3871c432c6abfd71660885f16ddbce3e2` was found in the original google/fonts commit `0aa5f370a` (2019-05-10) by Felipe Sanches, which added Beth Ellen to the catalog. The commit message reads: "Add Beth Ellen (Version 2.000)" and includes the URL `(https://github.com/googlefonts/BethEllen/commit/d6c8d9b3871c432c6abfd71660885f16ddbce3e2)`.

The commit hash was later added to the METADATA.pb source block in the batch commit `9a14639f3` (2026-02-25): "Add source blocks to 602 more METADATA.pb files".

The upstream commit `d6c8d9b` is: "manual fixes using gftools and ttx" - this is the commit from which the font binary was taken when onboarding Beth Ellen.

## Config YAML Status

**No config.yaml exists** in the upstream repository, either at the recorded commit or at HEAD.

At the recorded commit `d6c8d9b`, the repository structure is:
- `BethEllen-Regular.sfd` (FontForge source)
- `BethEllen-Regular.ttf` (pre-built binary)
- `BethEllen-Story.pdf`
- `OFL.txt`
- `README.md`
- `old/` and `prebuilt/` directories

The font source is in SFD (FontForge) format, which is not compatible with gftools-builder. At HEAD, a `.glyphs` file has been added (`BethEllen-Regular.glyphs`), but still no config.yaml.

No override config.yaml exists in the google/fonts family directory either.

## Verification

- **Repository exists**: Yes, confirmed locally in cache at `upstream_repos/fontc_crater_cache/googlefonts/BethEllen`
- **Commit hash exists**: Yes, verified: `d6c8d9b manual fixes using gftools and ttx`
- **Config.yaml exists**: No, neither in upstream repo nor as override
- **Source format**: SFD (FontForge) - not gftools-builder compatible

## Confidence Level

**High** - The commit hash is explicitly documented in the original google/fonts commit message by the person who performed the onboarding (Felipe Sanches). The upstream commit exists and is verified. The lack of config.yaml is expected given the SFD-only source format.

## Open Questions

- The upstream repo now has a `.glyphs` file at HEAD (not present at the recorded commit). A config.yaml could potentially be created for future builds using this newer source, but that would require a separate review process.
- The status remains `missing_config` because no gftools-builder configuration exists.
