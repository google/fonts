# Investigation: Bonheur Royale

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bonheur Royale |
| Slug | bonheur-royale |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/bonheur-royale |
| Commit Hash | 90087bb825c798641a29d2a1114ce7acd4048b0b |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/bonheur-royale"
  commit: "90087bb825c798641a29d2a1114ce7acd4048b0b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BonheurRoyale-Regular.ttf"
    dest_file: "BonheurRoyale-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

Bonheur Royale is a handwriting typeface by Robert Leuschke, added to Google Fonts on 2021-08-06.

### Git History

The font TTF file was added by google/fonts commit `0bc581c03` (PR #3675, 2021-08-10, author: Viviana Monsalve):

```
[gftools-packager] Bonheur Royale: Version 1.010; ttfautohint (v1.8.3) added (#3675)

Bonheur Royale Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo
https://github.com/googlefonts/bonheur-royale at commit
https://github.com/googlefonts/bonheur-royale/commit/5437451c7ef27d37081b96d4f73c445ca1813b10.
```

Note: The original packager commit referenced `5437451c` as the onboarding commit. The current METADATA.pb records `90087bb8` instead, which was added by commit `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list"), porting data from the fontc_crater targets list.

The source block was first created by commit `66f91f10f` (2024-04-03, "Merge upstream.yaml into METADATA.pb"), but without a commit hash. The commit hash and `config_yaml` were added by `19cdcec59` (2025-03-31).

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/bonheur-royale/`. The repository's commit history:

```
90087bb Nhung added to Contributors     <-- current METADATA.pb reference (HEAD)
5437451 py for sample imagge added      <-- original packager onboarding commit
b1e50d6 v1.010 fonts added
```

Commit `90087bb` (2021-08-06, "Nhung added to Contributors") is the repo HEAD. Commit `5437451c` ("py for sample imagge added", 2021-08-06 12:20) predates `90087bb` (2021-08-06 17:52). The font binary in google/fonts was taken from `b1e50d6` ("v1.010 fonts added"), which is an ancestor of both. The difference between `5437451c` and `90087bb` is only the CONTRIBUTORS.txt file. No source files, fonts, or build configuration changed between these two commits.

The `sources/config.yml` (note: `.yml` extension) exists at both commits and contains:
```yaml
sources:
  - BonheurRoyale.glyphs
familyName: "Bonheur Royale"
buildVariable: false
```

### Verification

- Repository URL: Confirmed correct (stated in packager commit and copyright string)
- Commit hash: `90087bb8` is the HEAD (not the original onboarding commit `5437451c`); the only difference is a CONTRIBUTORS.txt update — no functional change
- Config YAML: `sources/config.yml` (`.yml` extension) exists at the recorded commit and is valid
- Source files: `fonts/ttf/BonheurRoyale-Regular.ttf` exists in the upstream repo at `90087bb8`

## Conclusion

The METADATA.pb source block is complete and functional. The commit `90087bb8` is the HEAD of the upstream repo and is only 5 hours later than the original onboarding commit `5437451c` — the only difference is a name added to CONTRIBUTORS.txt, with no source or font changes. The config.yml is correctly referenced (note the `.yml` extension). No action needed.
