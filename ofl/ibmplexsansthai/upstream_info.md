# Investigation: IBM Plex Sans Thai

## Summary

| Field | Value |
|-------|-------|
| Family Name | IBM Plex Sans Thai |
| Slug | ibm-plex-sans-thai |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/plex |
| Commit Hash | 67b4babc1f9b57d6ad3e362cf5bbc1c4026b2d63 |
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
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/IBMPlexSansThai-Bold.ttf"
    dest_file: "IBMPlexSansThai-Bold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/IBMPlexSansThai-ExtraLight.ttf"
    dest_file: "IBMPlexSansThai-ExtraLight.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/IBMPlexSansThai-Light.ttf"
    dest_file: "IBMPlexSansThai-Light.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/IBMPlexSansThai-Medium.ttf"
    dest_file: "IBMPlexSansThai-Medium.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/IBMPlexSansThai-Regular.ttf"
    dest_file: "IBMPlexSansThai-Regular.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/IBMPlexSansThai-SemiBold.ttf"
    dest_file: "IBMPlexSansThai-SemiBold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/IBMPlexSansThai-Thin.ttf"
    dest_file: "IBMPlexSansThai-Thin.ttf"
  }
  branch: "master"
}
```

## Investigation

### METADATA.pb Analysis

The METADATA.pb has a `source` block with `repository_url: "https://github.com/googlefonts/plex"` and `branch: "master"`, but is **missing the `commit` field**. The file mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/`. The fonts are 7 static weights (Thin through Bold, no italics).

### Git History in google/fonts

The TTF file history shows a single commit:

```
3b7aef15c IBM Plex Sans Thai: Version 1.1 added (#3557)
```

This is the only commit that has ever modified the TTF files in `ofl/ibmplexsansthai/`. The commit was made by Yanone on 2021-07-01.

The commit body contains three squashed gftools-packager sub-commits:
1. "[gftools-packager] IBM Plex Sans Thai: Version 1.1 added"
2. "IBM Plex Sans Thai Version 1.1 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/67b4babc1f9b57d6ad3e362cf5bbc1c4026b2d63."
3. "[gftools-packager] ofl/ibmplexsansthai remove METADATA "source".  google/fonts#2587"

The third sub-commit removed the `source` block from METADATA.pb (per issue #2587 which cleaned up incomplete source blocks). The source block was later re-added, but without the commit hash.

### Upstream Repository Verification

The plex repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/plex/`.

Commit `67b4babc1f9b57d6ad3e362cf5bbc1c4026b2d63` exists in the cache. At this commit, source design files exist for IBM Plex Sans Thai:

- `IBM-Plex-Sans-Thai/sources/masters/IBM Plex Sans Thai.designspace`
- `IBM-Plex-Sans-Thai/sources/masters/IBM Plex Sans Thai-Bold.ufo/features.fea`
- `IBM-Plex-Sans-Thai/sources/masters/IBM Plex Sans Thai-Regular.ufo/features.fea`
- `IBM-Plex-Sans-Thai/sources/masters/IBM Plex Sans Thai-Thin.ufo/features.fea`
- Plus per-weight `.vfb` instance files for both postscript and truetype

The `Google-Fonts-Fixes/packager/sans-thai.yaml` file at this commit is a gftools-packager config (not a gftools-builder config.yaml). It maps pre-built TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai/fonts/complete/ttf/` to their destinations.

No gftools-builder `config.yaml` exists in the upstream repo or in the `ofl/ibmplexsansthai/` directory in google/fonts.

### Source Files

IBM Plex Sans Thai has a `.designspace` file and 3 UFO masters (`IBM-Plex-Sans-Thai/sources/masters/`) at the referenced commit. The actual fonts in google/fonts are pre-compiled TTFs copied from `Google-Fonts-Fixes/`, not compiled directly from sources. An override `config.yaml` could be created pointing to the `.designspace` file.

## Conclusion

The METADATA.pb source block is missing the `commit` field. The correct commit hash is `67b4babc1f9b57d6ad3e362cf5bbc1c4026b2d63`, sourced directly from the gftools-packager message in the google/fonts commit `3b7aef15c`. This commit is verified to exist in the upstream plex repo cache.

Source files (`.designspace` + `.ufo` masters) exist at that commit at path `IBM-Plex-Sans-Thai/sources/masters/IBM Plex Sans Thai.designspace`. An override `config.yaml` should be created in the `ofl/ibmplexsansthai/` directory in google/fonts pointing to this source.

Action needed: Add `commit: "67b4babc1f9b57d6ad3e362cf5bbc1c4026b2d63"` to the METADATA.pb source block, and create an override `config.yaml`.
