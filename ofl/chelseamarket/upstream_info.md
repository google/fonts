# Chelsea Market

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Chelsea Market (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/chelseamarket.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  ChelseaMarket-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/chelseamarket at `620f5bb572e9`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/chelseamarket.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`620f5bb572e9` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/chelseamarket at
  cb0d8b1186fc376de4d6be06a568c25362e381dd: src/ChelseaMarket-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/chelseamarket"
      commit: "cb0d8b1186fc376de4d6be06a568c25362e381dd"
    }

## Previous investigation

## Chelsea Market - Investigation Report

### Source Data

| Field | Value |
|---|---|
| **Family Name** | Chelsea Market |
| **Designer** | Tart Workshop |
| **License** | OFL |
| **Category** | DISPLAY |
| **Date Added** | 2012-01-04 |
| **Repository URL** | https://github.com/librefonts/chelseamarket |
| **Commit Hash** | cb0d8b1186fc376de4d6be06a568c25362e381dd |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config |

### How URL Found

The repository URL `https://github.com/librefonts/chelseamarket` was identified from the librefonts organization on GitHub. The upstream repo is cloned at `upstream_repos/fontc_crater_cache/librefonts/chelseamarket/`.

The repository remote confirms: `origin https://github.com/librefonts/chelseamarket`.

### How Commit Determined

The repository has only a single commit:

```
cb0d8b1 update .travis.yml
```

HEAD is `cb0d8b1186fc376de4d6be06a568c25362e381dd`, which is the only commit in the repository. As with other librefonts archives that have a single commit, there is no ambiguity about which commit to reference.

The font was originally added to google/fonts in the "Initial commit" (`90abd17b4`). Unlike Chela One, it was never updated with binary fixes -- the original binary has remained unchanged. A source block was added on a pending PR branch (`sources_info_2026-02-25`) via commit `9a14639f3`, not yet merged to main.

### Config YAML Status

**No config.yaml possible.** The upstream repository's source directory contains only:
- `src/ChelseaMarket-Regular-TTF.vfb` (FontLab VFB format)

VFB is a proprietary FontLab format that is not compatible with gftools-builder. There are no `.glyphs`, `.ufo`, `.sfd`, or `.designspace` source files. A config.yaml cannot be created without first converting the source to a modern format.

### Verification

- **Repository URL**: Verified - cloned and accessible at `upstream_repos/fontc_crater_cache/librefonts/chelseamarket/`
- **Commit hash**: Verified - matches HEAD, and is the only commit in the repo
- **Source block**: Pending merge via PR branch `sources_info_2026-02-25`
- **METADATA.pb on main**: Currently has no source block (pending PR)

### Confidence Level

**HIGH** for repository URL and commit hash. The librefonts repo is the recognized upstream, and with only one commit, the hash is unambiguous.

**N/A** for config.yaml -- VFB-only sources make this impossible without source conversion.

### Open Questions

- None. This is a legacy font with VFB-only sources. It would require conversion to a modern format before a config.yaml could be created.
