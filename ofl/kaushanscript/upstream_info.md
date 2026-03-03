# Investigation: Kaushan Script

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kaushan Script |
| Slug | kaushan-script |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Kaushan Script has no `source` block. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository.

The copyright notice credits "Pablo Impallari (www.impallari.com|impallari@gmail.com)" and "Igino Marini (www.ikern.com)".

The DESCRIPTION.en_us.html mentions the font was funded via Kickstarter but does not link to a GitHub repository.

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/kaushanscript` contains only TTX/VFB source files (legacy format, not gftools-builder compatible). The `src/` directory contains:
- `KaushanScript-Regular.otf.*.ttx` (OTF TTX dumps)
- `KaushanScript-Regular-OTF.vfb` (FontLab)
- `KaushanScript-Regular-TTF.vfb` (FontLab)
- `KaushanScript-Regular.vfb` (FontLab)

No `config.yaml` exists and the sources are VFB format (not gftools-builder compatible). The Impallari GitHub organization may have a repository for this font, but it was not found in the upstream cache.

## Conclusion

The font is an old font from 2012 with no tracked upstream repository. The librefonts cache contains only TTX/VFB files, not the original Glyphs or UFO sources. This family needs further investigation to identify the original upstream repository. A `config.yaml` is not possible with the current source format.
