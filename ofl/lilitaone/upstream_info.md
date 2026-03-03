# Investigation Report: Lilita One

**Family Name**: Lilita One
**Directory**: `ofl/lilitaone`
**Designer**: Juan Montoreano
**Date Added**: 2012-01-11
**License**: OFL
**Model**: Claude Opus 4.6

---

## METADATA.pb Analysis

The current METADATA.pb at `ofl/lilitaone/METADATA.pb` contained no `source { }` block. The file listed the family as a single-weight (Regular 400) display sans-serif font. The copyright attributed the font to Juan Montoreano (juan@remolacha.biz) with a 2011 date.

## Upstream Repository

**Repository URL**: https://github.com/librefonts/lilitaone
**Status**: Accessible (HTTP 200)
**Owner**: librefonts (archival organization)
**Default Branch**: master
**Created**: 2014-07-16 (over two years after the font was added to Google Fonts)
**Single Commit**: `d77736db8dc9d73e0c32093225a38a66e42400b8` (2014-10-17, by hash3g)

The repository was part of the `librefonts` organization, which was a batch archival effort by hash3g to preserve Google Fonts source files on GitHub. The repo was created on 2014-07-16 and received a single commit on 2014-10-17 with the message "update .travis.yml". This commit contained the entire initial content of the repository (41 files added, no prior history).

The repository was cached locally at `upstream_repos/fontc_crater_cache/librefonts/lilitaone/`. The cache was clean and up to date with the remote.

## Source Files

The upstream repository contained the following source files in the `src/` directory:

- `LilitaOne-Regular-TTF.sfd` -- Spline Font Database (FontForge format)
- `LilitaOne-Regular-OTF.vfb` -- FontLab VFB binary
- `LilitaOne-Regular.vfb` -- FontLab VFB binary

These are legacy font source formats. There were no `.glyphs`, `.ufo`, or `.designspace` files anywhere in the repository. The SFD file header showed it was originally created in FontForge with a modification timestamp from January 2012, consistent with the font's onboarding date.

The repository also contained TTX (FontTools XML) decompositions of both the TTF and OTF font files at the root level and in `src/`.

## Build Configuration

No `config.yaml` or `config.yml` file existed in the upstream repository. No override `config.yaml` existed in the `ofl/lilitaone/` directory of google/fonts either.

Since the source files were exclusively in SFD and VFB formats, these were not compatible with gftools-builder (which requires `.glyphs`, `.ufo`, or `.designspace` sources). Creating an override `config.yaml` was not feasible without first converting the sources to a supported format.

## Commit Hash Verification

The single commit `d77736db8dc9d73e0c32093225a38a66e42400b8` was the only commit in the repository and represented the archival import. Since the font was added to Google Fonts in January 2012 and the librefonts repo was created in July 2014, this repository was clearly not the original source used for onboarding -- it was a post-hoc archive.

The font binary in google/fonts (`LilitaOne-Regular.ttf`, MD5: `0d4e1383accd17a50bcc7d69f5ac7582`, 28092 bytes) had never been modified since the initial commit `90abd17b4` (2015-03-07, the bulk import of the entire google/fonts repository). No subsequent commits modified the font binary; only metadata files (METADATA.pb/METADATA.json) were updated over the years.

## Google Fonts Repository History

The git history for `ofl/lilitaone/` showed only metadata-related changes:

1. `90abd17b4` (2015-03-07) -- Initial commit (bulk import of all fonts)
2. `480630de3` (2015-12-08) -- METADATA.pb textproto update
3. `27f377ab0` (2016-01-11) -- Copyright field update
4. `883939708` (2016-01-11) -- Remove METADATA.json files
5. `633ebadbf` (2021-12-12) -- Add language support metadata
6. Various rollback/redo commits for language metadata (2022)
7. `ea42b7c32` (2023-08-14) -- Stroke and classifications metadata

None of these commits modified the font binary itself.

## Designer Information

The designer was Juan Montoreano, contactable at juan@remolacha.biz (website: http://www.remolacha.biz). The copyright year was 2011, predating the Google Fonts addition date of 2012-01-11. No personal GitHub account or alternative upstream repository was identified for the designer.

## Conclusion

**Repository URL**: `https://github.com/librefonts/lilitaone`
**Commit**: `d77736db8dc9d73e0c32093225a38a66e42400b8` (the only commit; archival import)
**Config**: None (SFD-only sources, not gftools-builder compatible)
**Status**: `missing_config` -- The upstream repo had only legacy SFD/VFB sources. No gftools-builder compatible sources existed, making it impossible to create a config.yaml without source conversion.
**Confidence**: HIGH -- The repository URL was confirmed accessible, the commit hash was the sole commit, and the source format limitation was clearly verified.

The librefonts/lilitaone repository served as an archival mirror rather than an active development repository. The original sources predated the Google Fonts onboarding and were created in FontForge/FontLab. To make this font fully rebuildable via gftools-builder, the SFD/VFB sources would need to be converted to a supported format (UFO or Glyphs) first.
