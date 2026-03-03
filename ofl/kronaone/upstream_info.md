# Investigation: Krona One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Krona One |
| Slug | krona-one |
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

The METADATA.pb for Krona One has no `source` block. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com) with Reserved Font Name 'Krona'."

The DESCRIPTION.en_us.html credits "Sorkin Type Co" and mentions the source files were available from "Google Code" (http://code.google.com/p/googlefontdirectory/), which is no longer available.

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/kronaone` contains TTX source files:
- `KronaOne-Regular.ttf.*` (TTX dumps)
- No Glyphs, UFO, or other editable source formats

The FONTLOG.txt confirms the Sorkin Type Co origin with contact email `sorkineben@gmail.com`. No upstream GitHub repository was found in the cache. The original source was on Google Code, which has been shut down.

## Conclusion

The font is an old sans-serif from 2012 with no tracked upstream repository. The original sources were on Google Code (now defunct). The librefonts cache contains only TTX dumps. No `config.yaml` is possible with the current sources. This family needs further investigation to find if sources were migrated from Google Code to GitHub.
