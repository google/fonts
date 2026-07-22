# Investigation: IBM Plex Serif

## Summary

| Field | Value |
|-------|-------|
| Family Name | IBM Plex Serif |
| Slug | ibm-plex-serif |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/plex |
| Commit Hash | 43279c151110b30d65a582261a5ddefd5c75c7be |
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
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-Bold.ttf"
    dest_file: "IBMPlexSerif-Bold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-BoldItalic.ttf"
    dest_file: "IBMPlexSerif-BoldItalic.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-ExtraLight.ttf"
    dest_file: "IBMPlexSerif-ExtraLight.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-ExtraLightItalic.ttf"
    dest_file: "IBMPlexSerif-ExtraLightItalic.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-Italic.ttf"
    dest_file: "IBMPlexSerif-Italic.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-Light.ttf"
    dest_file: "IBMPlexSerif-Light.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-LightItalic.ttf"
    dest_file: "IBMPlexSerif-LightItalic.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-Medium.ttf"
    dest_file: "IBMPlexSerif-Medium.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-MediumItalic.ttf"
    dest_file: "IBMPlexSerif-MediumItalic.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-Regular.ttf"
    dest_file: "IBMPlexSerif-Regular.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-SemiBold.ttf"
    dest_file: "IBMPlexSerif-SemiBold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-SemiBoldItalic.ttf"
    dest_file: "IBMPlexSerif-SemiBoldItalic.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-Thin.ttf"
    dest_file: "IBMPlexSerif-Thin.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/IBMPlexSerif-ThinItalic.ttf"
    dest_file: "IBMPlexSerif-ThinItalic.ttf"
  }
  branch: "master"
}
```

## Investigation

### METADATA.pb Analysis

The METADATA.pb has a `source` block with `repository_url: "https://github.com/googlefonts/plex"` and `branch: "master"`, but is **missing the `commit` field**. The file mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/`. The fonts are 14 static TTFs: 7 weights (Thin through Bold) in both Roman and Italic.

### Git History in google/fonts

The TTF file history shows four commits:

```
b598f5e3a IBM Plex Serif: Version 2.6 added (#3544)
115c6eb01 Add updated and new versions of IBM Plex (#1837)
02d76fa55 ibmplexserif: v2.001 Bold added. (#1488)
e39edaea9 ibmplexserif: v2.001 added (#1482)
```

The most recent commit `b598f5e3a` (by Yanone, 2021-06-23) is the authoritative onboarding commit for the current TTF files. Its commit body contains three squashed gftools-packager sub-commits:

1. "[gftools-packager] IBM Plex Serif: Version 2.6 added"
2. "IBM Plex Serif Version 2.6 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/43279c151110b30d65a582261a5ddefd5c75c7be."
3. "[gftools-packager] ofl/ibmplexserif remove METADATA "source".  google/fonts#2587"

The third sub-commit removed the `source` block from METADATA.pb (per issue #2587 which cleaned up incomplete source blocks). The source block was later re-added, but without the commit hash.

IBM Plex Serif was originally added to Google Fonts in 2018 (`e39edaea9`), updated in 2019 (`115c6eb01`), and last updated to Version 2.6 in June 2021 (`b598f5e3a`). The Version 2.6 commit represents the current state of the files in google/fonts.

### Upstream Repository Verification

The plex repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/plex/`.

Commit `43279c151110b30d65a582261a5ddefd5c75c7be` exists in the cache. At this commit, source design files exist for IBM Plex Serif:

- `IBM-Plex-Serif/sources/masters/IBM Plex Serif Roman.designspace`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif Italic.designspace`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif-Bold.ufo/features.fea`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif-Bold Italic.ufo/features.fea`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif-Italic.ufo/features.fea`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif-Regular.ufo/features.fea`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif-Thin.ufo/features.fea`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif-Thin Italic.ufo/features.fea`
- Plus per-weight `.vfb` instance files for both postscript and truetype

The `Google-Fonts-Fixes/packager/serif.yaml` file at this commit is a gftools-packager config (not a gftools-builder config.yaml). It maps pre-built TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Serif/fonts/complete/ttf/` to their destinations.

No gftools-builder `config.yaml` exists in the upstream repo or in the `ofl/ibmplexserif/` directory in google/fonts.

### Source Files

IBM Plex Serif has two `.designspace` files and 6 UFO masters (`IBM-Plex-Serif/sources/masters/`) at the referenced commit. The actual fonts in google/fonts are pre-compiled TTFs copied from `Google-Fonts-Fixes/`, not compiled directly from sources. An override `config.yaml` could be created pointing to the `.designspace` files.

## Conclusion

The METADATA.pb source block is missing the `commit` field. The correct commit hash is `43279c151110b30d65a582261a5ddefd5c75c7be`, sourced directly from the gftools-packager message in the google/fonts commit `b598f5e3a`. This commit is verified to exist in the upstream plex repo cache.

Source files (`.designspace` + `.ufo` masters) exist at that commit. IBM Plex Serif has separate Roman and Italic designspace files:
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif Roman.designspace`
- `IBM-Plex-Serif/sources/masters/IBM Plex Serif Italic.designspace`

An override `config.yaml` should be created in the `ofl/ibmplexserif/` directory in google/fonts pointing to these sources.

Action needed: Add `commit: "43279c151110b30d65a582261a5ddefd5c75c7be"` to the METADATA.pb source block, and create an override `config.yaml`.
