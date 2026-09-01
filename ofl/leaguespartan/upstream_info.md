# Investigation: League Spartan

## Summary

| Field | Value |
|-------|-------|
| Family Name | League Spartan |
| Slug | league-spartan |
| License Dir | ofl |
| Repository URL | https://github.com/theleagueof/league-spartan |
| Commit Hash | 27341b9bf93a2c7faa140538a64ce342486c5fb5 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/theleagueof/league-spartan"
  commit: "27341b9bf93a2c7faa140538a64ce342486c5fb5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/LeagueSpartan[wght].ttf"
    dest_file: "LeagueSpartan[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb has `repository_url`, `commit` hash, and `config_yaml` all populated. The commit `27341b9bf93a2c7faa140538a64ce342486c5fb5` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/theleagueof/league-spartan/`:

```
commit 27341b9bf93a2c7faa140538a64ce342486c5fb5
Author: Ty Bradford <hello@madebytyler.com>
Date:   Thu Dec 16 11:12:36 2021 -0500

    Merge pull request #37 from emmamarichal/master
```

The `config.yaml` exists at `sources/config.yaml` in the upstream repo.

The google/fonts history shows:
- `c762083ef` — "League Spartan: Version 2.002 added (#4122)"

All fields are present and verified.

## Conclusion

All source metadata fields are complete and verified. No action needed.
