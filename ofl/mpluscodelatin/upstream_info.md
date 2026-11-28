# M PLUS Code Latin - Source Investigation

**Model**: Claude Opus 5.5

## Initial state

- METADATA.pb had a complete source block except for the build config: repository_url https://github.com/coz-m/MPLUS_FONTS, branch master, commit 4bf69824e45a175b9121b248c46abff103569051 and the file mapping fonts/MPLUSCodeLatin/variable/MPLUSCodeLatin[wdth,wght].ttf -> MPLUSCodeLatin[wdth,wght].ttf. Aaron Bell set this commit on 2026-04-09 (google/fonts e20f9bdde, "Updating MPLUS families to version 1.100", PR #10416, merged 2026-04-30).
- METADATA.pb had no config_yaml and the family directory had no override config.yaml.
- The previous upstream_info.md (preserved below) described the version 1.005 state and a 2021 commit found by date correlation.

## Actions taken

- The recorded commit was verified. The shipped MPLUSCodeLatin[wdth,wght].ttf is byte-identical to fonts/MPLUSCodeLatin/variable/MPLUSCodeLatin[wdth,wght].ttf at 4bf6982 (and at 06feee4, the Aaron Bell commit it merges). sources/MPLUS1Code/MPLUS1-code.glyphs is identical at 06feee4 and 4bf6982. The 18 upstream commits between 4bf6982 and the google/fonts merge touched only sources/MPLUS3/MPLUS-3.glyphs. The commit was kept.
- The upstream config sources/MPLUSCodeLatin/config.yaml was examined. It builds merged_ufo/MPLUSCodeLatin.designspace, which the repository does not contain: the Makefile (make prep merge) converts MPLUS1-code.glyphs to UFO masters and sources/scripts/merge.py copies them with the family renamed to "M PLUS Code Latin". Building that config from a clean checkout failed in gftools-builder3 and in gftools builder, so config_yaml was not set.
- An override config.yaml was added. It builds sources/MPLUS1Code/MPLUS1-code.glyphs and renames the family to "M PLUS Code Latin" with a postCompile rename operation.
- The override was build-tested at 4bf6982. gftools builder built it; glyph set (740), cmap (716), glyf, gvar, name, OS/2, hhea, fvar, avar and STAT are byte-identical to the shipped font, and functional_gate.py passed (2,495,023 shaping runs, 0 differ). gftools-builder3 (e851b8b) built it but ignores postCompile, so its font keeps the source names (M PLUS 1 Code); it also drew uni2573 differently.
- A later upstream change was noted: MPLUS1-code.glyphs changed in four commits on 2026-09-23 and 2026-09-24 (programming ligatures). They are not in the shipped font and need separate review before any update.

## Final state

- METADATA.pb is unchanged; commit 4bf69824e45a175b9121b248c46abff103569051 is correct.
- config.yaml (override) builds a font functionally equivalent to the shipped one with gftools builder. The output file is named after the source, MPLUS1-code[wdth,wght].ttf.

## Previous upstream_info.md (2026-03)

### M PLUS Code Latin - Source Investigation

**Model**: Claude Opus 4.6

#### Source Repository
- **URL**: https://github.com/coz-m/MPLUS_FONTS
- **Commit**: N/A

#### Findings
The METADATA.pb contained a source block pointing to the coz-m/MPLUS_FONTS GitHub repository on the master branch, but no specific commit was recorded.

#### Status
- **Category**: MISSING_COMMIT

#### Commit Added (MEDIUM confidence)

Commit `a1268635894c5ee23dfdece570418ca07b66c3fc` was determined by **date_correlation**. Found the latest upstream commit before the binary modification date in google/fonts (2021-12-08). This assumes the upstream HEAD at onboarding time was the commit used.
