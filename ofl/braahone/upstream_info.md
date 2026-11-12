# Investigation: Braah One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Braah One |
| Slug | braah-one |
| License Dir | ofl |
| Repository URL | https://github.com/artandtype/Braah |
| Commit Hash | 2b7ba2ea006af5a55313158531b6f0b71eca5ff8 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/artandtype/Braah"
  commit: "2b7ba2ea006af5a55313158531b6f0b71eca5ff8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BraahOne-Regular.ttf"
    dest_file: "BraahOne-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

### Git History in google/fonts

The font has two commits in google/fonts:

1. `20db4c2da` — `[gftools-packager] Braah One: Version 1.001; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.29] added`
2. `ff85c4135` — `[gftools-packager] Braah One: Version 1.000 added`

The most recent packager commit message states:

> Braah One Version 1.001; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.29] taken from the upstream repo https://github.com/artandtype/Braah at commit https://github.com/artandtype/Braah/commit/2b7ba2ea006af5a55313158531b6f0b71eca5ff8.

This directly confirms both the repository URL and the commit hash in METADATA.pb.

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/artandtype/Braah`. Commit `2b7ba2ea006af5a55313158531b6f0b71eca5ff8` was verified to exist — it is the latest commit on the master branch ("Merge pull request #3 from emmamarichal/master").

The upstream repository does **not** contain a `config.yaml` file. The sources directory contains:
- `sources/BraahOne.glyphs` — the primary Glyphs source file
- `sources/BraahOne-Regular.enc`, `.fea`, `.flc`, `.vfc`, `.vfm` — auxiliary files

### Override config.yaml in google/fonts

An override `config.yaml` already exists in `ofl/braahone/config.yaml` (in google/fonts) with the following content:

```yaml
buildVariable: false
sources:
  - sources/BraahOne.glyphs
```

This override correctly references the Glyphs source at `sources/BraahOne.glyphs`, which is a valid path relative to the upstream repo root. The `METADATA.pb` does not set `config_yaml` (correct behavior when an override is present in the google/fonts directory).

### METADATA.pb Status

The source block is already present and complete in METADATA.pb on the main branch:
- `repository_url` is set and correct
- `commit` is set and matches the gftools-packager commit message
- No `config_yaml` field in METADATA.pb (correct — override config.yaml exists in google/fonts)

## Conclusion

No action needed. The source block in METADATA.pb is complete and correct. The override `config.yaml` in `ofl/braahone/config.yaml` handles build configuration. Status is **complete** with HIGH confidence.
