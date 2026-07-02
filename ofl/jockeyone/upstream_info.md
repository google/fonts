# Investigation: Jockey One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jockey One |
| Slug | jockey-one |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/jockeyone |
| Commit Hash | 71261c6f0c80fb7269df32e4aa396669a038030f |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `ofl/jockeyone/` directory in google/fonts contains `DESCRIPTION.en_us.html`, `JockeyOne-Regular.ttf`, `METADATA.pb`, and `OFL.txt`. The METADATA.pb has only basic metadata — no `source { }` block.

The git log shows the font has been in google/fonts since the initial commit (`90abd17b4`, 2015-03-07). No font file updates have been pushed since then.

The copyright reads: "Copyright (c) 2011, TypeTogether (www.type-together.com), with Reserved Font Names 'Jockey' and 'Jockey One'."

The tracking JSON (`data/gfonts_library_sources.json`) records the upstream repository as `https://github.com/librefonts/jockeyone` at commit `71261c6f0c80fb7269df32e4aa396669a038030f` (subject: "update .travis.yml"). This is the librefonts GitHub organization's mirror repository. Notes indicate: "SFD-only sources (FontForge format), not gftools-builder compatible".

The upstream repository is cached at `upstream_repos/fontc_crater_cache/librefonts/jockeyone`. The local clone has only one commit (shallow clone). The repository contains:
- `JockeyOne-Regular.ttf` (binary font)
- `src/JockeyOne-Regular-TTF.sfd` (FontForge source, SFD format)
- `src/JockeyOne-Regular.vfb` (FontLab Studio source)
- TTX decompositions of the fonts

The source format is `.sfd` (FontForge) and `.vfb` (FontLab Studio), which are NOT compatible with gftools-builder. No `.glyphs`, `.ufo`, or `.designspace` files exist.

## Conclusion

The upstream repository is `https://github.com/librefonts/jockeyone` at commit `71261c6f0c80fb7269df32e4aa396669a038030f`. However, the only sources available are `.sfd` (FontForge) and `.vfb` (FontLab Studio) files, which are not gftools-builder compatible. No config.yaml is possible with these sources. A source block needs to be added to METADATA.pb but the status will remain `missing_config` until buildable sources become available.
