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


## Update (2026-04-24)

**Model**: Claude Opus 4.7 (1M context)

Added `config_yaml: "sources/config.yaml"` to the METADATA.pb `source { }` block. Direct inspection of the upstream repo at the pinned commit `85646f13` (via the bare mirror in `upstream_repos/repo_archive/wix-incubator/wixmadefor.git`) confirms that `sources/config.yaml` exists at that commit and is a valid gftools-builder config — it declares the `sources:` key. The family should move from the dashboard's "missing_config" bucket into "covered" once `google-fonts-sources` regenerates crater's `targets.json`.

The upstream repo at `85646f13` contains three gftools-builder configs — `sources/config.yaml` (builds Text + Display variable fonts), `sources/config_display.yaml` (Display statics only), and `sources/config_text.yaml` (Text statics only). The shipped `WixMadeforText[wght].ttf` is a variable font, and the sibling family Wix Madefor Display already records `config_yaml: "sources/config.yaml"` — so the shared VF config is the right pointer for Wix Madefor Text too.
