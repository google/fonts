# Beth Ellen

**Model**: Claude Opus 5.5
**Date**: 2026-11-20

Sources modernized 2026-11: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Beth Ellen built from FontForge `.sfd` sources in
https://github.com/googlefonts/BethEllen at commit
`d6c8d9b3871c432c6abfd71660885f16ddbce3e2`. There was no source that builds with fontc.

## Actions taken

- The work was done on top of the upstream history, in
  https://github.com/googlefonts/BethEllen.
- Its default branch had 3 later commits (wip - manually tweaking glyph outlines; a lot
  more improvements; Update README.md for typo); a commit restored the sources as at
  `d6c8d9b3871c`, the revision Google Fonts ships, so they stay in history but are not
  part of this conversion.
- Each change to the `.sfd` before conversion is its own commit: Set UnderlinePosition
  so the build gets the release's -249.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last change to the font.

## Final state

The source is https://github.com/googlefonts/BethEllen at `d2eebcc2584a`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts cc39c4c2c304 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF, hinting), 1 style. Those tools,
including this family's plan `plans/bethellen.json`:
https://github.com/felipesanches/gf-source-modernization at `5d88a7c`.

`d2eebcc2584a` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Where the shipped
binaries differ from the source, the difference is reproduced by a documented commit
before the conversion, never silently corrected. Any improvement is a later commit that
needs its own QA, and is left as future work for an onboarder to review in a font-update
PR.

## Previous source block

The source block this replaces (the same repository, before this work), preserved for
provenance:

    source {
      repository_url: "https://github.com/googlefonts/BethEllen"
      commit: "d6c8d9b3871c432c6abfd71660885f16ddbce3e2"
    }

## Previous investigation

## Beth Ellen - Investigation Report

### Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Beth Ellen |
| Repository URL | https://github.com/googlefonts/BethEllen |
| Commit Hash | d6c8d9b3871c432c6abfd71660885f16ddbce3e2 |
| Config YAML | (none) |
| Status | missing_config |
| Category | HANDWRITING |

### How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/BethEllen` was already present in the METADATA.pb `source{}` block. It was first added by commit `f7455d788` ("Populate source.repository_url") and confirmed by the copyright string in the font metadata: "Copyright 2019 The Beth Ellen Project Authors (https://github.com/googlefonts/BethEllen)". An earlier commit `2bf30f384` also updated the font project URL to point to `googlefonts/BethEllen`.

### How the Commit Hash Was Determined

The commit hash `d6c8d9b3871c432c6abfd71660885f16ddbce3e2` was found in the original google/fonts commit `0aa5f370a` (2019-05-10) by Felipe Sanches, which added Beth Ellen to the catalog. The commit message reads: "Add Beth Ellen (Version 2.000)" and includes the URL `(https://github.com/googlefonts/BethEllen/commit/d6c8d9b3871c432c6abfd71660885f16ddbce3e2)`.

The commit hash was later added to the METADATA.pb source block in the batch commit `9a14639f3` (2026-02-25): "Add source blocks to 602 more METADATA.pb files".

The upstream commit `d6c8d9b` is: "manual fixes using gftools and ttx" - this is the commit from which the font binary was taken when onboarding Beth Ellen.

### Config YAML Status

**No config.yaml exists** in the upstream repository, either at the recorded commit or at HEAD.

At the recorded commit `d6c8d9b`, the repository structure is:
- `BethEllen-Regular.sfd` (FontForge source)
- `BethEllen-Regular.ttf` (pre-built binary)
- `BethEllen-Story.pdf`
- `OFL.txt`
- `README.md`
- `old/` and `prebuilt/` directories

The font source is in SFD (FontForge) format, which is not compatible with gftools-builder. At HEAD, a `.glyphs` file has been added (`BethEllen-Regular.glyphs`), but still no config.yaml.

No override config.yaml exists in the google/fonts family directory either.

### Verification

- **Repository exists**: Yes, confirmed locally in cache at `upstream_repos/fontc_crater_cache/googlefonts/BethEllen`
- **Commit hash exists**: Yes, verified: `d6c8d9b manual fixes using gftools and ttx`
- **Config.yaml exists**: No, neither in upstream repo nor as override
- **Source format**: SFD (FontForge) - not gftools-builder compatible

### Confidence Level

**High** - The commit hash is explicitly documented in the original google/fonts commit message by the person who performed the onboarding (Felipe Sanches). The upstream commit exists and is verified. The lack of config.yaml is expected given the SFD-only source format.

### Open Questions

- The upstream repo now has a `.glyphs` file at HEAD (not present at the recorded commit). A config.yaml could potentially be created for future builds using this newer source, but that would require a separate review process.
- The status remains `missing_config` because no gftools-builder configuration exists.
