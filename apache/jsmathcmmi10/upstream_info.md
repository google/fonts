# Investigation: jsMath cmmi10

## Summary

| Field | Value |
|-------|-------|
| Family Name | jsMath cmmi10 |
| Slug | jsmath-cmmi10 |
| License Dir | apache |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `apache/jsmathcmmi10/` directory contains only `DESCRIPTION.en_us.html`, `jsMath-cmmi10.ttf`, and `METADATA.pb`. There is no license text file.

The METADATA.pb has no `source { }` block.

The copyright reads: "Generated from MetaFont bitmap by mftrace 1.0.33, http://www.cs.uu.nl/~hanwen/mftrace/". The font is based on the Computer Modern math italic font (`cmmi10`), which provides math italic glyphs for TeX/LaTeX typesetting. The font was generated from MetaFont (`.mf`) sources using the `mftrace` tool.

The jsMath cmmi10 font provides math italic characters (letters used in mathematical equations) for the jsMath JavaScript math rendering package. It was `date_added: "2010-12-20"`.

The git history shows only metadata-only changes since the initial commit. No font file updates have been made.

No repository for this font exists in the local cache. The jsMath project and its fonts predate modern git hosting, and the MetaFont (`.mf`) sources are part of the TeX/CTAN distribution — not a standard gftools-builder compatible source.

This is one of six related jsMath Computer Modern families (jsMath cmbx10, cmex10, cmmi10, cmr10, cmsy10, cmti10) all sharing the same MetaFont origin.

## Conclusion

No upstream git repository is known or likely to exist for this font. The font was generated from MetaFont sources with no standard gftools-builder compatible source. No config.yaml is possible. Same status as all other jsMath CM families.
