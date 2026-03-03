# Investigation: IM Fell Double Pica SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | IM Fell Double Pica SC |
| Slug | im-fell-double-pica-sc |
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

The METADATA.pb at `ofl/imfelldoublepicasc/METADATA.pb` contains no source block. The font was added to google/fonts in the initial commit (`90abd17b4f97671435798b6147b698aa9087612f`, dated 2015-03-07) by Dave Crossland, along with all other IM Fell variants. This predates the practice of tracking upstream repository information.

The git log for `ofl/imfelldoublepicasc/` shows that only metadata/language updates were made after the initial commit; no upstream repository references appear anywhere.

The font was designed by Igino Marini (iginomarini.com). The copyright string reads: "© 2007 Igino Marini (www.iginomarini.com mail@iginomarini.com)". The family is a small caps variant of IM Fell Double Pica. The single font file is `IMFeDPsc28P.ttf` (version 3.00, per the `VERSIONS.txt` in the librefonts archive).

A repository `https://github.com/librefonts/imfelldoublepicasc` exists in the local cache at `upstream_repos/fontc_crater_cache/librefonts/imfelldoublepicasc`. This repo has a single commit (`2274064`, "update .travis.yml", 2014-10-17) and contains only TTX-disassembled font data (no VFB or other editable source files, only `src/METADATA_comments.txt` and `src/VERSIONS.txt`).

Like the non-SC variant, this `librefonts/imfelldoublepicasc` repository is an archival mirror of the compiled TTF, not the original design source. The SC variant was originally provided alongside the other IM Fell variants from Igino Marini's personal website. No public GitHub repository for the actual design sources has been identified.

No Google Fonts config.yaml override exists in `ofl/imfelldoublepicasc/` in google/fonts.

## Conclusion

The source block is missing from METADATA.pb. The situation is identical to IM Fell Double Pica: the only available "upstream" is a TTX archival mirror (`librefonts/imfelldoublepicasc`) with no buildable design sources. A question should be raised with the Google Fonts team (Dave Crossland) about whether `librefonts/imfelldoublepicasc` is the appropriate repository to reference and what the appropriate commit would be. Until clarified, this family requires further investigation into Igino Marini's original source distribution or the `librefonts` organization's use as the canonical source mirror.
