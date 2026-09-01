# Investigation Report: Linden Hill

**Family Name**: Linden Hill
**Slug**: lindenhill
**Designer**: Barry Schwartz
**License**: OFL
**Date Added**: 2011-10-19
**Model**: Claude Opus 4.6

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/theleagueof/linden-hill"
}
```

The source block was added in commit `658d6674d` ("Update upstreams", 2024-03-04) by Simon Cozens as part of PR #7343 ("Update more upstreams (1/2)"). The block contains a `repository_url` but no `commit` hash and no `config_yaml` path.

## Upstream Repository

- **URL**: https://github.com/theleagueof/linden-hill (verified accessible, HTTP 200)
- **Owner**: theleagueof (The League of Moveable Type)
- **Default branch**: master
- **Total commits**: 1
- **Only commit**: `a3f7ae6c4cac1b7e5ce5269e1fcc6a2fbb9e31ee` ("Initial commit with readme and licenses", 2011-05-25, by micah rich)
- **Tags**: none
- **Open PRs**: 4 (none merged) -- #1 (CSS font-face, closed), #2 (Unicode ligatures, closed), #3 (CSS font-face, open since 2015), #5 (woff2, open since 2024)

The repository was created on GitHub on 2011-05-25. It contains a single commit with the full font package including source UFOs, compiled OTF files, webfont files, and license/readme.

## Source Files in Upstream

The upstream repo contains the following source-relevant files at commit `a3f7ae6`:

- `source/Linden Hill.ufo/` -- Regular UFO source (fontinfo.plist reports creation date 2011/05/25)
- `source/Linden Hill Italic.ufo/` -- Italic UFO source
- `Linden Hill.otf` (120,992 bytes) -- Compiled OTF, regular
- `Linden Hill Italic.otf` (86,760 bytes) -- Compiled OTF, italic
- `webfonts/LindenHill-webfont.ttf` (37,476 bytes) -- Webfont TTF, regular
- `webfonts/LindenHill-Italic-webfont.ttf` (41,368 bytes) -- Webfont TTF, italic

Both `features.fea` files in the UFOs are empty (0 bytes). The UFO sources have standard structure with `fontinfo.plist`, `glyphs/`, `groups.plist`, `kerning.plist`, `lib.plist`, and `metainfo.plist`.

No `config.yaml`, `.designspace`, or `.glyphs` files were found in the upstream repo.

## Font Binaries in google/fonts

- `LindenHill-Regular.ttf` (124,844 bytes)
- `LindenHill-Italic.ttf` (94,540 bytes)

Both files were added in the google/fonts initial commit (`90abd17b4`, 2015-03-07) and have never been updated since. The font binary metadata (extracted via `strings`) showed:

- **Regular**: "FontForge 2.0 : Linden Hill Regular : 28-10-2011", Version 1.202
- **Italic**: "FontForge 2.0 : Linden Hill Italic : 28-10-2011", Version 1.201

The fonts were built with FontForge on 2011-10-28, approximately 5 months after the only upstream commit (2011-05-25). The TTF files in google/fonts are significantly larger than the upstream webfont TTFs and do not correspond to them. The TTFs were likely generated from FontForge SFD sources (possibly from the Sortsmill Fonts project at bitbucket.org/sortsmill/sortsmill-fonts, as referenced in the DESCRIPTION.en_us.html) rather than from the UFO sources in the League of Moveable Type repo.

## Background: Sortsmill / League of Moveable Type Connection

Barry Schwartz (chemoelectric) created fonts under the "Sortsmill" umbrella. The DESCRIPTION.en_us.html references both:
- `bitbucket.org/sortsmill/sortsmill-fonts` (original source repository, now likely defunct)
- `theleagueofmoveabletype.com/linden-hill` (The League of Moveable Type distribution)

The League of Moveable Type repo (`theleagueof/linden-hill`) served as a distribution point with UFO exports, while the original development likely happened in FontForge SFD format in the Sortsmill project. The copyright in the OFL states "Copyright (c) 2011, Barry Schwartz (chemoelectric@chemoelectric.org)".

## Commit Hash Determination

Since the upstream repo has only a single commit (`a3f7ae6c4cac1b7e5ce5269e1fcc6a2fbb9e31ee`), and it predates both the font build date (2011-10-28) and the google/fonts addition (2015-03-07), this is the correct commit hash to reference. There are no other commits or merged PRs to consider.

## Config.yaml Assessment

The upstream repo has UFO sources compatible with gftools-builder but lacks a `config.yaml` file. An override `config.yaml` could be created in the google/fonts family directory referencing the two UFO sources:

- `source/Linden Hill.ufo`
- `source/Linden Hill Italic.ufo`

Since there is no `.designspace` file, a config.yaml would need to define the sources explicitly. However, building these single-master UFOs without a designspace is straightforward for gftools-builder.

## PR History in google/fonts

| PR | Title | Date | Relevance |
|----|-------|------|-----------|
| #7343 | Update more upstreams (1/2) | 2024-03-04 | Added source block with `repository_url` |
| #435 | Update URL of Sortsmill source repository in descriptions | 2017-02-08 | Updated description links |

## Summary

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/theleagueof/linden-hill |
| **Commit Hash** | `a3f7ae6c4cac1b7e5ce5269e1fcc6a2fbb9e31ee` |
| **Config.yaml** | Not present in upstream; override needed |
| **Source Type** | UFO |
| **Status** | missing_config |
| **Confidence** | HIGH |

The repository URL is confirmed correct. The commit hash is trivially determined (single commit). The main gap is the absence of a `config.yaml` in the upstream repo. An override config.yaml in the google/fonts family directory would be needed to make the sources buildable with gftools-builder. The UFO sources are the correct format for gftools-builder, though the original TTFs in google/fonts were built with FontForge from what were likely SFD sources in the now-defunct Sortsmill Bitbucket repository.
