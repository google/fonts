# PT Serif — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ptserif/src/`

## Source Files

The `ptserif/src/` directory contains compiled binaries and web font formats, but no editable design sources.

- **TTF** (compiled binaries, not design sources): PTF55F.ttf, PTF56F.ttf, PTF75F.ttf, PTF76F.ttf, PTZ55F.ttf, PTZ56F.ttf
- **Web fonts** (compiled formats): PTF55F_W.eot, PTF55F_W.svg, PTF55F_W.woff, PTF56F_W.eot, PTF56F_W.svg, PTF56F_W.woff, PTF75F_W.eot, PTF75F_W.svg, PTF75F_W.woff, PTF76F_W.eot, PTF76F_W.svg, PTF76F_W.woff, PTZ55F_W.eot, PTZ55F_W.svg, PTZ55F_W.woff, PTZ56F_W.eot, PTZ56F_W.svg, PTZ56F_W.woff
- **Other**: demo.html, stylesheet.css

## Buildability

No design source files are available in this directory. The font cannot be rebuilt from the files present here.

## Designer

ParaType (yakupov@paratype.com). Copyright 2010 ParaType Ltd.

## Investigation Details

- **Checked cache**: the upstream repo cache — no cached entry.
- **GitHub organization**: The `paratype` GitHub organization exists but contains only two unrelated repositories — no font source repositories.
- **GitHub search**: Searches for "PT Serif paratype OFL", "ptserif font", and "PT fonts paratype" returned no canonical designer-owned repository.
- **Third-party mirrors**: No packaging mirrors were found for PT Serif specifically, unlike PT Sans.
- **paratype.com**: No source repository link was found.

## Notes

PT Serif is the serif companion to PT Sans, part of the PT (Public Type) family commissioned by the Federal Agency on Press and Mass Communications of the Russian Federation. Designed by Alexandra Korolkova under Paratype leadership, released in 2010. It covers Latin and Cyrillic scripts with Regular, Bold, Italic, and Bold Italic variants plus PT Serif Caption.
