# Investigation: Judson

## Summary

| Field | Value |
|-------|-------|
| Family Name | Judson |
| Slug | judson |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/judson |
| Commit Hash | a80a2aecb86b334586bc8b956ddf8b1bf61e144b |
| Config YAML | none (SFD-only sources) |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Judson has no source block. The font was added to google/fonts in the initial commit `90abd17b4` ("Initial commit") alongside hundreds of other families.

The copyright in the font reads: "Copyright (c) 2010, 2011 by Daniel Johnson (il.basso.buffo@gmail.com)". The FONTLOG.txt confirms the same designer email and mentions the project was originally hosted at `http://io.debian.net/~danielj/`. Importantly, this is the same Daniel Johnson who maintains the Jura font family (GitHub: `ossobuffo`) — the Jura METADATA.pb includes `repository_url: "https://github.com/ossobuffo/jura"` and the email `il.basso.buffo@gmail.com` matches Jura's copyright.

A `librefonts` mirror of Judson exists in the cache at `upstream_repos/fontc_crater_cache/librefonts/judson/`. The `librefonts` project is a preservation initiative that stores decomposed TTX files of font binaries, as well as the original source files when available. At commit `a80a2aecb86b334586bc8b956ddf8b1bf61e144b` ("update .travis.yml"), the repository contains:
- `Judson-Bold-TTF.sfd`, `Judson-Italic-TTF.sfd`, `Judson-Regular-TTF.sfd` — FontForge SFD source files
- `Judson-Bold.vfb`, `Judson-Italic.vfb`, `Judson-Regular.vfb` — FontLab VFB source files
- TTX decompiled font files

The commit `a80a2aecb86b334586bc8b956ddf8b1bf61e144b` was verified to exist in the librefonts/judson repo. However, the `librefonts` repository is not the canonical upstream — it is a mirror. The canonical upstream is likely the same Daniel Johnson who maintains Jura (GitHub: ossobuffo), but no `judson` repository exists under `ossobuffo`. The original sources were at `http://io.debian.net/~danielj/`.

The FONTLOG.txt mentions FontForge `.sfd` files as the source format, and the librefonts mirror confirms SFD files are present. SFD format is not directly compatible with gftools-builder, and no override `config.yaml` exists in the google/fonts Judson directory.

## Conclusion

Judson has a librefonts mirror at `https://github.com/librefonts/judson` with commit `a80a2aecb86b334586bc8b956ddf8b1bf61e144b`. The sources are FontForge SFD files and FontLab VFB files, which are not compatible with gftools-builder. No `config.yaml` can be created for this family without first converting sources to a gftools-builder compatible format (.glyphs, .ufo, .designspace). The METADATA.pb needs a source block at minimum, but no config is possible with current sources. Status: no_config_possible.
