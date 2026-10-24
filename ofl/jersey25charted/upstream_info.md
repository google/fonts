# Investigation: Jersey 25 Charted

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jersey 25 Charted |
| Slug | jersey-25-charted |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jersey |
| Commit Hash | afc20d521110d3ba6d6614d226896c74d62f8f2f |
| Config YAML | sources/config-jersey25charted.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jersey"
  commit: "afc20d521110d3ba6d6614d226896c74d62f8f2f"
  config_yaml: "sources/config-jersey25charted.yaml"
  files {
    source_file: "fonts/ttf/Jersey25Charted-Regular.ttf"
    dest_file: "Jersey25Charted-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path. Note that this family uses a different commit hash (`afc20d521110d3ba6d6614d226896c74d62f8f2f`) from the other Jersey families which all share `d8446c4c9c2ba14cf408c295be35213c006e19ff`.

Git history in google/fonts shows a complex sequence for this font:
- `cba254412` — "Revert 'Jersey 25 Charted: Version 1.002'" (latest state — reverted back to 1.001)
- `b9a533293` — "Jersey 25 Charted: Version 1.002; ttfautohint (v1.8.4.7-5d5b) added" (reverted)
- `3d8f0dee3` — "Jersey 25 Charted: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added"
- `db5706d09` — "Revert 'Jersey 25 Charted: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added'"
- `1b92994da` — "[gftools-packager] Jersey 25 Charted: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (initial onboarding)

The revert of Version 1.002 is significant. The commit message for `3d8f0dee3` (Version 1.001) explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jersey at commit https://github.com/scfried/soft-type-jersey/commit/afc20d521110d3ba6d6614d226896c74d62f8f2f."

The revert commit `cba254412` changed the METADATA.pb commit from `d8446c4c9c2ba14cf408c295be35213c006e19ff` back to `afc20d521110d3ba6d6614d226896c74d62f8f2f`, confirming the current correct commit hash.

The upstream repository `scfried/soft-type-jersey` is cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jersey`. An alternate clone `soft-type-jersey_afc20d5211` also exists, which has `afc20d521110d3ba6d6614d226896c74d62f8f2f` as its HEAD ("Merge pull request #5 from emmamarichal/main", dated 2024-04-10). The main clone only has the HEAD commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` (shallow clone), but the alternate clone confirms `afc20d5` predates `d8446c4`. The file `sources/config-jersey25charted.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate. Jersey 25 Charted correctly uses commit `afc20d521110d3ba6d6614d226896c74d62f8f2f` (which is an older commit than `d8446c4` used by the other Jersey families), reflecting the actual binary that was onboarded — confirmed by the revert history in google/fonts.
