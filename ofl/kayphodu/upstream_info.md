# Investigation: Kay Pho Du

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kay Pho Du |
| Slug | kay-pho-du |
| License Dir | ofl |
| Repository URL | https://github.com/silnrsi/font-kayphodu |
| Commit Hash | unknown |
| Config YAML | none (SIL smith build system) |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/silnrsi/font-kayphodu"
  archive_url: "https://github.com/silnrsi/font-kayphodu/releases/download/v3.000/KayPhoDu-3.000.zip"
  files {
    source_file: "KayPhoDu-3.000/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "KayPhoDu-3.000/KayPhoDu-Regular.ttf"
    dest_file: "KayPhoDu-Regular.ttf"
  }
  files {
    source_file: "KayPhoDu-3.000/KayPhoDu-Medium.ttf"
    dest_file: "KayPhoDu-Medium.ttf"
  }
  files {
    source_file: "KayPhoDu-3.000/KayPhoDu-SemiBold.ttf"
    dest_file: "KayPhoDu-SemiBold.ttf"
  }
  files {
    source_file: "KayPhoDu-3.000/KayPhoDu-Bold.ttf"
    dest_file: "KayPhoDu-Bold.ttf"
  }
  branch: "master"
}
primary_script: "Kali"
stroke: "SLAB_SERIF"
```

## Investigation

The METADATA.pb contains `repository_url` and `archive_url` but no `commit`. The upstream repository `silnrsi/font-kayphodu` is cached at `upstream_repos/fontc_crater_cache/silnrsi/font-kayphodu`.

This is a SIL International font that uses the SIL smith build system. The `source/` directory contains:
- `KayPhoDu.designspace` (Designspace format)
- `KayPhoDuR.designspace`
- `masters/` (UFO masters)

The font was onboarded using a release archive (v3.000), not directly from a git commit. The `archive_url` references the v3.000 release.

The git log shows the latest commit is `18bf51b` ("[FTLS-941] Fix links and text in about.md [nobuild]"). The repository uses SIL's wscript build system, not gftools-builder. No `config.yaml` exists.

## Conclusion

This family uses a release archive for onboarding. The source block is missing a `commit` field corresponding to the v3.000 release. The SIL smith build system is not compatible with gftools-builder, so no `config.yaml` is possible. The commit hash for the v3.000 release tag needs to be found.

## Commit Added (HIGH confidence)

Commit `4c49d8ac7ae00cf0ee10db3c3c35dc49ca9efd4d` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2023-10-04). This is the most reliable method.
