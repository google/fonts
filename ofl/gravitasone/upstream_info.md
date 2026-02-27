# Investigation: Gravitas One

## Summary

Gravitas One is a display serif font by Riccardo De Franceschi (Sorkin Type Co), added to Google Fonts on 2011-06-29 as part of the initial commit. The upstream repository is `librefonts/gravitasone` on GitHub. The current METADATA.pb on the main branch has **no source block**. The upstream repo contains only SFD (FontForge) and VFB (FontLab) source files -- no `.glyphs`, `.ufo`, or `.designspace` sources, and no `config.yaml`. A gftools-builder config is not possible with SFD-only sources.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gravitas One                                                       |
| Designer          | Riccardo De Franceschi                                             |
| Repository URL    | https://github.com/librefonts/gravitasone                          |
| Commit Hash       | c89d142ad0f695ba267d27965c26d1dd75463f20                           |
| Config YAML       | None (SFD-only sources)                                            |
| Source Files      | src/GravitasOne-TTF.sfd, src/GravitasOne.vfb                      |
| Status            | **no_config_possible**                                             |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/gravitasone/METADATA.pb` (main branch) has **no source block**. It contains only basic metadata: name, designer, license, category, date_added, fonts, subsets, stroke, and classifications.

Note: A source block has been prepared in a pending branch (`sources_info_2026-02-25`) with repository_url and commit hash, but it has not yet been merged to main.

### Git History in google/fonts

The font was part of the initial commit of the google/fonts repository:
- Commit `90abd17b4` (2015-03-07) by Dave Crossland: "Initial commit"
- This was a bulk import; the font had been in Google Fonts since 2011-06-29

The font binary has never been updated since the initial commit -- there is only one commit touching `GravitasOne.ttf`.

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/librefonts/gravitasone/` has a single commit:
- `c89d142ad0f695ba267d27965c26d1dd75463f20` (2014-10-17) by hash3g: "update .travis.yml"

This is the initial (and only) commit in the librefonts repo. Repository contents:
- `src/GravitasOne-TTF.sfd` -- FontForge source file
- `src/GravitasOne.vfb` -- FontLab source file
- `src/VERSIONS.txt` -- states "GravitasOne.ttf: Version 1.001"
- `src/METADATA_comments.txt` -- metadata comments
- Various `.ttx` decomposition files of the font binary
- `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`
- `.travis.yml` -- CI configuration for fontbakery

The repo has **no config.yaml** and **no gftools-builder compatible sources** (.glyphs, .ufo, .designspace). The only source files are SFD (FontForge) and VFB (FontLab), which are not supported by gftools-builder.

### Commit Hash Verification

The librefonts repo has only one commit (`c89d142`), so this is the only possible reference commit. The font was already in Google Fonts before this repo was created (the repo was set up in 2014, the font was added to Google Fonts in 2011). The librefonts repo is an archive of the source files, not the original development location.

The DESCRIPTION.en_us.html references the original source at Google Code: "Source files are available from Google Code." This aligns with the pre-GitHub era origins of many early Google Fonts.

## Conclusion

The upstream repository exists but only contains SFD/VFB sources that are not compatible with gftools-builder. No config.yaml is possible with these source formats.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/librefonts/gravitasone"
  commit: "c89d142ad0f695ba267d27965c26d1dd75463f20"
}
```

**Status: no_config_possible** -- The upstream repo has only SFD/VFB sources, which are not supported by gftools-builder. A config.yaml cannot be created.
