# Investigation: Birthstone Bounce

**Family name:** Birthstone Bounce
**Slug:** birthstonebounce
**Family directory:** ofl/birthstonebounce
**Designer:** Robert Leuschke
**Date added:** 2021-09-02
**Model:** Claude Opus 4.6

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/birthstone-bounce"
  commit: "db48de44b60017495c71a024aa2c079d70869225"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BirthstoneBounce-Regular.ttf"
    dest_file: "BirthstoneBounce-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/BirthstoneBounce-Medium.ttf"
    dest_file: "BirthstoneBounce-Medium.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository

- **URL:** https://github.com/googlefonts/birthstone-bounce
- **Cached at:** upstream_repos/fontc_crater_cache/googlefonts/birthstone-bounce
- **Status:** Valid, accessible, cached

## Commit Verification

The METADATA.pb references commit `db48de44b60017495c71a024aa2c079d70869225` ("outline fixes in acute and ring", authored by Viviana Monsalve on 2021-09-17).

### Onboarding History

The family was onboarded via PR [#3793](https://github.com/google/fonts/pull/3793) ("Birthstone Bounce: Version 1.010; ttfautohint (v1.8.3) added"), authored by vv-monsalve and merged on 2021-09-08. The gftools-packager message in the PR body referenced commit `f45812daabb656a9d1d8c19c211fc19c26c95c07`.

### Discrepancy Analysis

The upstream repository currently contains only a single commit (`db48de4`), dated 2021-09-17 -- nine days *after* the google/fonts PR was merged on 2021-09-08. The originally referenced commit `f45812da` no longer exists. This indicates the upstream repository was force-pushed or squashed after the onboarding, collapsing the history into a single commit.

Despite this, the binary font files at commit `db48de4` are **byte-identical** to those in google/fonts:
- `BirthstoneBounce-Regular.ttf`: 326,712 bytes (match)
- `BirthstoneBounce-Medium.ttf`: 322,404 bytes (match)

Since `db48de4` is the only commit in the repository and the binaries match exactly, the METADATA.pb commit hash is the best available reference. The source block data was added in the batch commit `19cdcec59` ([Batch 1/4] port info from fontc_crater targets list, 2025-03-31), porting data from the fontc_crater targets list.

**Conclusion:** The commit hash `db48de4` is accepted as the correct reference. The original commit `f45812da` was lost to a force-push, but the sole remaining commit produces identical binaries.

## Source Files and Config

### Source Files at Referenced Commit

The upstream repo contained gftools-builder compatible sources:
- `sources/BirthstoneBounce.glyphs` -- Glyphs source file
- `sources/config.yaml` -- gftools-builder configuration

### config.yaml (upstream)

Located at `sources/config.yaml` in the upstream repo:

```yaml
sources:
    - BirthstoneBounce.glyphs
familyName: Birthstone Bounce
outputDir: "../fonts"
buildVariable: false
```

This is a valid gftools-builder configuration. The `config_yaml: "sources/config.yaml"` field in METADATA.pb correctly points to this file.

### Local Override

No override `config.yaml` existed in the google/fonts family directory.

## Font Files

| File | Size |
|------|------|
| BirthstoneBounce-Regular.ttf | 326,712 bytes |
| BirthstoneBounce-Medium.ttf | 322,404 bytes |

## Status

- **Repository URL:** Correct
- **Commit hash:** Accepted (only commit in repo; binaries match; original commit lost to force-push)
- **config_yaml:** Correct (`sources/config.yaml` exists at the referenced commit)
- **Overall status:** Complete
- **Confidence:** HIGH

No changes needed. The source block in METADATA.pb is accurate and complete.
