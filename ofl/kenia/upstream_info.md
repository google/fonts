# Investigation: Kenia

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kenia |
| Slug | kenia |
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

The METADATA.pb for Kenia has no `source` block. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2010, Julia Petretta (julia.petretta@googlemail.com), with Reserved Font Name Kenia"

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/kenia` contains only TTX/VFB/SFD source files. The `src/` directory contains:
- `Kenia-Regular.sfd` (FontForge)
- `Kenia-Regular.vfb` (FontLab)
- `Kenia-Regular-TTF.sfd` (FontForge)
- Design documentation PDFs (2010)

The git log shows one commit (`update .travis.yml`). No actual source changes exist beyond the initial librefonts import.

There is no publicly known upstream repository for this Julia Petretta font. Kenia is Julia Petretta's earliest known Google Fonts contribution (2010).

## Conclusion

The font is an old display font from 2010 with no tracked upstream repository. The librefonts cache contains only legacy FontForge/FontLab source files not compatible with gftools-builder. No `config.yaml` is possible with the current sources. This family needs further investigation to find original source files from Julia Petretta.
