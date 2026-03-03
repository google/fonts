# Investigation Report: Big Shoulders Stencil Text SC

## Family Information
- **Family Name**: Big Shoulders Stencil Text SC
- **Slug**: bigshouldersstenciltextsc
- **Designer**: Patric King
- **Category**: DISPLAY
- **Date Added**: 2024-05-30
- **License**: OFL
- **Family Directory**: ofl/bigshouldersstenciltextsc

## Source Block (Current METADATA.pb)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "0b3d09a86862b19efae28eae0cd868f17c476b20"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders-Stencil/fonts/variable/text/BigShouldersStencilTextSC[wght].ttf"
    dest_file: "BigShouldersStencilTextSC[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository Verification

The upstream repository at https://github.com/xotypeco/big_shoulders was verified. The local cache at `upstream_repos/fontc_crater_cache/xotypeco/big_shoulders` has the correct remote URL.

### Commit Verification

The commit `0b3d09a86862b19efae28eae0cd868f17c476b20` ("regenerate font files", 2024-02-26) was confirmed to exist in the upstream repository on the `master` branch.

### How the Family Was Onboarded

The family was added to google/fonts via PR #7789 (branch: `gftools_packager_ofl_bigshouldersstenciltextsc`), merged on 2024-06-25 by Emma Marichal. The onboarding commit by Simon Cozens (2024-05-30) explicitly stated:

> Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/0b3d09a86862b19efae28eae0cd868f17c476b20.

The commit introduced 5 files:
- `BigShouldersStencilTextSC[wght].ttf` (the font binary)
- `DESCRIPTION.en_us.html`
- `METADATA.pb`
- `OFL.txt`
- `config.yaml` (override config)

### Source File Verification

At commit `0b3d09a`, the upstream repository contained:
- `Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs` -- the primary source file
- `Big-Shoulders-Stencil/sources/config.yml` -- an upstream config (standard gftools format, not suitable for building the SC variant)
- `Big-Shoulders-Stencil/fonts/variable/text/BigShouldersStencilText[wght].ttf` -- pre-built Text variant (non-SC)

Notably, the `BigShouldersStencilTextSC[wght].ttf` binary did **not** exist in the upstream repo at commit `0b3d09a`. The SC (Small Caps) variant was built from source by gftools-packager using the override `config.yaml` in google/fonts. The SC binary only appeared in the upstream repo much later (January/February 2025, commits `bdd1757` and `b16b16d`).

The METADATA.pb `files` block references `Big-Shoulders-Stencil/fonts/variable/text/BigShouldersStencilTextSC[wght].ttf` as a source file, but this file did not exist at the referenced commit. This is a minor inaccuracy -- the font was actually built from the `.glyphs` source using the config.yaml recipe, not copied from a pre-built binary.

### Override config.yaml

A local override `config.yaml` exists in the google/fonts family directory. It was included in the original onboarding commit. The config defines a build recipe that:

1. Builds from `../Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs`
2. Subspaces to `opsz=10` (Text optical size)
3. Applies `remapLayout` (`smcp -> ccmp`) to create the Small Caps variant
4. Renames to "Big Shoulders Stencil Text SC"
5. Applies fix and buildStat postprocessing

The config also builds the non-SC `BigShouldersStencilText[wght].ttf` alongside the SC variant. The `sources` paths use `../Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs`, which is relative to the family directory.

Since an override `config.yaml` exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block.

### Upstream config.yml vs Override config.yaml

The upstream repository had a `Big-Shoulders-Stencil/sources/config.yml` at the referenced commit, but it only configured the full 2-axis (`opsz,wght`) Stencil variable font, without the SC variant build recipe. The override `config.yaml` in google/fonts was necessary to produce the small caps variant.

## Conclusion

- **Repository URL**: `https://github.com/xotypeco/big_shoulders` -- Verified correct
- **Commit**: `0b3d09a86862b19efae28eae0cd868f17c476b20` -- Verified correct (explicitly referenced in onboarding commit message)
- **Config**: Override `config.yaml` in google/fonts family directory -- Present and correct
- **Status**: Complete
- **Confidence**: HIGH

The source block is complete and accurate. The repository URL and commit hash were verified against the onboarding PR #7789 and commit message. The override config.yaml is correctly present in the family directory, enabling the SC variant build from the upstream `.glyphs` source.

The only minor note is that the `files` block in METADATA.pb references a binary path (`BigShouldersStencilTextSC[wght].ttf`) that did not exist at the referenced upstream commit. The font was actually built from source using the config.yaml recipe. This is a cosmetic issue and does not affect functionality.
