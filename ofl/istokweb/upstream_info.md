# Investigation: Istok Web

## Summary

| Field | Value |
|-------|-------|
| Family Name | Istok Web |
| Slug | istok-web |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The font is stored under `ofl/istokweb/` with an OFL license. The METADATA.pb has no `source` block at all.

The font history in google/fonts shows:
- `90abd17b4` — "Initial commit" — the font was present from the very beginning of the google/fonts repository (2015)

The copyright states: "Copyright (c) 2008-2014, Andrey V. Panov (panov@canopus.iacp.dvo.ru), with Reserved Font Name Istok"

The FONTLOG.txt in the google/fonts directory reveals:
> The sources and truetype fonts are available at http://code.google.com/p/istok/

This points to **Google Code** (code.google.com/p/istok), which has been shut down since 2016. The font sources were originally hosted on Google Code, not GitHub.

The FONTLOG also describes the build requirements:
> "You need fontforge (http://fontforge.sourceforge.net/), TTX/FontTools, xgridfit (http://xgridfit.sourceforge.net/ - version as of April 2010) and font-helpers (http://code.google.com/p/font-helpers/) in order to build the truetype fonts from the sources."

The sources were in SFD format (FontForge native format) based on the build instructions mentioning fontforge and xgridfit. There is no known GitHub mirror of the original Google Code repository.

No cached upstream repository was found in `upstream_repos/fontc_crater_cache/` for this family.

The designer is Andrey V. Panov (email: panov@canopus.iacp.dvo.ru). The font supports Latin and Cyrillic scripts.

## Conclusion

The original source repository was on Google Code (`http://code.google.com/p/istok/`) which has been shut down. No GitHub repository has been identified. The source format was SFD (FontForge) files, and there is likely no modern gftools-builder compatible `config.yaml` possible for this font.

Action needed: Check if there is a GitHub mirror of the Google Code repository, or if the font can be considered `no_config_possible` given its SFD source format and the Google Code origin.
