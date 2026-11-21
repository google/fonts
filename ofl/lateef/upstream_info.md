# Investigation: Lateef

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lateef |
| Slug | lateef |
| License Dir | ofl |
| Repository URL | https://github.com/silnrsi/font-lateef |
| Commit Hash | d682ea7cc0305b592058255167c83d059aa640fa |
| Config YAML | Override in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/silnrsi/font-lateef"
  commit: "d682ea7cc0305b592058255167c83d059aa640fa"
  archive_url: "https://github.com/silnrsi/font-lateef/releases/download/v4.400/Lateef-4.400.zip"
  files {
    source_file: "Lateef-4.400/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Lateef-4.400/Lateef-ExtraLight.ttf"
    dest_file: "Lateef-ExtraLight.ttf"
  }
  ...
  branch: "master"
}
```

## Investigation

The METADATA.pb has `repository_url`, `commit` hash, and `archive_url` pointing to the v4.400 release. The commit `d682ea7cc0305b592058255167c83d059aa640fa` was verified to exist in the upstream repo:

```
commit d682ea7cc0305b592058255167c83d059aa640fa
Author: Lorna Evans <LornaSIL@users.noreply.github.com>
Date:   Mon Aug 11 16:00:30 2025 -0500

    Regenerate ftml files. [nobuild]
```

The google/fonts commit (`e73610035`) was made on 2025-09-05 and its body states: "Lateef: Version 4.400 added. Taken from the upstream repo https://github.com/silnrsi/font-lateef at commit https://github.com/silnrsi/font-lateef/commit/d682ea7cc0305b592058255167c83d059aa640fa."

The `v4.400` tag in the upstream points to commit `934a8399` ("Finalize documentation", Aug 2025). The commit `d682ea7cc` is a `[nobuild]` commit that came after the v4.400 tag but before the v4.401 bump. The packager used this as the HEAD reference commit while the actual fonts came from the archive_url.

The upstream repo uses `.designspace` sources in `source/` and does not have a `config.yaml` file.

## Conclusion

Commit hash, repository URL, and archive URL are all present. The commit `d682ea7cc` is a `[nobuild]` commit that is the HEAD of the repo at the time of the v4.400 release packaging. No `config.yaml` exists in the upstream repo; the sources use `.designspace` format with SIL's own build toolchain, and an override in google/fonts names the designspace (see the last section).

## Override config corrected (2026-11-13)

**Model**: Claude Opus 5.5

The override named `source/lateef-edit.designspace`, an editing file whose Light and Black masters no longer exist. smith builds from `source/lateef.designspace` ([wscript](https://github.com/silnrsi/font-lateef/blob/d682ea7cc0305b592058255167c83d059aa640fa/wscript#L43-L45)), so the override now names that, with `buildVariable: false` since only statics ship.

With gftools 0.10.8 and fontmake 3.12.2, all seven weights match the shipped cmap, and every shipped glyph's bounds and advance are within 1 unit. The build keeps the `_`-prefixed component glyphs that smith drops.
