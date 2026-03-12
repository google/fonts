# Meiescript — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/librefonts/meiescript
- **Owner**: librefonts (Mikhail Kashkin / hash3g — not the original designers)
- **Default branch**: master
- **Last pushed**: 2014-10-17
- **Latest relevant commit**: `5b8265c5fea4aedc3d90da6e6b2e5bc47fb2bb22` — "update .travis.yml" (2014-10-17)
- **Commit that added font files**: `1689c5fd5600097e726a3bbcc857b4d1f034a8c1` — "Move meiescript font files to separate repository" (2014-07-16)

This repository was created by Mikhail Kashkin (GitHub: hash3g) as part of the `librefonts` organization, which appears to be a Google Fonts infrastructure effort to host font sources. The original designers are Johan Kallas (johankallas) and Mihkel Virkus (mihkelvirkus), both based in Tallinn, Estonia. Neither designer has public GitHub repositories of their own.

The font was added to Google Fonts on 2012-08-21, and the librefonts repo was created in 2014-07-16. The repository has 12 commits total, all from 2014, and has been inactive since October 2014.

## Source Files

The repository contains two distinct source formats:

**In the root directory (TTF sources, TTX format):**
- `MeieScript-Regular.ttf.ttx` — master TTX file for the TTF
- Individual per-table TTX files: `*.F_F_T_M_.ttx`, `*.GlyphOrder.ttx`, `*.O_S_2f_2.ttx`, `*._c_m_a_p.ttx`, `*._c_v_t.ttx`, `*._f_p_g_m.ttx`, `*._g_a_s_p.ttx`, `*._g_l_y_f.ttx`, `*._h_e_a_d.ttx`, `*._h_h_e_a.ttx`, `*._h_m_t_x.ttx`, `*._l_o_c_a.ttx`, `*._m_a_x_p.ttx`, `*._n_a_m_e.ttx`, `*._p_o_s_t.ttx`, `*._p_r_e_p.ttx`

**In `src/` directory (original design sources + OTF TTX):**
- `MeieScript-Regular-OTF.vfb` — original FontLab VFB source (OTF variant)
- `MeieScript-Regular-TTF.sfd` — FontForge SFD source (TTF variant)
- `MeieScript-Regular.otf.ttx` + per-table OTF TTX files
- `METADATA_comments.txt` — metadata notes
- `VERSIONS.txt` — version info (Version 1.001)

The VFB and SFD files are the original design masters. The TTX files are derived artifacts produced by decompiling the binaries.

## Build System

The repository uses the **fontbakery-build** pipeline (circa 2014) via Travis CI (`.travis.yml`). The build process:

1. Installs FontForge, ttfautohint, fontTools, fontcrunch, fontbakery-cli
2. Runs `fontbakery-build.py .` to rebuild the TTF from sources
3. Deploys build artifacts via `fontbakery-travis-deploy.py`

This is a legacy build system from the early Google Fonts era and is not compatible with current tooling (`gftools builder`, `fontmake`). No `Makefile`, `config.yaml`, or `sources/` directory with UFO sources is present. The build pipeline is entirely obsolete.

## config.yaml Status

**No `config.yaml` exists** in this repository or in the `google/fonts` working copy at `/mnt/shared/google/fonts/ofl/meiescript/`. The repository predates the current Google Fonts build infrastructure that uses `config.yaml` with `gftools builder`/`fontmake`.

## Notes

- **Font version**: 1.001 (unchanged since 2012 initial release)
- **No upstream activity since 2014**: The repository has been completely dormant. There are no issues, pull requests, or forks.
- **Designer contact**: Johan Kallas (`johan.kallas@gmail.com`), Mihkel Virkus (`mihkelvirkus@gmail.com`) — emails from FONTLOG.txt. The METADATA.pb uses slightly different addresses (`johankallas@gmail.com`, `mihkelvirkus@gmail.com`).
- **No UFO sources**: The original sources are in VFB (FontLab) and SFD (FontForge) formats. There are no UFO sources, which would be the preferred format for modern tooling.
- **Redesign/modernization needed**: To bring this font up to current Google Fonts standards, the VFB/SFD sources would need to be converted to UFO, a `config.yaml` created, and the font rebuilt with `fontmake`. This would require either designer involvement or significant reverse engineering.
- **librefonts org**: The `librefonts` GitHub organization (https://github.com/librefonts) was used in 2014 to migrate several early Google Fonts to hosted repositories. It is not an official Google organization.
- **Confidence in upstream identification**: High — the repository explicitly describes itself as the Meie Script font by the same designers, with matching copyright, license, and version.
