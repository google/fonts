# Investigation: Bitcount Prop Double

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Prop Double |
| Slug | bitcount-prop-double |
| License Dir | ofl |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit Hash | af0818eaeb3b0839806ea19134fc18f317cdcf5a |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "af0818eaeb3b0839806ea19134fc18f317cdcf5a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf"
    dest_file: "BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

Bitcount Prop Double is part of the initial batch of non-Ink Bitcount families added in January 2025. All non-Ink families were added in commit `bb009d354` ("Bitcount Grid Double: Version 1.0 added") which confirms the upstream commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a`. This matches the METADATA.pb.

Commit `af0818eaeb3b` is confirmed in the upstream repo cache at `upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount`, dated January 13, 2025.

The upstream `sources/config.yaml` only contains `familyName: Bitcount`. An override `config.yaml` is present in the google/fonts family directory (`ofl/bitcountpropdouble/config.yaml`):
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Prop Double
buildVariable: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb source block is complete. The commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a` is confirmed as the onboarding commit. An override `config.yaml` is present in the google/fonts family directory. No action needed.
