# Aksara Bali Galang

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: needs_investigation
**Designer**: Bemby Bantara Narendra, I Made Suatjana
**METADATA.pb path**: `ofl/aksarabaligalang/METADATA.pb` (does not exist)

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | `https://github.com/librefonts/aksarabaligalang` (secondary; see notes) |
| Commit | `unknown` |
| Config YAML | -- |
| Branch | -- |

## How the Repository URL Was Found

The font directory `ofl/aksarabaligalang/` in google/fonts has **no METADATA.pb file** and never had one. The font was added in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07 by Dave Crossland) and has only been modified twice since, both for technical fixes (nbspace/fsType corrections in commits `06d9851e7` and `bacec3651`, both by Dave Crossland in 2015).

The font binary's name table includes two URLs:
- `http://www.babadbali.com/` -- Yayasan Bali Galang foundation cultural heritage site
- `http://aksarabali.wordpress.com/` -- A blog about Balinese script computerization

Neither of these is a source code repository.

A GitHub search found `librefonts/aksarabaligalang` (created 2014-07-16), which contains the font's TTX decomposition and was created by Vitaly Volkov (vitalyvolkov) as part of the librefonts organization's effort to extract individual fonts from the google/fonts monorepo into separate repositories. The initial commit message is "Move aksarabaligalang font files to separate repository." This is **not the original upstream** -- it is a derivative that extracts the font tables into TTX format for the Font Library project.

No original source repository by the font authors (Bemby Bantara Narendra and I Made Suatjana) was found on GitHub or anywhere else.

## How the Commit Hash Was Identified

No commit hash could be identified. The font was part of the initial monorepo commit of google/fonts, which predates structured onboarding with upstream commit tracking. The `librefonts/aksarabaligalang` repo was created later (July 2014) by extracting from google/fonts, so its commits are not original upstream commits.

## How Config YAML Was Resolved

No config.yaml is possible for this font. The only source files that exist are TTX decompositions (XML representations of font tables). There are no gftools-builder compatible sources (.glyphs, .ufo, .designspace) in any known repository. The font was created using specialized tools for Graphite smart font technology and requires Graphite-enabled applications (e.g., Firefox with Graphite support) to render correctly.

## Additional Context

- **Not on Google Fonts catalog**: This font is present in the google/fonts repository but is NOT served through the Google Fonts API or listed on fonts.google.com (returns 404). Issue [#1102](https://github.com/google/fonts/issues/1102) from 2017 explicitly lists AksaraBaliGalang-Regular among fonts in the repo but absent from the API. Issue [#1590](https://github.com/google/fonts/issues/1590) lists it among fonts with no METADATA.pb.
- **Graphite dependency**: The DESCRIPTION.en_us.html warns that "This font requires a web browser with Graphite support enabled, such as Firefox 11+, to display correctly." This likely explains why it was never fully onboarded to the Google Fonts catalog.
- **Font version**: Version 1.001, 2012 web release
- **Copyright**: 2008-2012, Bemby Bantara Narendra and I Made Suatjana
- **Script**: Balinese (Aksara Bali), an abugida derived from Old Kawi script
- **Designer websites**: babadbali.com (Yayasan Bali Galang foundation), aksarabali.wordpress.com

## Conclusion

**Confidence: LOW**

Aksara Bali Galang is an edge case: it exists in the google/fonts repository but was never fully onboarded to the Google Fonts catalog (no METADATA.pb, not served via the API). The font uses Graphite smart font technology for complex Balinese script rendering, which is not supported by the standard Google Fonts serving infrastructure.

The `librefonts/aksarabaligalang` repository is a secondary extraction, not an original upstream. No original source repository from the font authors exists on GitHub. The only available "sources" are TTX decompositions, which are not gftools-builder compatible.

This font likely needs a decision from the Google Fonts team about whether to:
1. Create a METADATA.pb and formally include it in the catalog (would require Graphite rendering support)
2. Remove it from the repository entirely
3. Leave it as-is in its current limbo state

No source block can be meaningfully added to METADATA.pb at this time due to the absence of both the METADATA.pb file itself and any gftools-builder compatible upstream source.
