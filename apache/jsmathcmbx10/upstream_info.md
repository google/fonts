# Investigation: jsMath cmbx10

## Summary

| Field | Value |
|-------|-------|
| Family Name | jsMath cmbx10 |
| Slug | jsmath-cmbx10 |
| License Dir | apache |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `apache/jsmathcmbx10/` directory contains only `DESCRIPTION.en_us.html`, `jsMath-cmbx10.ttf`, and `METADATA.pb`. There is no license text file (no APACHE2.txt or similar).

The METADATA.pb has no `source { }` block.

The copyright in the font's METADATA.pb reads: "Generated from MetaFont bitmap by mftrace 1.0.33, http://www.cs.uu.nl/~hanwen/mftrace/". The font is NOT compiled from standard font sources (`.glyphs`, `.ufo`, `.designspace`) — it was generated from a MetaFont bitmap using the `mftrace` tool. MetaFont is the typesetting system used by TeX/LaTeX; the original sources are `.mf` files from the Computer Modern font family designed by Donald Knuth.

The jsMath package (http://www.math.union.edu/locate/jsMath/) was a JavaScript-based mathematics rendering system that used these fonts. The font was `date_added: "2010-12-20"` (one of the earliest Google Fonts additions).

The git history for `apache/jsmathcmbx10/` shows only metadata-only changes since the initial commit, going back through language cleanup commits and an "Initial commit" baseline. The fonts were added very early in the google/fonts repository history.

No jsMath repository was found in the cache at `upstream_repos/fontc_crater_cache/`. The jsMath project predates GitHub; the original fonts were distributed from the jsMath project website. The source is MetaFont (`.mf`) files from the TeX distribution (CTAN), which do not form a standard gftools-builder compatible source.

This family is one of six related jsMath Computer Modern families: jsMath cmbx10, jsMath cmex10, jsMath cmmi10, jsMath cmr10, jsMath cmsy10, jsMath cmti10. All six share the same origin.

## Conclusion

No upstream git repository is known or likely to exist for this font. The font was generated from MetaFont sources — not from standard gftools-builder compatible sources. No config.yaml is possible. This family, along with the other five jsMath CM variants, represents a special case of legacy fonts with no modern build pipeline.
