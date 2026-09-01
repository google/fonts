# Investigation: IBM Plex Sans KR

## Summary

| Field | Value |
|-------|-------|
| Family Name | IBM Plex Sans KR |
| Slug | ibm-plex-sans-kr |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/plex |
| Commit Hash | 1331d4514d6ab96ddf2efbb59f0b640b9a4e9d87 |
| Config YAML | none (sources exist at commit, override needed) |
| Status | missing_commit |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/plex"
  files {
    source_file: "LICENSE.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Google-Fonts-Fixes/descriptions/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/IBMPlexSansKR-Bold.ttf"
    dest_file: "IBMPlexSansKR-Bold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/IBMPlexSansKR-ExtraLight.ttf"
    dest_file: "IBMPlexSansKR-ExtraLight.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/IBMPlexSansKR-Light.ttf"
    dest_file: "IBMPlexSansKR-Light.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/IBMPlexSansKR-Medium.ttf"
    dest_file: "IBMPlexSansKR-Medium.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/IBMPlexSansKR-Regular.ttf"
    dest_file: "IBMPlexSansKR-Regular.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/IBMPlexSansKR-SemiBold.ttf"
    dest_file: "IBMPlexSansKR-SemiBold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/IBMPlexSansKR-Thin.ttf"
    dest_file: "IBMPlexSansKR-Thin.ttf"
  }
  branch: "master"
}
```

## Investigation

### METADATA.pb Analysis

The METADATA.pb has a `source` block with `repository_url: "https://github.com/googlefonts/plex"` and `branch: "master"`, but is **missing the `commit` field**. The file mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/`. The fonts are 7 static weights (Thin through Bold, no italics).

### Git History in google/fonts

The TTF file history shows a single commit:

```
29731dada IBM Plex Sans KR: Version 1.001 added (#3556)
```

This is the only commit that has ever modified the TTF files in `ofl/ibmplexsanskr/`. The commit was made by Yanone on 2021-07-01.

The commit body contains three squashed gftools-packager sub-commits:
1. "[gftools-packager] IBM Plex Sans KR: Version 1.001 added"
2. "IBM Plex Sans KR Version 1.001 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/1331d4514d6ab96ddf2efbb59f0b640b9a4e9d87."
3. "[gftools-packager] ofl/ibmplexsanskr remove METADATA "source".  google/fonts#2587"

The third sub-commit removed the `source` block from METADATA.pb (per issue #2587 which cleaned up incomplete source blocks). The source block was later re-added by a later merge of upstream.yaml data into METADATA.pb, but without the commit hash.

### Upstream Repository Verification

The plex repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/plex/`.

Commit `1331d4514d6ab96ddf2efbb59f0b640b9a4e9d87` exists in the cache. At this commit, source design files exist:

- `IBM-Plex-Sans-KR/sources/masters/IBM Plex Sans KR.glyphs` (master Glyphs file)
- `IBM-Plex-Sans-KR/sources/instances/postscript/IBM Plex Sans KR-{weight}.glyphs` (per-weight instance files)
- `IBM-Plex-Sans-KR/sources/instances/truetype/IBM Plex Sans KR-{weight}.glyphs` (per-weight instance files)

The `Google-Fonts-Fixes/packager/sans-kr.yaml` file at this commit is a gftools-packager config (not a gftools-builder config.yaml). It maps pre-built TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-KR/fonts/complete/ttf/` to their destinations.

No gftools-builder `config.yaml` exists in the upstream repo or in the `ofl/ibmplexsanskr/` directory in google/fonts.

### Source Files

IBM Plex Sans KR has a `.glyphs` master file (`IBM-Plex-Sans-KR/sources/masters/IBM Plex Sans KR.glyphs`) at the referenced commit. The actual fonts in google/fonts are pre-compiled TTFs copied from `Google-Fonts-Fixes/`, not compiled directly from the `.glyphs` source. An override `config.yaml` could be created pointing to the `.glyphs` file, similar to the approach taken for IBM Plex Sans JP.

## Conclusion

The METADATA.pb source block is missing the `commit` field. The correct commit hash is `1331d4514d6ab96ddf2efbb59f0b640b9a4e9d87`, sourced directly from the gftools-packager message in the google/fonts commit `29731dada`. This commit is verified to exist in the upstream plex repo cache.

A source `.glyphs` file exists at that commit (`IBM-Plex-Sans-KR/sources/masters/IBM Plex Sans KR.glyphs`). An override `config.yaml` should be created in the `ofl/ibmplexsanskr/` directory in google/fonts pointing to this source.

Action needed: Add `commit: "1331d4514d6ab96ddf2efbb59f0b640b9a4e9d87"` to the METADATA.pb source block, and create an override `config.yaml`.
