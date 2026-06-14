# Spicy Rice -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `spicyrice/src/`

## Source Files

The source directory contains: 3 VFB files (FontLab, proprietary format); 1 compiled binary (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `SpicyRice-Regular-OTF.vfb` (VFB, proprietary)
- `SpicyRice-Regular-TTF.vfb` (VFB, proprietary)
- `SpicyRice-Regular.vfb` (VFB, proprietary)
- `SpicyRice-Regular.otf` (compiled binary)

## Research

Spicy Rice was designed by Brian J. Bonislawsky for Astigmatic (AOETI)
(astigma@astigmatic.com) and released in 2011. Searches on GitHub for
Astigmatic-related repositories and for the Spicy Rice font source files
returned no relevant results. The Astigmatic GitHub organization did not
exist, and no personal GitHub account for Brian Bonislawsky was found with
font source repositories.


## Notes

The designer listed in METADATA.pb is Astigmatic. Spicy Rice is described as
a casual display font with festive flair. It supports Latin and Latin Extended
character sets and is licensed under the SIL Open Font License.
