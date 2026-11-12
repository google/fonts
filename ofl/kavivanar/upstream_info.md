# Investigation: Kavivanar

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kavivanar |
| Slug | kavivanar |
| License Dir | ofl |
| Repository URL | https://github.com/enathu/kavivanar |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Kavivanar has no `source` block. The font was added on August 7, 2017 via commit `2af7a09e5` ("hotfix-kavivanar: v1.881 added (#977)").

The upstream repository was identified from DESCRIPTION.en_us.html added in that commit, which states: "To contribute, see github.com/enathu/kavivanar".

The upstream repository `enathu/kavivanar` is cached at `upstream_repos/fontc_crater_cache/enathu/kavivanar`. The repository contains:
- `source/Kavivanar-Regular.ufo` (UFO format)
- `source/sfd/` (FontForge SFD files)

The UFO source is a gftools-builder compatible format. However, no `config.yaml` exists in the repository.

The git log shows one commit: `689a10b` ("Added enhancements v1.89").

## Conclusion

The upstream repository URL has been identified as `https://github.com/enathu/kavivanar`. A source block needs to be added to METADATA.pb. The repository contains a UFO source but no `config.yaml`. An override `config.yaml` could be created in the google/fonts directory, or the commit hash needs to be verified.
