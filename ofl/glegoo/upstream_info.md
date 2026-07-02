# Investigation Report: Glegoo

## Summary

Glegoo is a slab serif typeface designed by Eduardo Tunni, featuring Regular and Bold weights with Latin and Devanagari script support. The upstream repository at `https://github.com/etunni/glegoo` contains FontForge SFD source files. The METADATA.pb already has a source block with repository_url and commit hash, and an override config.yaml exists in the google/fonts family directory. However, the override config.yaml only references `Glegoo-Regular.sfd` and omits `Glegoo-Bold.sfd`, which means it cannot produce the full family.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Glegoo |
| Designer           | Eduardo Tunni |
| Repository URL     | https://github.com/etunni/glegoo |
| Commit Hash        | a6b0a10abfaf1b88feb4a9f9eb731beefbb4bbb8 |
| Config YAML        | Override config.yaml in google/fonts (needs correction) |
| Source Type        | FontForge SFD (.sfd) |
| Weights            | Regular (400), Bold (700) |
| Status             | needs_correction |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a source block added by Simon Cozens (commit 474a446c0, 2024-01-14) with the repository_url, later enriched by Felipe Sanches (commit f7b6a76a3, 2025-10-30) with the commit hash `a6b0a10abfaf1b88feb4a9f9eb731beefbb4bbb8`. No `config_yaml` field is set in the source block, which is correct since there is a local override config.yaml.

### Upstream Repository

- **URL**: https://github.com/etunni/glegoo
- **Cached at**: upstream_repos/fontc_crater_cache/etunni/glegoo
- **Remote verified**: Yes, remote origin matches the METADATA.pb repository_url

The repository contains:
- `Glegoo-Regular.sfd` - FontForge source for Regular weight (v2.0.1)
- `Glegoo-Bold.sfd` - FontForge source for Bold weight (v2.0.1)
- `Glegoo-Regular.ttf` - Pre-compiled Regular binary
- `Glegoo-Bold.ttf` - Pre-compiled Bold binary
- `OFL.txt`, `FONTLOG.txt` - License and font log
- No config.yaml in the upstream repo
- No .glyphs, .ufo, or .designspace files

### Commit Hash Verification

The referenced commit `a6b0a10` (2014-08-27, "Update files and image") is the HEAD of the repository's master branch. It only modified documentation files (PDF sample and InDesign template), not the font sources.

The SFD source files were last updated in commit `99fd234` (2014-08-12, "New ttf's with auto hinting version 1.1"). The commit `a6b0a10` is acceptable as the reference since it is the latest commit in the repo and the SFD files at that commit are identical to those at `99fd234`.

The TTF files in google/fonts do not match the pre-compiled TTFs in the upstream repo (different md5 checksums), indicating the fonts in google/fonts were rebuilt from the SFD sources during onboarding rather than copied directly.

### Google Fonts History

- **Initial commit** (90abd17b4, 2015-03-07): Font files were added in the initial commit of the google/fonts repository.
- **No TTF updates**: The TTF files have never been updated since the initial commit.

### Override config.yaml Issue

The current override config.yaml in `ofl/glegoo/config.yaml` contains:

```yaml
buildVariable: false
sources:
  - Glegoo-Regular.sfd
```

This only references the Regular weight. The Bold weight (`Glegoo-Bold.sfd`) is a separate SFD file in the upstream repo and should also be listed. Without it, gftools-builder would only produce the Regular weight, not the full family.

## Conclusion

The source block in METADATA.pb is correct (repository_url and commit hash are both valid). However, the override config.yaml needs correction to include both SFD sources. Note that SFD is not a modern gftools-builder source format, so building from these sources may not be fully supported by the current toolchain.

### Recommended METADATA.pb Source Block

The existing source block is correct and does not need changes:

```
source {
  repository_url: "https://github.com/etunni/glegoo"
  commit: "a6b0a10abfaf1b88feb4a9f9eb731beefbb4bbb8"
}
```

### Recommended Override config.yaml Correction

```yaml
buildVariable: false
sources:
  - Glegoo-Regular.sfd
  - Glegoo-Bold.sfd
```

### Status: needs_correction

The METADATA.pb source block is complete, but the override config.yaml should be corrected to include both the Regular and Bold SFD sources.
