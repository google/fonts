# Investigation: League Gothic

## Summary

| Field | Value |
|-------|-------|
| Family Name | League Gothic |
| Slug | league-gothic |
| License Dir | ofl |
| Repository URL | https://github.com/sursly/league-gothic |
| Commit Hash | f1d4a1c8c1db3c4a32cc13763c5fbb1776b5d478 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/sursly/league-gothic"
  commit: "f1d4a1c8c1db3c4a32cc13763c5fbb1776b5d478"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/LeagueGothic[wdth].ttf"
    dest_file: "LeagueGothic[wdth].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb has `repository_url`, `commit` hash, and `config_yaml` all populated. The commit `f1d4a1c8c1db3c4a32cc13763c5fbb1776b5d478` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/sursly/league-gothic/`:

```
commit f1d4a1c8c1db3c4a32cc13763c5fbb1776b5d478
Author: Ty Bradford <hello@madebytyler.com>
Date:   Fri Dec 3 10:26:16 2021 -0500

    Merge pull request #1 from emmamarichal/master
```

The `config.yaml` exists at `sources/config.yaml` in the upstream repo.

The google/fonts history shows:
- `7e64fb81d` — "League Gothic: Version 2.001 added (#4146)"

All fields are present and verified.

## Conclusion

All source metadata fields are complete and verified. No action needed.
