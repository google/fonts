# Pangolin — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Pangolin was identified at https://github.com/googlefonts/pangolin, hosted under the `googlefonts` GitHub organization. The METADATA.pb file referenced commit `8257f00935ee0d1dba28c9e9142c85bcb357aae2`. No config_yaml or explicit file mappings were specified in the source block, indicating the font binary is built directly from the repository defaults.

## Font Description

Pangolin is a handwriting typeface designed by Kevin Burke. It is a casual, semi-connected script suitable for body text and informal use. The font covers Latin, Cyrillic (including Extended), and Vietnamese scripts, making it broadly applicable for multilingual content.

## Designer

Kevin Burke is the designer of Pangolin. The copyright dates to 2016.

## Repository

- **URL**: https://github.com/googlefonts/pangolin
- **Commit**: `8257f00935ee0d1dba28c9e9142c85bcb357aae2`
- **License**: OFL

## Font Details

| Property | Value |
|----------|-------|
| Category | HANDWRITING |
| Style | Regular (400) |
| Subsets | latin, latin-ext, cyrillic, cyrillic-ext, vietnamese |
| Variable | No |

## Notes

The source block contained no `config_yaml` or explicit `files` mappings, which is minimal compared to most current Google Fonts source entries. No branch was specified either.

## Confidence

**High** — The repository is hosted under the `googlefonts` organization and the commit is explicitly referenced. The copyright notice matches the repository URL.
