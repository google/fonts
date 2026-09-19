# Investigation: Iceberg

## Summary

| Field | Value |
|-------|-------|
| Family Name | Iceberg |
| Slug | iceberg |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/iceberg |
| Commit Hash | db1c024077a00f9999b5f6437a70c19ced5c1fc5 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/iceberg"
  commit: "db1c024077a00f9999b5f6437a70c19ced5c1fc5"
}
```

## Investigation

The METADATA.pb at `ofl/iceberg/METADATA.pb` already contains a complete source block with both a repository URL and a commit hash. The font was added to google/fonts in the initial commit (90abd17b4f97671435798b6147b698aa9087612f, dated 2015-03-07) by Dave Crossland. No PR number is associated with this initial onboarding.

The referenced repository `https://github.com/librefonts/iceberg` is available in the upstream cache at `upstream_repos/fontc_crater_cache/librefonts/iceberg`. The remote URL confirms this is `https://github.com/librefonts/iceberg`.

Commit `db1c024077a00f9999b5f6437a70c19ced5c1fc5` exists in the cached repo with the message "update .travis.yml" (dated 2014-10-17). It is the only commit in the repository and includes the full font source: TTX disassembled files and the binary source files `src/Iceberg-Regular-OTF.vfb` and `src/Iceberg-Regular-TTF.vfb` (FontLab VFB format).

There is no `config.yaml` in the upstream repository. However, an override `config.yaml` exists in `ofl/iceberg/config.yaml` within google/fonts with the following content:

```yaml
buildVariable: false
sources:
  - src/Iceberg-Regular-TTF.vfb
  - src/Iceberg-Regular-OTF.vfb
```

This config references VFB source files that exist in the upstream repo at the referenced commit. The `cyrealtype/Iceberg` repository is a different, newer repository (with only 2 commits starting from 2016) and does not contain commit `db1c024`. The correct upstream is `librefonts/iceberg`.

## Conclusion

The source block in METADATA.pb is complete and correct. The repository URL points to `librefonts/iceberg`, the commit hash `db1c024` is verified to exist in the cached repo, and an override `config.yaml` is present in the google/fonts family directory. No action is needed.
