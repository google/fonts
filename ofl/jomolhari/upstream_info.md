# Investigation: Jomolhari

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jomolhari |
| Slug | jomolhari |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `ofl/jomolhari/` directory contains `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `Jomolhari-Regular.ttf`, `METADATA.pb`, and `OFL.txt`. The METADATA.pb has no `source { }` block.

The font's history in google/fonts is as follows:
- `90abd17b4` (Initial commit, 2015-03-07): Added `ofl/jomolhari/Jomolhari-alpha3c-0605331.ttf` along with FONTLOG, DESCRIPTION, and OFL.txt.
- `636da261d` (2019-09-11, "jomolhari: gen metadata and hotfix font"): The font file was renamed from `Jomolhari-alpha3c-0605331.ttf` to `Jomolhari-Regular.ttf` (with slight binary changes), and METADATA.pb was created.

The FONTLOG.txt describes the font as "alpha version 0.003c" from 2005-05-31 by Christopher Fynn. The original filename `Jomolhari-alpha3c-0605331.ttf` encodes "alpha3c" (version 0.003c) and "0605331" (likely a date or revision reference from the original non-git hosting).

The original DESCRIPTION linked to `https://sites.google.com/site/chrisfynn2/home/fonts/jomolhari` (a Google Sites page). The current DESCRIPTION no longer includes this link.

The copyright is "Copyright (c) 2006, Christopher J Fynn. All rights reserved." The font is a Tibetan script typeface for Tibetan and Dzongkha text.

No modern git repository for Jomolhari was found in the cache at `upstream_repos/fontc_crater_cache/`. The original distribution appears to have been hosted on Google Sites/Code or a similar pre-git platform (circa 2005-2006). This font predates GitHub and modern version control workflows for font projects.

## Conclusion

No source block exists in METADATA.pb and no upstream git repository is known. The font originates from a 2005/2006 project by Christopher Fynn hosted on Google Sites, which is not a git-based repository. A public git repository likely does not exist for this project. This is a case where a `no_config_possible` or `missing_url` status is appropriate. Further investigation is needed to determine if a modern git hosting exists for this font.
