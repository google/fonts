# Investigation: Bitcount Prop Double Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Prop Double Ink |
| Slug | bitcount-prop-double-ink |
| License Dir | ofl |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit Hash | 89e7994f73b7f5ced80e7cf493d40be9e66ff82f |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
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
    source_file: "fonts/ttf/variable/BitcountPropDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountPropDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

Bitcount Prop Double Ink is part of the Ink variant family batch, all added from the same upstream commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f`. This is confirmed by checking the initial addition commits for other Ink families (e.g., `5d1b8f3e6` for Bitcount Grid Double Ink and `c020967df` for Bitcount Ink), all of which reference the same upstream commit hash.

Commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` is confirmed in the upstream repo cache at `upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount`, dated September 5, 2025.

The upstream `sources/config.yaml` only contains `familyName: Bitcount`. An override `config.yaml` is present in the google/fonts family directory (`ofl/bitcountpropdoubleink/config.yaml`):
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Prop Double Ink
buildVariable: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb source block is complete. The commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` is confirmed as the onboarding commit. An override `config.yaml` is present in the google/fonts family directory. No action needed.
