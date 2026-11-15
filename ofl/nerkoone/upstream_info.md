# Nerko One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/nermink99/Nerko
- **Owner**: nermink99 (Nermin Kahrimanovic)
- **Default branch**: master
- **License**: OFL-1.1
- **Last pushed**: 2020-11-09
- **Pinned commit**: `62c2998197eaa09664ca1e0605fa4cfd273ac8bf` (2020-11-06) — "Merge pull request #8 from yanone/master — Additional changes for Google Fonts"

The repo is not cached locally at `/mnt/shared/upstream_repos/fontc_crater_cache/`.

## Source Files

Sources are located in the `src/` directory:

- `src/NerkoOne-Regular.ufo` — primary UFO source (standard UFO3 layout: `features.fea`, `fontinfo.plist`, `glyphs/`, `groups.plist`, `kerning.plist`, `layercontents.plist`, `lib.plist`, `metainfo.plist`)
- `src/NerkoOne-Regular.sfd` — FontForge SFD source (legacy; also present)
- `src/build.sh` — shell-based build script using `fontmake` + `gftools`
- `src/original_drawings/` — archival artwork

Output fonts:
- `fonts/ttf/NerkoOne-Regular.ttf` — static TTF (what Google Fonts uses)
- `fonts/otf/` — OTF versions

## Build System

The repo uses a **shell script** (`src/build.sh`) rather than gftools builder or a Makefile. The script calls `fontmake -u NerkoOne-Regular.ufo -o ttf` and then post-processes with `gftools fix-dsig` and `gftools fix-nonhinting`. Requirements are loosely pinned via `requirements.txt`:

```
fontmake
git+https://github.com/googlefonts/fontbakery
git+https://github.com/googlefonts/gftools
```

CI was previously handled via Travis CI (`.travis.yml` present), which is now defunct. No GitHub Actions workflow is present.

## config.yaml Status

There is **no `config.yaml` in the upstream repo** (`nermink99/Nerko`). The build is driven by `src/build.sh`, not by gftools builder. However, an override `config.yaml` is present in google/fonts at `ofl/nerkoone/config.yaml`, with content:

```yaml
sources:
  - src/NerkoOne-Regular.ufo
familyName: "Nerko One"
buildVariable: false
```

This config.yaml was added on the Google Fonts side. It names the UFO that `src/build.sh` builds.

The `METADATA.pb` does **not** include a `config_yaml` field, which is consistent with the absence of a config in the upstream repo. The `source.files` block directly maps `fonts/ttf/NerkoOne-Regular.ttf` → `NerkoOne-Regular.ttf`.

## Notes

- This is a static (non-variable) handwriting font with a single Regular weight; no variable font is planned.
- The designer is Nermin Kahrimanovic; Kai Bernau (yanone) contributed the Google Fonts preparation work via PR #8.
- The repository has been inactive since November 2020. The pinned commit is effectively the HEAD of master at onboarding time.
- Subsets: latin, latin-ext (no Vietnamese subset — consistent with the limited character coverage of this handwriting font).
- The METADATA.pb `source.files` block also copies `DESCRIPTION.en_us.html` and `FONTLOG.txt`, both of which exist in the upstream repo root.
- The `config.yaml` present in the Google Fonts repo side is a local addition not tracked in the upstream; it should not be referenced in METADATA.pb unless a proper gftools builder config is added upstream.
- The Travis CI setup is now obsolete; migration to GitHub Actions would be recommended if the upstream is ever updated.
- The UFO source (`src/NerkoOne-Regular.ufo`) is what the shipped font was built from; the override `config.yaml` names it (see below).

## Override config corrected (2026-11-13)

**Model**: Claude Fable 5.2

The override listed `src/NerkoOne-Regular.sfd`, a FontForge file last changed in July 2019. The shipped `NerkoOne-Regular.ttf` is byte-identical to `fonts/ttf/NerkoOne-Regular.ttf` at the pinned commit, which `src/build.sh` builds from `src/NerkoOne-Regular.ufo` (last changed in November 2020). The override now names the UFO.

With gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1, the new config builds a font with the shipped codepoints and glyph count (440).
