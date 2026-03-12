# Oxygen Mono — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Oxygen Mono is the monospace companion to the Oxygen font family, designed by Vernon Adams (GitHub: vernnobile). It was added to Google Fonts on 2012-09-08 and shares its upstream repository with Oxygen.

## Designer

Vernon Adams (vern@newtypography.co.uk) maintains the canonical upstream at https://github.com/vernnobile/oxygenFont. See the Oxygen investigation for full designer details.

## Canonical Upstream Repository

The canonical upstream repository is **vernnobile/oxygenFont**: https://github.com/vernnobile/oxygenFont

The `Oxygen-Monospace/src/` directory contains:
- `OxygenMono-Regular.ufo/` — UFO source directory (confirmed: contains `features.fea`, `fontinfo.plist`, `glyphs/`, `lib.plist`, `metainfo.plist`)
- `OxygenMono-Regular.sfd` — FontForge SFD source file
- `OxygenMono-Regular-unhinted.ttf` — unhinted TTF build artifact

The presence of the UFO source confirms this is a canonical, buildable open-source repository.

Latest commit: `62db0ebe3488c936406685485071a54e3d18473b`

## METADATA.pb Update

A source block was added to METADATA.pb pointing to the canonical upstream repository with the latest commit hash.

## References

- Canonical upstream: https://github.com/vernnobile/oxygenFont
- Designer GitHub profile: https://github.com/vernnobile
- Google Fonts: https://fonts.google.com/specimen/Oxygen+Mono
