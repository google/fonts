# Galindo

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Galindo (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/galindo.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Galindo-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/galindo at `1856721cb25c`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Galindo-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/galindo.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`1856721cb25c` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The build's GSUB numbers or packs some lookups differently from the release's (fontc
  places a lookup that only a contextual lookup calls, and packs chained contextual
  rules, its own way: gfonts-ai-usage-report 22-fontc-problems, problems 12 and 13);
  every rule is the same and the text shapes identically (tools/functional_gate.py).
  Decided 2026-10-02: problems that need fontc are disclosed and fixed in fontc later.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/galindo at dc5fea52318d56672b1e3f000851806c8b5bd2cc:
  src/Galindo-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/galindo"
      commit: "dc5fea52318d56672b1e3f000851806c8b5bd2cc"
    }

## Previous investigation

## Investigation Report: Galindo

### Summary

Galindo is a display typeface designed by Brian J. Bonislawsky (Astigmatic/AOETI). It was part of the initial commit to the google/fonts repository on 2015-03-07. The upstream repository is `librefonts/galindo`, a single-commit archive repo created by Alexei Vanyashin (hash3g) on 2014-10-17. The repo contains only legacy VFB sources with no gftools-builder compatible formats.

### Key Findings

| Field             | Value                                                    |
|-------------------|----------------------------------------------------------|
| Family Name       | Galindo                                                  |
| Repository URL    | https://github.com/librefonts/galindo                    |
| Commit Hash       | dc5fea52318d56672b1e3f000851806c8b5bd2cc                 |
| Config YAML       | None (VFB sources only)                                  |
| Source Type        | VFB (legacy FontLab format)                              |
| Status            | no_config_possible                                       |
| Confidence        | HIGH                                                     |
| Date Added        | 2012-08-13                                               |

### Investigation Details

#### METADATA.pb Review

The current METADATA.pb has no `source { }` block. The font is listed under the OFL license with designer "Astigmatic". Copyright references Brian J. Bonislawsky DBA Astigmatic (AOETI).

#### Git History in google/fonts

- **90abd17b4** (2015-03-07): "Initial commit" by Dave Crossland - The font was included in the massive initial commit that added all fonts to the google/fonts repository.
- **76adaf1d2**: Deploy commit (no font changes).

The font binary (Galindo-Regular.ttf) has never been modified since the initial commit. All subsequent commits touching the directory were metadata-only changes (METADATA.pb updates, language support, classifications, etc.).

#### FONTLOG.txt

The FONTLOG.txt in the google/fonts directory documents:
- Version 1.001, released 2012-05-24
- Three source files mentioned: Galindo-Regular.vfb (original), Galindo-Regular-OTF.vfb (merged contours for OTF), Galindo-Regular-TTF.vfb (TrueType outlines with hinting)

#### Upstream Repository

The repo `librefonts/galindo` was created on 2014-07-16 and last pushed on 2014-10-17. It contains a single commit:

- **dc5fea5** (2014-10-17): "update .travis.yml" by hash3g (Alexei Vanyashin) - This is a squashed initial commit that includes all files: TTX decompositions, source files, metadata, and Travis CI configuration.

The `librefonts` organization is a collection of archived font repos, typically migrated from the old Google Font Directory.

#### Source Files

The repo contains legacy VFB source files only:
- `src/Galindo-Regular.vfb` - Original FontLab source with contour overlaps
- `src/Galindo-Regular-OTF.vfb` - OTF-specific FontLab source (merged contours)
- `src/Galindo-Regular-TTF.vfb` - TrueType outlines with hinting adjustments

All three are binary VFB files (FontLab Studio format). Additionally, the repo has extensive TTX decompositions of both the TTF and OTF at the root level and in `src/`.

The `src/VERSIONS.txt` confirms: "Galindo-Regular.ttf: Version 1.000"

The `src/METADATA_comments.txt` contains the original subsetting/processing commands from the Google Font Directory workflow.

#### Config YAML Assessment

No `config.yaml` exists. The only source format is VFB (proprietary FontLab Studio), which is not compatible with gftools-builder. Creating an override config.yaml is not possible without converting the sources to a modern format first.

### Conclusion

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/galindo"
  commit: "dc5fea52318d56672b1e3f000851806c8b5bd2cc"
}
```

**Status**: no_config_possible

**Notes**: This is a legacy font from the original Google Font Directory era. The `librefonts/galindo` repo is an archive containing VFB sources that are not compatible with gftools-builder. The single commit in the repo predates the google/fonts initial commit. No config.yaml can be created without first converting the sources to a modern format (UFO, .glyphs, or .designspace).
