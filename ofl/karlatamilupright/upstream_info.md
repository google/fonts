# Investigation: Karla Tamil Upright

## Summary

| Field | Value |
|-------|-------|
| Family Name | Karla Tamil Upright |
| Slug | karla-tamil-upright |
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

The METADATA.pb for Karla Tamil Upright has no `source` block at all. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository, which predates the source metadata tracking system.

The copyright notice reads: "Copyright (c) 2011-2012, Jonathan Pinhorn (jonpinhorn.typedesign@gmail.com), with Reserved Font Names 'Karla'"

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/karlatamilupright` contains only TTX/VFB source files (not gftools-builder compatible). The sources are legacy font engineer tools similar to its sister family Karla Tamil Inclined.

There is no `config.yaml` in the upstream repo, and the sources are not in a gftools-builder compatible format. Both Karla Tamil families were created by Jonathan Pinhorn in 2011-2012 for Tamil script support.

The upstream source repository is not publicly known and has not been found in available caches.

## Conclusion

The font is an old font from 2012 with no tracked upstream repository. The librefonts cache contains only a mirror of the binary TTFs with TTX dumps, not the original source files. No `config.yaml` is possible with these sources. This family shares the same situation as Karla Tamil Inclined and needs further investigation to find the original upstream repository if one exists.
