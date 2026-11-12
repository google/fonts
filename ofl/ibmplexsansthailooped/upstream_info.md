# Investigation: IBM Plex Sans Thai Looped

## Summary

| Field | Value |
|-------|-------|
| Family Name | IBM Plex Sans Thai Looped |
| Slug | ibm-plex-sans-thai-looped |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/plex |
| Commit Hash | 20f93381c40c4779f2297bb31c60fbc2992620b6 |
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
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/IBMPlexSansThaiLooped-Bold.ttf"
    dest_file: "IBMPlexSansThaiLooped-Bold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/IBMPlexSansThaiLooped-ExtraLight.ttf"
    dest_file: "IBMPlexSansThaiLooped-ExtraLight.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/IBMPlexSansThaiLooped-Light.ttf"
    dest_file: "IBMPlexSansThaiLooped-Light.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/IBMPlexSansThaiLooped-Medium.ttf"
    dest_file: "IBMPlexSansThaiLooped-Medium.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/IBMPlexSansThaiLooped-Regular.ttf"
    dest_file: "IBMPlexSansThaiLooped-Regular.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/IBMPlexSansThaiLooped-SemiBold.ttf"
    dest_file: "IBMPlexSansThaiLooped-SemiBold.ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/IBMPlexSansThaiLooped-Thin.ttf"
    dest_file: "IBMPlexSansThaiLooped-Thin.ttf"
  }
  branch: "master"
}
```

## Investigation

### METADATA.pb Analysis

The METADATA.pb has a `source` block with `repository_url: "https://github.com/googlefonts/plex"` and `branch: "master"`, but is **missing the `commit` field**. The file mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/`. The fonts are 7 static weights (Thin through Bold, no italics).

### Git History in google/fonts

The TTF file history shows a single commit:

```
0457aa161 IBM Plex Sans Thai Looped: Version 1.1 added (#3558)
```

This is the only commit that has ever modified the TTF files in `ofl/ibmplexsansthailooped/`. The commit was made by Yanone on 2021-07-01.

The commit body contains three squashed gftools-packager sub-commits:
1. "[gftools-packager] IBM Plex Sans Thai Looped: Version 1.1 added"
2. "IBM Plex Sans Thai Looped Version 1.1 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/20f93381c40c4779f2297bb31c60fbc2992620b6."
3. "[gftools-packager] ofl/ibmplexsansthailooped remove METADATA "source".  google/fonts#2587"

The third sub-commit removed the `source` block from METADATA.pb (per issue #2587 which cleaned up incomplete source blocks). The source block was later re-added, but without the commit hash.

### Upstream Repository Verification

The plex repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/plex/`.

Commit `20f93381c40c4779f2297bb31c60fbc2992620b6` exists in the cache. At this commit, source design files exist for IBM Plex Sans Thai Looped:

- `IBM-Plex-Sans-Thai-Looped/sources/masters/IBM Plex Sans Thai Looped.designspace`
- `IBM-Plex-Sans-Thai-Looped/sources/masters/IBM Plex Sans Thai Looped-Bold.ufo/features.fea`
- `IBM-Plex-Sans-Thai-Looped/sources/masters/IBM Plex Sans Thai Looped-Regular.ufo/features.fea`
- `IBM-Plex-Sans-Thai-Looped/sources/masters/IBM Plex Sans Thai Looped-Thin.ufo/features.fea`
- Plus per-weight `.vfb` instance files for both postscript and truetype

The `Google-Fonts-Fixes/packager/sans-thai-looped.yaml` file at this commit is a gftools-packager config (not a gftools-builder config.yaml). It maps pre-built TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Thai-Looped/fonts/complete/ttf/` to their destinations.

No gftools-builder `config.yaml` exists in the upstream repo or in the `ofl/ibmplexsansthailooped/` directory in google/fonts.

### Source Files

IBM Plex Sans Thai Looped has a `.designspace` file and 3 UFO masters (`IBM-Plex-Sans-Thai-Looped/sources/masters/`) at the referenced commit. The actual fonts in google/fonts are pre-compiled TTFs copied from `Google-Fonts-Fixes/`, not compiled directly from sources. An override `config.yaml` could be created pointing to the `.designspace` file.

## Conclusion

The METADATA.pb source block is missing the `commit` field. The correct commit hash is `20f93381c40c4779f2297bb31c60fbc2992620b6`, sourced directly from the gftools-packager message in the google/fonts commit `0457aa161`. This commit is verified to exist in the upstream plex repo cache.

Source files (`.designspace` + `.ufo` masters) exist at that commit at path `IBM-Plex-Sans-Thai-Looped/sources/masters/IBM Plex Sans Thai Looped.designspace`. An override `config.yaml` should be created in the `ofl/ibmplexsansthailooped/` directory in google/fonts pointing to this source.

Action needed: Add `commit: "20f93381c40c4779f2297bb31c60fbc2992620b6"` to the METADATA.pb source block, and create an override `config.yaml`.
