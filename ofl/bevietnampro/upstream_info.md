# Investigation Report: Be Vietnam Pro

- **Family name**: Be Vietnam Pro
- **Slug**: bevietnampro
- **Date investigated**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Confidence**: HIGH

## METADATA.pb Current State

- **Repository URL**: https://github.com/bettergui/BeVietnamPro
- **Commit**: `804e62d81abbbcdcce5686069c69b41b8c245192`
- **Branch**: main
- **Config YAML**: `sources/config.yaml`
- **Designer**: Lam Bao, Tony Le, VietAnh Nguyen
- **License**: OFL
- **Category**: SANS_SERIF
- **Date added**: 2021-06-13
- **Subsets**: latin, latin-ext, menu, vietnamese

## Source Block Assessment

The existing source block in METADATA.pb was already complete with repository URL, commit hash, branch, config_yaml path, and file mappings. No changes are needed.

## Upstream Repository Analysis

- **Repository**: https://github.com/bettergui/BeVietnamPro
- **Cached at**: upstream_repos/fontc_crater_cache/bettergui/BeVietnamPro
- **Repo status**: Clean (no local modifications)
- **Remote URL**: https://github.com/bettergui/BeVietnamPro (verified)
- **Total commits**: 1 (single-commit repository)
- **Only commit**: `804e62d` - "fix(sources): Update winAscent in Master" (2021-08-14)

Since the repository contained only a single commit, `804e62d` was necessarily the commit used for onboarding. There was no ambiguity about which commit to reference.

### Source Files at Commit 804e62d

The `sources/` directory contained:
- `BeVietnamPro.glyphs` (upright master)
- `BeVietnamPro-Italic.glyphs` (italic master)
- `config.yaml` (gftools-builder configuration)

### config.yaml Contents (at sources/config.yaml)

```yaml
    sources:
      - BeVietnamPro.glyphs
      - BeVietnamPro-Italic.glyphs
    axisOrder:
      - wght
      - ital
    familyName: Be Vietnam Pro
```

The config.yaml referenced source files using paths relative to its own directory (`sources/`), which was standard for gftools-builder configurations.

### Pre-built TTF Files

The repository included pre-built TTF files at `fonts/ttf/`. The METADATA.pb source block mapped these pre-built files directly to the google/fonts family directory (not compiled from source).

## Commit Hash Verification

The commit hash `804e62d81abbbcdcce5686069c69b41b8c245192` was verified through multiple methods:

1. **Explicit reference in google/fonts PR #3771**: The commit message for `1cfe4cb` (merged 2021-08-27) stated: "Be Vietnam Pro Version 1.002; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/bettergui/BeVietnamPro at commit https://github.com/bettergui/BeVietnamPro/commit/804e62d81abbbcdcce5686069c69b41b8c245192."

2. **Single-commit repository**: The upstream repo contained exactly one commit, so there was no possibility of a different commit having been used.

3. **Binary file size match**: All 18 TTF files at commit `804e62d` in the upstream repo matched the file sizes in google/fonts exactly:
   - BeVietnamPro-Thin.ttf: 127,040 bytes (match)
   - BeVietnamPro-ThinItalic.ttf: 129,556 bytes (match)
   - BeVietnamPro-ExtraLightItalic.ttf: 131,492 bytes (match)
   - BeVietnamPro-Regular.ttf: 132,948 bytes (match)
   - BeVietnamPro-ExtraLight.ttf: 134,464 bytes (match)
   - BeVietnamPro-SemiBoldItalic.ttf: 134,740 bytes (match)
   - BeVietnamPro-Medium.ttf: 135,980 bytes (match)
   - BeVietnamPro-LightItalic.ttf: 136,084 bytes (match)
   - BeVietnamPro-SemiBold.ttf: 136,736 bytes (match)
   - BeVietnamPro-Light.ttf: 136,772 bytes (match)
   - BeVietnamPro-Italic.ttf: 137,244 bytes (match)
   - BeVietnamPro-BoldItalic.ttf: 137,748 bytes (match)
   - BeVietnamPro-ExtraBoldItalic.ttf: 138,076 bytes (match)
   - BeVietnamPro-MediumItalic.ttf: 138,280 bytes (match)
   - BeVietnamPro-ExtraBold.ttf: 139,680 bytes (match)
   - BeVietnamPro-Bold.ttf: 140,300 bytes (match)
   - BeVietnamPro-BlackItalic.ttf: 140,468 bytes (match)
   - BeVietnamPro-Black.ttf: 142,612 bytes (match)

## google/fonts History

The font's history in google/fonts:

1. **2021-07-15**: Initial onboarding as "Be Vietnam Pro: Version 1.000 added (#3456)" by bettergui, co-authored by Rosalie Wagner. The source block was removed from METADATA.pb during this commit.
2. **2021-08-27**: Updated to "Version 1.002; ttfautohint (v1.8.3) added (#3771)" by Rosalie Wagner, using gftools-packager from commit `804e62d`.
3. **2024-04-03**: Source block with repository_url and file mappings added by Simon Cozens via "Merge upstream.yaml into METADATA.pb" commit.
4. **2025-03-31**: Commit hash and config_yaml path added by Felipe Sanches via "[Batch 1/4] port info from fontc_crater targets list" commit.

## Override Config Assessment

No override config.yaml was needed. The upstream repository already contained a valid `sources/config.yaml` at the referenced commit, and this path was correctly recorded in METADATA.pb as `config_yaml: "sources/config.yaml"`.

## Conclusion

The source block in METADATA.pb for Be Vietnam Pro was already complete and accurate. All fields were verified:
- Repository URL pointed to a valid, accessible repository
- Commit hash matched the only commit in the repository and was confirmed by the google/fonts PR #3771 commit message
- Binary files at the referenced commit matched exactly (all 18 TTFs had identical sizes)
- config.yaml existed at `sources/config.yaml` in the upstream repo and correctly referenced the .glyphs source files
- No action was required
