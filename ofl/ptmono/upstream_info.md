# PT Mono — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream GitHub repository was found for PT Mono. ParaType does not maintain a public GitHub repository for the PT font families. No METADATA.pb changes were made.

## Designer

ParaType (yakupov@paratype.com). Copyright 2010 ParaType Inc., ParaType Ltd.

## Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry.
- **GitHub organization**: The `paratype` GitHub organization exists but contains only two unrelated repositories (`paratype/paratype.github.io` and `paratype/MauiLifecycleEvents`) — no font source repositories.
- **GitHub search**: Searches for "PT Mono paratype OFL", "ptsans ptserif ptmono paratype", "PT fonts cyrillic OFL" all returned no canonical designer-owned repository.
- **Third-party mirrors**: The `openela-main/paratype-pt-sans-fonts` repository was found but is a Linux packaging mirror (OpenELA), not a canonical designer repository.
- **paratype.com**: The ParaType website is an Angular application; no source repository link was found for the PT fonts.
- **googlefontdirectory-hg**: https://github.com/googlefonts/googlefontdirectory-hg at
  `52f780bc9d197280a9f430574e179a5f233c56b6` keeps a FontLab source for this family:
  `ofl/ptmono/src/PTM55FT.vfb`, beside the font as built (`ofl/ptmono/PTM55FT.ttf`).

## Context

PT Mono is part of the PT (Public Type) family, commissioned by the Federal Agency on Press and Mass Communications of the Russian Federation for use in state documents. The PT family includes PT Sans, PT Serif, PT Sans Caption, PT Sans Narrow, PT Serif Caption, and PT Mono. All were released under the OFL but ParaType does not appear to host sources on a public version control platform.

## Verdict

**No canonical upstream repository found**, but a legacy FontLab source exists in googlefontdirectory-hg (above). PT Mono is distributed by ParaType but no public source repository exists on GitHub or other platforms. No METADATA.pb changes were made.
