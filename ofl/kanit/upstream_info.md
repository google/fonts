# Investigation: Kanit

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kanit |
| Slug | kanit |
| License Dir | ofl |
| Repository URL | https://github.com/cadsondemak/kanit |
| Commit Hash | 467dfe842185681d8042cd608b8291199dd37cda |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cadsondemak/kanit"
  commit: "467dfe842185681d8042cd608b8291199dd37cda"
}
primary_script: "Thai"
```

## Investigation

The METADATA.pb contains both `repository_url` and `commit`. The upstream repository is at `cadsondemak/kanit` in the cache at `upstream_repos/fontc_crater_cache/cadsondemak/kanit`.

The repository contains Glyphs source files in `sources/`:
- `sources/Kanit_Upright_Master.glyphs`
- `sources/Kanit_Italic_Master.glyphs`

No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/kanit/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - sources/Kanit_Upright_Master.glyphs
  - sources/Kanit_Italic_Master.glyphs
```

The upstream repo's latest commit is `467dfe8` ("Merge pull request #16 from RosaWagner/master"), which matches the commit hash in METADATA.pb exactly.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.
