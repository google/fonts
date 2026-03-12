# Parisienne — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream GitHub repository was found for Parisienne. The FONTLOG.txt confirmed that source files exist as VFB (FontLab) files, and the designer Brian J. Bonislawsky (Astigmatic) was contacted via astigmatic.com. No public GitHub repository for this font was found under the Astigmatic organization, googlefonts organization, or any other public location. The font was created in 2012 and the source distribution has remained VFB-only.

## Investigation

The METADATA.pb listed the designer as Astigmatic with copyright held by Brian J. Bonislawsky DBA Astigmatic (AOETI), dated 2012.

The FONTLOG.txt described three VFB source files:
1. `Parisienne-Regular-OTF.vfb` — merged contours and optimized for OTF
2. `Parisienne-Regular-TTF.vfb` — TrueType outlines with hinting adjustments
3. `Parisienne-Regular.vfb` — original source files with contour overlaps

Web searches were conducted for a GitHub repository under Astigmatic, googlefonts/ParisienneFont, and related variations. The only Astigmatic-attributed font found on GitHub under googlefonts was `googlefonts/SacramentoFont`. No dedicated Parisienne repository was found.

The DESCRIPTION.en_us.html contained no upstream repository link.

## Conclusion

No canonical upstream repository was found. Sources are VFB-only with no public hosting. No METADATA.pb changes were made.
