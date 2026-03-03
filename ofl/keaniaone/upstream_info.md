# Investigation: Keania One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Keania One |
| Slug | keania-one |
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

The METADATA.pb for Keania One has no `source` block. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2012, Julia Petretta (julia.petretta@googlemail.com), with Reserved Font Name 'Keania'"

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/keaniaone` contains only TTX/VFB source files (legacy format, not gftools-builder compatible). The `src/` directory contains:
- `KeaniaOne-Regular.otf.*` (OTF TTX dumps)
- `KeaniaOne-Regular-OTF.vfb` (FontLab)
- `KeaniaOne-Regular-TTF.sfd` (FontForge)
- `KeaniaOne-Regular.vfb` (FontLab)

There is no publicly known upstream repository for this Julia Petretta font. The librefonts archive only provides the compiled binary and TTX source dumps.

## Conclusion

The font is an old display font from 2012 with no tracked upstream repository. The librefonts cache contains only legacy source files not compatible with gftools-builder. No `config.yaml` is possible with the current sources. Further investigation would require contacting Julia Petretta to find if original source files exist.
