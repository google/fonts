**Model**: Claude Opus 4.6

# Wix Madefor Text — Upstream Source Investigation

## Summary

The upstream source repository for Wix Madefor Text was identified and a source block was added to `METADATA.pb`.

## Repository

- **URL**: https://github.com/wix-incubator/wixmadefor
- **Owner**: Wix (wix-incubator organization)
- **Designer**: Dalton Maag
- **Source format**: UFO (multiple masters for both Text and Display variants)
- **Branch**: main
- **Commit**: `85646f130c8d3edffe66c4d8755c3f9f7abfa877`
- **Commit date**: 2023-08-01
- **Commit message**: "Add arrows and checkmark (#23)"

## Investigation Notes

The repository was found at `wix-incubator/wixmadefor` (also accessible via the `wix/wixmadefor` redirect). The DESCRIPTION.en_us.html in google/fonts referenced `github.com/wix/wixmadefor`, and the font copyright string referenced `https://github.com/wix/wixmadefor/`. The repository contained UFO sources for both Wix Madefor Text and Wix Madefor Display in the `sources/` directory, along with designspace files and a `config.yaml` for gftools builds. The repo is not a fork and was created using the googlefonts project template.

## Confidence

High — the repository URL is referenced in both DESCRIPTION.en_us.html and the font copyright string, and the UFO sources for the Text variant were confirmed present.
