# Investigation: Karla Tamil Inclined

## Summary

| Field | Value |
|-------|-------|
| Family Name | Karla Tamil Inclined |
| Slug | karla-tamil-inclined |
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

The METADATA.pb for Karla Tamil Inclined has no `source` block at all. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository, which predates the source metadata tracking system.

The copyright notice reads: "Copyright (c) 2011-2012, Jonathan Pinhorn (jonpinhorn.typedesign@gmail.com), with Reserved Font Names 'Karla'"

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/karlatamilinclined` contains only TTX/VFB source files (not gftools-builder compatible). The source files found in the `src/` directory are:
- `KarlaInclined-Bold-InVOLT.ttf.*` (TTX dumps of InVOLT-processed TTF)
- VFB files for FontLab

There is no `config.yaml` in the upstream repo, and the sources are not in a gftools-builder compatible format (Glyphs, UFO, or Designspace). These are legacy font engineer tools.

The upstream source repository for Jonathan Pinhorn's Karla Tamil fonts is not publicly known and has not been found in available caches.

## Conclusion

The font is an old font from 2012 with no tracked upstream repository. The librefonts cache contains only a mirror of the binary TTFs with TTX dumps, not the original source files. No `config.yaml` is possible with these sources. This family needs further investigation to find the original upstream repository if one exists.
