# Codystar - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Codystar |
| Designer | Neapolitan (Font Diner) |
| Repository URL | https://github.com/librefonts/codystar |
| Commit Hash | e32d050fbb01232b6a85423b121da89f21bba8b3 |
| Branch | master (default) |
| Config YAML | N/A (override config.yaml in google/fonts) |
| Override Config | Yes |
| Status | complete |

## How URL Was Found

The repository URL `https://github.com/librefonts/codystar` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") on January 14, 2024. The librefonts organization on GitHub hosts many font families that were originally contributed to Google Fonts.

## How Commit Was Determined

The commit `e32d050fbb01232b6a85423b121da89f21bba8b3` (dated July 16, 2014) is the initial commit in the repository with message "Move codystar font files to separate repository". This is the oldest and most foundational commit. Subsequent commits (9 more, up to October 2014) only add CI/Travis configuration and do not modify the font source files.

The commit was recorded in the METADATA.pb source block (commit `a76a3a1b3`, "sources info for Codystar", by Felipe Sanches on November 21, 2025). The original google/fonts commit referenced was `90abd17b4` (Initial commit).

## Config YAML Status

**Override config.yaml exists** in google/fonts at `ofl/codystar/config.yaml`:

```yaml
buildVariable: false
sources:
  - src/Codystar-Regular-TTF.vfb
  - src/Codystar-Light-TTF.vfb
```

The upstream repository only contains `.vfb` (FontLab binary) source files in `src/`:
- `src/Codystar-Regular-TTF.vfb`
- `src/Codystar-Light-TTF.vfb`

No `.ufo`, `.glyphs`, or `.designspace` files exist. The override config.yaml correctly references the VFB sources.

## Verification

- **Repository accessible**: Yes, https://github.com/librefonts/codystar is accessible
- **Commit exists**: Yes, `e32d050f` is present (it is the initial commit)
- **Source block on main**: Yes, the full source block (repository_url + commit) is on main
- **Override config exists**: Yes, at `ofl/codystar/config.yaml`
- **Config references correct files**: Yes, the VFB files referenced in config.yaml match the source files at the recorded commit

## Confidence Level

**High**. This is a straightforward case. The repository has minimal history (10 commits, all from 2014), the commit hash points to the initial commit which contains the actual font sources, and an override config.yaml is already in place.

## Open Questions

None. This family is complete.
