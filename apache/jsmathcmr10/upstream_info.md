# Investigation: jsMath cmr10

## Summary

| Field | Value |
|-------|-------|
| Family Name | jsMath cmr10 |
| Slug | jsmath-cmr10 |
| License Dir | apache |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `apache/jsmathcmr10/` directory contains only `DESCRIPTION.en_us.html`, `jsMath-cmr10.ttf`, and `METADATA.pb`. There is no license text file.

The METADATA.pb has no `source { }` block.

The copyright reads: "Generated from MetaFont bitmap by mftrace 1.0.33, http://www.cs.uu.nl/~hanwen/mftrace/". The font is based on the Computer Modern Roman font (`cmr10`) — the primary upright roman font in Donald Knuth's Computer Modern family, used as the default text font in TeX/LaTeX documents. Generated from MetaFont (`.mf`) sources using the `mftrace` tool.

The jsMath cmr10 font provides the standard roman characters for the jsMath JavaScript math rendering package. It was `date_added: "2010-12-20"`.

The git history shows only metadata-only changes since the initial commit. No font file updates have been made.

No repository for this font exists in the local cache. The MetaFont (`.mf`) sources are part of the TeX/CTAN distribution, which is not a standard gftools-builder compatible source.

This is one of six related jsMath Computer Modern families (jsMath cmbx10, cmex10, cmmi10, cmr10, cmsy10, cmti10) all sharing the same MetaFont origin.

## Conclusion

No upstream git repository is known or likely to exist for this font. The font was generated from MetaFont sources with no standard gftools-builder compatible source. No config.yaml is possible. Same status as all other jsMath CM families.
