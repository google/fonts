# Investigation: Jura

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jura |
| Slug | jura |
| License Dir | ofl |
| Repository URL | https://github.com/ossobuffo/jura |
| Commit Hash | f9df75d92c93324e74e5ec0df6d91c8ee4b84b5a |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/ossobuffo/jura"
  commit: "f9df75d92c93324e74e5ec0df6d91c8ee4b84b5a"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb for Jura has a complete source block with `repository_url`, `commit`, and `config_yaml`. The upstream repository is `https://github.com/ossobuffo/jura`, maintained by Daniel Johnson (ossobuffo).

The commit hash `f9df75d92c93324e74e5ec0df6d91c8ee4b84b5a` was added to google/fonts in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list") by Felipe Sanches on 2025-03-31. The commit was sourced from the fontc_crater targets list at commit `ee7a65d433882450efa1d8418ed746bf07c05642`.

The referenced commit `f9df75d` corresponds to "Merge pull request #12 from aaronbell/master" (dated 2021-08-26, "Update to UFR format"), which is also the same day that PR #3639 ("Jura v5.106 (stat fix)") was merged into google/fonts by Aaron Bell. This is the HEAD commit of the jura upstream repo — the repository appears to have been migrated to UFR (Unicode Font Repository) format and has only one commit in its current form.

Verification in the cached repository at `upstream_repos/fontc_crater_cache/ossobuffo/jura/`:
- The commit `f9df75d` exists and is the latest commit
- `sources/config.yaml` exists at this commit with content:
  ```yaml
  sources:
    - Jura.glyphs
  axisOrder:
    - wght
  familyName: Jura
  ```
- `sources/Jura.glyphs` is present as the source file

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml` in the upstream repo.

## Conclusion

Jura is in a complete state. The METADATA.pb has `repository_url`, `commit`, and `config_yaml` all correctly set. The commit hash matches the upstream onboarding commit. The `sources/config.yaml` exists at the referenced commit. No action needed.
