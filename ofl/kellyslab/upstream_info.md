# Investigation: Kelly Slab

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kelly Slab |
| Slug | kelly-slab |
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

The METADATA.pb for Kelly Slab has no `source` block. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2011, Denis Masharov <denis.masharov@gmail.com>, with Reserved Font Names 'Kelly', 'Kelly Slab'."

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/kellyslab` contains only TTX/VFB/SFD source files (legacy format, not gftools-builder compatible). The `src/` directory contains:
- `KellySlab-Regular.otf.*` (OTF TTX dumps)
- `KellySlab-Regular.vfb` (FontLab)
- `KellySlab-Regular-TTF.sfd` (FontForge)
- `menusubset-kelly.ff` (FontForge script)

The git log shows commit `ed9a0d2` ("update .travis.yml"). No actual source changes exist in this librefonts mirror.

There is no publicly known upstream GitHub repository for Denis Masharov's Kelly Slab font.

## Conclusion

The font is an old display font from 2011 with no tracked upstream repository. The librefonts cache contains only legacy source files not compatible with gftools-builder. No `config.yaml` is possible with the current sources. This family needs further investigation to find the original upstream repository if one exists.
