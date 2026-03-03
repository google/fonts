# Investigation: Bitcount Prop Single Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Prop Single Ink |
| Slug | bitcount-prop-single-ink |
| License Dir | ofl |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit Hash | 89e7994f73b7f5ced80e7cf493d40be9e66ff82f |
| Config YAML | sources/config.yaml (upstream, but inadequate — needs correction) |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "89e7994f73b7f5ced80e7cf493d40be9e66ff82f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountPropSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountPropSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL, commit hash, and `config_yaml: "sources/config.yaml"`.

The font was added via a series of commits. The initial version (`9cc1c52fc` or similar) used commit `af0818eaeb3b`. Commit `19cdcec59` (March 31, 2025, batch import from fontc_crater targets) updated the commit to `653fc48a72cf3b6a293f6fc207a770f537921889` and added `config_yaml: "sources/config.yaml"`. Commit `529068a1e` ("Bitcount Prop Single Ink: Version 1.001 added") then updated the commit to `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` — confirmed by the commit body: "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/89e7994f73b7f5ced80e7cf493d40be9e66ff82f."

The commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` is confirmed valid (September 5, 2025).

**Problem**: The `config_yaml: "sources/config.yaml"` refers to the upstream `sources/config.yaml`, which only contains `familyName: Bitcount` — an incomplete gftools-builder configuration. Unlike the other Bitcount Ink families (Grid Double Ink, Grid Single Ink, Ink, Prop Double Ink), there is no local override `config.yaml` in the `ofl/bitcountpropsingleink/` directory within google/fonts.

This is inconsistent with all other Bitcount Ink families, which either have a local override `config.yaml` and no `config_yaml` in METADATA.pb, or vice versa. The current state likely causes build failures when attempting to rebuild from source.

The fix would be either:
1. Remove `config_yaml` from METADATA.pb and add a proper override `config.yaml` to the google/fonts family directory (consistent with other Bitcount Ink families), or
2. Fix the upstream `sources/config.yaml` to contain proper build instructions.

## Conclusion

The commit hash is correct. However, `config_yaml: "sources/config.yaml"` points to an inadequate upstream config that only sets `familyName: Bitcount`. This family needs correction: a proper override `config.yaml` should be added to the google/fonts directory, and the `config_yaml` field should be removed from METADATA.pb to match the pattern used by all other Bitcount Ink families.
