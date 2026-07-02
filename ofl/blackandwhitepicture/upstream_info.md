# Investigation: Black And White Picture

## Summary

| Field | Value |
|-------|-------|
| Family Name | Black And White Picture |
| Slug | black-and-white-picture |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb has no source block at all — no repository URL, no commit hash, no config_yaml.

The font was added to google/fonts in commit `16680f868` (March 13, 2018, PR #1459, "korean families r01: added"). This was a bulk addition of multiple Korean font families with no upstream reference information included.

The copyright string in METADATA.pb reads: "Copyright (c) 1992-2018 AsiaSoft Inc. Seoul Korea All Rights Reserved." This indicates the font was created by AsiaSoft Inc., a commercial Korean type foundry. No GitHub or publicly accessible source repository was found — a search of the upstream repos cache at `upstream_repos/fontc_crater_cache/` found no AsiaSoft-related repositories.

The google/fonts family directory (`ofl/blackandwhitepicture/`) contains only the TTF binary, DESCRIPTION, METADATA.pb, and OFL.txt — no upstream.yaml, no source references of any kind.

Given that this is a commercial Korean foundry font from 1992-2018, it is likely that the source files (if any exist in a form usable for rebuilding) are proprietary to AsiaSoft Inc. No public upstream repository has been identified.

## Conclusion

No upstream source information is available. The font comes from AsiaSoft Inc., a commercial Korean type foundry, and no public repository has been found. This family likely cannot have a source block added without direct contact with AsiaSoft Inc. Status is `missing_url` with LOW confidence that a public upstream repo exists.
