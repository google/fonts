# Investigation: jsMath cmex10

## Summary

| Field | Value |
|-------|-------|
| Family Name | jsMath cmex10 |
| Slug | jsmath-cmex10 |
| License Dir | apache |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `apache/jsmathcmex10/` directory contains only `DESCRIPTION.en_us.html`, `jsMath-cmex10.ttf`, and `METADATA.pb`. There is no license text file.

The METADATA.pb has no `source { }` block.

The copyright in the font's METADATA.pb reads: "Generated from MetaFont bitmap by mftrace 1.0.33, http://www.cs.uu.nl/~hanwen/mftrace/". The font is NOT compiled from standard font sources — it was generated from MetaFont using `mftrace`. The font is based on the Computer Modern extension font (`cmex10`) from Donald Knuth's Computer Modern family, used in TeX/LaTeX mathematics typesetting.

The jsMath cmex10 font provides mathematical extension symbols (large brackets, summation signs, etc.) for the jsMath JavaScript package. It was `date_added: "2010-12-20"`.

The git history shows only metadata-only changes (language, classification updates) since the initial commit. No font file updates have been made.

No repository for this font was found in the cache at `upstream_repos/fontc_crater_cache/`. The jsMath project predates modern git hosting, and the original font was distributed from the jsMath website. The `.mf` source files are part of the TeX/CTAN distribution.

This is one of six related jsMath Computer Modern families sharing the same origin (jsMath cmbx10, cmex10, cmmi10, cmr10, cmsy10, cmti10).

## Conclusion

No upstream git repository is known or likely to exist for this font. The font was generated from MetaFont sources and has no standard gftools-builder compatible source. No config.yaml is possible. Same status as all other jsMath CM families.
