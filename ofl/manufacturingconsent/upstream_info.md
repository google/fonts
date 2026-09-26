# Manufacturing Consent — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The METADATA.pb at `ofl/manufacturingconsent/METADATA.pb` already contains a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/manufacturing-consent-font"
  commit: "80c3d822c2459ac0d76f8cb9d7ca1ca89a068f3b"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/ManufacturingConsent-Regular.ttf"
    dest_file: "ManufacturingConsent-Regular.ttf"
  }
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "article/showing.jpg"
    dest_file: "article/showing.jpg"
  }
  branch: "master"
}
```

## Repository Analysis

- **Repository**: https://github.com/googlefonts/manufacturing-consent-font
- **Default branch**: master
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/manufacturing-consent-font`
- **Remote verified**: URL matches the `repository_url` in METADATA.pb

The repository was originally `ctrlcctrlv/chomsky`, a font named "Chomsky" created by Fredrick Brennan. It was forked/recreated under the `googlefonts` organization as `manufacturing-consent-font` when it was renamed for the Google Fonts onboarding. The font is a newspaper masthead display font in the style of the New York Times masthead.

### Source files at referenced commit (80c3d82)

- `sources/ManufacturingConsent.glyphspackage` — Glyphs package source
- `sources/config.yaml` — gftools-builder config
- `fonts/ttf/ManufacturingConsent-Regular.ttf` — pre-built TTF binary
- `article/ARTICLE.en_us.html` and `article/showing.jpg` — article assets
- `OFL.txt` — license file

### Contributors

- Fredrick Brennan (original designer, `copypaste@kittens.ph`)
- Yanone (onboarding engineer, `post@yanone.de`)
- Dave Crossland (README update after onboarding)
- Mark E. Shoulson and gosh-darn (earlier contributions)

### Commits after referenced hash

Only one commit exists after `80c3d82`:
- `09d87b3` (2025-05-28): "Update README.md" by Dave Crossland — a non-functional change (README only), no impact on font sources or binaries.

## Onboarding History

The font was added to Google Fonts through PR #9496, created by Yanone (the onboarding engineer) and merged on 2025-05-30.

### Key commits in google/fonts

1. `d893d58f3` (2025-05-23): "Manufacturing Consent: Version 3.000; ttfautohint (v1.8.4.7-5d5b) added" — the initial onboarding commit. The commit message explicitly states: "Taken from the upstream repo https://github.com/googlefonts/manufacturing-consent-font at commit 80c3d822c2459ac0d76f8cb9d7ca1ca89a068f3b."
2. `fef553597`: "sources info for Manufacturing Consent" — the source block metadata was added in a subsequent commit.

### Issue #2071

The original issue (#2071) was titled "Add Chomsky" and referenced the original repo at `ctrlcctrlv/chomsky`. The font was renamed to "Manufacturing Consent" before onboarding, and the source repository was recreated under `googlefonts/manufacturing-consent-font`.

### Binary verification

The TTF file in `ofl/manufacturingconsent/ManufacturingConsent-Regular.ttf` has MD5 hash `beb61955b202a28597c44597add32572`, which exactly matches the file at `fonts/ttf/ManufacturingConsent-Regular.ttf` in the upstream repo at commit `80c3d82`. This confirms the commit hash is correct.

## Build Configuration

The upstream repository contains a `sources/config.yaml` at the referenced commit with the following content:

```yaml
sources:
  - ManufacturingConsent.glyphspackage
buildOTF: false
buildWebfont: false
```

The config references the Glyphs package source file located at `sources/ManufacturingConsent.glyphspackage`. No override config.yaml exists in the google/fonts family directory. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml`.

## Findings

1. **Source block is complete and correct**: The METADATA.pb contains all required fields — `repository_url`, `commit`, `config_yaml`, `branch`, and `files` mappings.
2. **Commit hash verified**: The referenced commit `80c3d822c2459ac0d76f8cb9d7ca1ca89a068f3b` was confirmed through binary file comparison (MD5 match) and consistent with the onboarding PR (#9496) message.
3. **Config path verified**: `sources/config.yaml` exists at the referenced commit and contains valid gftools-builder configuration.
4. **No issues found**: The source block is accurate and no corrections are needed.
5. **Historical note**: The font was originally named "Chomsky" (repo `ctrlcctrlv/chomsky`) and was renamed to "Manufacturing Consent" for the Google Fonts catalog. The upstream repo was recreated under the `googlefonts` organization.

## Recommended Source Block

No changes needed. The current source block is complete and correct:

```
source {
  repository_url: "https://github.com/googlefonts/manufacturing-consent-font"
  commit: "80c3d822c2459ac0d76f8cb9d7ca1ca89a068f3b"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/ManufacturingConsent-Regular.ttf"
    dest_file: "ManufacturingConsent-Regular.ttf"
  }
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "article/showing.jpg"
    dest_file: "article/showing.jpg"
  }
  branch: "master"
}
```
