# Investigation: Jaro

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jaro |
| Slug | jaro |
| License Dir | ofl |
| Repository URL | https://github.com/agyeiarcher/Jaro |
| Commit Hash | 51096c4f8e9e0076709d509b905741470beb972d |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/agyeiarcher/Jaro"
  commit: "51096c4f8e9e0076709d509b905741470beb972d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Jaro[opsz].ttf"
    dest_file: "Jaro[opsz].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows one commit touching this font:
- `2a07a56bc` — "[gftools-packager] Jaro: Version 1.000 added" (initial onboarding)

The commit message for `2a07a56bc` explicitly states: "Jaro Version 1.000 taken from the upstream repo https://github.com/agyeiarcher/Jaro at commit https://github.com/agyeiarcher/Jaro/commit/51096c4f8e9e0076709d509b905741470beb972d."

The METADATA.pb was later updated by `66f91f10f` ("Merge upstream.yaml into METADATA.pb") which consolidated the upstream information, and `19cdcec59` which ported fontc_crater data.

The upstream repository `agyeiarcher/Jaro` is cached at `upstream_repos/fontc_crater_cache/agyeiarcher/Jaro`. Commit `51096c4f8e9e0076709d509b905741470beb972d` exists in the repo — it is a merge commit ("Merge pull request #14 from emmamarichal/main") that added build infrastructure including the GitHub Actions workflow. The file `sources/config.yaml` exists in the upstream repo.

The METADATA.pb lists designers as "Agyei Archer, Céline Hurka, Mirko Velimirović" (updated from the initial "Celine Hurka" spelling by commit `0c4315f94`).

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`51096c4f8e9e0076709d509b905741470beb972d`), and config_yaml (`sources/config.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.
