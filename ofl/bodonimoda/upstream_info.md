# Investigation: Bodoni Moda

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bodoni Moda |
| Slug | bodoni-moda |
| License Dir | ofl |
| Repository URL | https://github.com/indestructible-type/Bodoni |
| Commit Hash | 30ce6cdc354ef179a3b72ba0f0e71826e599348c |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/indestructible-type/Bodoni"
  commit: "30ce6cdc354ef179a3b72ba0f0e71826e599348c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BodoniModa[opsz,wght].ttf"
    dest_file: "BodoniModa[opsz,wght].ttf"
  }
  files {
    source_file: "fonts/variable/BodoniModa-Italic[opsz,wght].ttf"
    dest_file: "BodoniModa-Italic[opsz,wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Bodoni Moda is a variable serif typeface by Owen Earl (Indestructible Type), added to Google Fonts on 2020-11-25. It features optical size (opsz) and weight (wght) axes in both roman and italic.

### Git History

The font files were last updated by google/fonts commit `634558fcb` (2024-02-21, author: Emma Marichal):

```
[gftools-packager] Bodoni Moda: Version 2.005 added

Bodoni Moda Version 2.005 taken from the upstream repo
https://github.com/indestructible-type/Bodoni at commit
https://github.com/indestructible-type/Bodoni/commit/30ce6cdc354ef179a3b72ba0f0e71826e599348c.
```

This gftools-packager commit explicitly documents both the upstream repository and the exact commit hash. A subsequent commit `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list") added the `config_yaml: "sources/config.yaml"` field to the source block.

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/indestructible-type/Bodoni/`. Commit `30ce6cdc` is a merge commit ("Merge pull request #38 from emmamarichal/master", 2024-02-18) and is the HEAD of the master branch.

The config.yaml at `sources/config.yaml` contains valid gftools-builder configuration:
- Sources: `BodoniModa.glyphs`, `BodoniModa-Italic.glyphs`
- `buildOTF: false`
- `familyName: Bodoni Moda`
- Full STAT table configuration for opsz, wght, and ital axes for both roman and italic variable fonts

### Verification

- Repository URL: Confirmed correct (stated in packager commit and copyright string)
- Commit hash: Confirmed correct (stated in packager commit, commit exists in upstream repo as HEAD of master)
- Config YAML path: Confirmed — `sources/config.yaml` exists at the referenced commit with valid gftools-builder configuration
- METADATA.pb source block: Fully populated with repository_url, commit, files, branch, and config_yaml

## Conclusion

No action needed. The METADATA.pb source block is complete and accurate. All fields are correctly set: repository URL, commit hash, file mappings, branch, and config_yaml path. This family is fully documented.
