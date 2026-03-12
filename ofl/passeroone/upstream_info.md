# Passero One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream GitHub repository was found for Passero One. The FONTLOG.txt confirmed that the font was mastered from FontLab VFB (VBF) format, and the DESCRIPTION.en_us.html referenced the now-defunct Google Code project hosting (code.google.com/p/googlefontdirectory/) as the source location. The SorkinType GitHub organization does not contain a Passero One repository.

## Investigation

The METADATA.pb listed the designer as Viktoriya Grabowska with copyright held by Sorkin Type Co, dated 2011.

The FONTLOG.txt described the font history:
- Original design by Viktoriya Grabowska in FontLab VBF format
- Mastered and spaced by Eben Sorkin (Sorkin Type Co)
- The source format was FontLab VFB

The DESCRIPTION.en_us.html pointed to `code.google.com/p/googlefontdirectory/` as the source location, which is the old Google Code project hosting that has since been shut down and is only available as an archive.

A web search was conducted for SorkinType's GitHub organization repositories. Sorkin Type has 67+ repositories on GitHub, but none named PasseroOne, Passero, or Passero-One were found in the results.

The google/fonts FONTLOG indicates this font was contributed in August–December 2011, predating GitHub becoming the standard for font source hosting.

## Conclusion

No canonical upstream GitHub repository was found. Sources are VFB-only, originally hosted on Google Code (now defunct). No METADATA.pb changes were made.
