# Investigation: IM Fell Double Pica

## Summary

| Field | Value |
|-------|-------|
| Family Name | IM Fell Double Pica |
| Slug | im-fell-double-pica |
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

The METADATA.pb at `ofl/imfelldoublepica/METADATA.pb` contains no source block. The font was added to google/fonts in the initial commit (`90abd17b4f97671435798b6147b698aa9087612f`, dated 2015-03-07) by Dave Crossland, along with all other IM Fell variants. This predates the practice of tracking upstream repository information.

The git log for `ofl/imfelldoublepica/` shows:
- `49cd93129` — "imfelldoublepica: rename fonts and regenerate METADATA.pb" (renamed `IMFeDPit28P.ttf` → `IMFELLDoublePica-Italic.ttf` and `IMFeDPrm28P.ttf` → `IMFELLDoublePica-Regular.ttf`)
- `90abd17b4` — "Initial commit"

None of these commits reference an upstream repository URL or commit hash.

The font was designed by Igino Marini (iginomarini.com). The copyright string reads: "© 2007 Igino Marini (www.iginomarini.com mail@iginomarini.com)".

A repository `https://github.com/librefonts/imfelldoublepica` exists in the local cache at `upstream_repos/fontc_crater_cache/librefonts/imfelldoublepica`. This repo has a single commit (`35b0c6ea`, "update .travis.yml", 2014-10-17) and contains only TTX-disassembled font data (no VFB or other editable source files, only `src/METADATA_comments.txt` and `src/VERSIONS.txt`). The font version documented is 3.00.

This `librefonts/imfelldoublepica` repository appears to be an archival mirror of the compiled TTF, not the original design source. Igino Marini does not appear to have a public GitHub repository for the IM Fell fonts; the actual sources were originally provided from his personal website (www.iginomarini.com).

Since the available "source" is only a TTX decomposition of prebuilt binaries (not editable design files), and there are no VFB or Glyphs/UFO/designspace sources available, it is unclear whether a `config.yaml` can be meaningfully constructed. The `librefonts/imfelldoublepica` repo does not provide a buildable source.

No Google Fonts config.yaml override exists in `ofl/imfelldoublepica/` in google/fonts.

## Conclusion

The source block is missing from METADATA.pb. The most likely upstream candidate is `https://github.com/librefonts/imfelldoublepica` (an archival TTX mirror), but this is not a true upstream design source. The actual designer (Igino Marini) does not appear to maintain a public GitHub repository. A question should be raised with the Google Fonts team about whether `librefonts/imfelldoublepica` is the appropriate repository to reference, and what commit to use. Until the upstream source situation is clarified, this family requires further investigation or a question to the original onboarding engineer (Dave Crossland).
