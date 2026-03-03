# Investigation: Idiqlat

## Summary

| Field | Value |
|-------|-------|
| Family Name | Idiqlat |
| Slug | idiqlat |
| License Dir | ofl |
| Repository URL | https://github.com/silnrsi/font-idiqlat |
| Commit Hash | 37a6c68fa053f4b4b4c9f6d67c569f66621b6daa |
| Config YAML | none (uses archive_url with prebuilt TTFs) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/silnrsi/font-idiqlat"
  commit: "37a6c68fa053f4b4b4c9f6d67c569f66621b6daa"
  archive_url: "https://github.com/silnrsi/font-idiqlat/releases/download/v2.000/Idiqlat-2.000.zip"
  files {
    source_file: "Idiqlat-2.000/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Idiqlat-2.000/Idiqlat-ExtraLight.ttf"
    dest_file: "Idiqlat-ExtraLight.ttf"
  }
  files {
    source_file: "Idiqlat-2.000/Idiqlat-Light.ttf"
    dest_file: "Idiqlat-Light.ttf"
  }
  files {
    source_file: "Idiqlat-2.000/Idiqlat-Regular.ttf"
    dest_file: "Idiqlat-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb at `ofl/idiqlat/METADATA.pb` contains a complete source block with a repository URL, commit hash, archive URL, and explicit file mappings. The font was added to google/fonts by Emma Marichal in commit `5f85f5cbc91cc82480e505da3dfa150fb296a1ff`.

The commit message body for `5f85f5cbc` explicitly states:

> "Taken from the upstream repo https://github.com/silnrsi/font-idiqlat at commit https://github.com/silnrsi/font-idiqlat/commit/37a6c68fa053f4b4b4c9f6d67c569f66621b6daa."

This directly confirms the repository URL and commit hash recorded in METADATA.pb.

The upstream repository `https://github.com/silnrsi/font-idiqlat` is **not** present in the local cache at `upstream_repos/fontc_crater_cache/silnrsi/` (the silnrsi cache contains other SIL repositories but not font-idiqlat). The METADATA.pb uses `archive_url` to fetch prebuilt TTF files from a GitHub release (`v2.000`), rather than building from source files. This is the standard approach for SIL fonts that don't have gftools-builder compatible source files exposed.

The `date_added` field is `2026-01-22`, indicating this is a very recently added font. A subsequent commit `8d66a498f6a0b489538a8bbaabf08558a0ead238` added an article for the family, confirming the onboarding was complete.

Since the source block uses `archive_url` to fetch prebuilt binaries, no `config.yaml` is needed or applicable. The `config_yaml` field is absent from the METADATA.pb source block, which is correct for this pattern.

## Conclusion

The source block in METADATA.pb is complete and correct. The repository URL, commit hash, archive URL, and file mappings are all documented. The `archive_url` approach means no `config.yaml` is needed. No action is required. The `silnrsi/font-idiqlat` repository should be added to the fontc_crater_cache when disk space allows.
