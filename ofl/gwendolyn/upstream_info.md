# Investigation Report: Gwendolyn

## Summary

Gwendolyn is a handwriting/display font designed by Robert Leuschke. It was added to Google Fonts on 2021-11-04 by Viviana Monsalve via gftools-packager (PR #4002). The upstream repository at `https://github.com/googlefonts/gwendolyn` has a single commit which is correctly referenced in METADATA.pb. The repo includes `sources/config.yml` which is properly documented. The source block is fully complete.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gwendolyn                                                          |
| Designer           | Robert Leuschke                                                    |
| Date Added         | 2021-11-02                                                         |
| Repository URL     | https://github.com/googlefonts/gwendolyn                           |
| Commit Hash        | 8ab228a0fd9cc201781ce4596cb039330b504e57                            |
| Config YAML        | sources/config.yml (in upstream repo)                              |
| Source Files       | sources/GwendolynPro.glyphs                                       |
| Status             | **complete**                                                       |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a comprehensive source block with:
- `repository_url`: `https://github.com/googlefonts/gwendolyn`
- `commit`: `8ab228a0fd9cc201781ce4596cb039330b504e57`
- `config_yaml`: `sources/config.yml`
- `branch`: `master`
- File mappings for `OFL.txt`, `DESCRIPTION.en_us.html`, `fonts/ttf/Gwendolyn-Regular.ttf`, and `fonts/ttf/Gwendolyn-Bold.ttf`

### Git History in google/fonts

Key commits affecting `ofl/gwendolyn/`:

1. **306bf7bf** (2021-11-04) - Viviana Monsalve: "Gwendolyn: Version 1.010; ttfautohint (v1.8.3) added (#4002)". The commit body contains: "[gftools-packager] Gwendolyn: Version 1.010; ttfautohint (v1.8.3) added" and explicitly states: "taken from the upstream repo https://github.com/googlefonts/gwendolyn at commit 8ab228a0fd9cc201781ce4596cb039330b504e57." This commit also created an `upstream.yaml` file.
2. **66f91f10** (2024-04-03) - "Merge upstream.yaml into METADATA.pb [skip ci]" - migrated the source info from upstream.yaml into METADATA.pb.
3. **19cdcec5** (2025-03-31) - "[Batch 1/4] port info from fontc_crater targets list" - added additional source metadata.

### Upstream Repository Inspection

The upstream repo at `googlefonts/gwendolyn` contains a single commit:
- **8ab228a** (2021-11-02) by Viviana Monsalve: "version 1.010 fonts added"

This is the only commit in the entire repository, making the hash unambiguously correct.

Repository contents:
- `sources/GwendolynPro.glyphs` - Glyphs source file
- `sources/config.yml` - gftools-builder config
- `fonts/ttf/Gwendolyn-Regular.ttf` - Compiled Regular TTF
- `fonts/ttf/Gwendolyn-Bold.ttf` - Compiled Bold TTF
- `fonts/otf/Gwendolyn-Regular.otf` - Compiled Regular OTF
- `fonts/otf/Gwendolyn-Bold.otf` - Compiled Bold OTF
- `OFL.txt` - License
- `DESCRIPTION.en_us.html` - Description
- `requirements.txt` - Python requirements

The `sources/config.yml` contains:
```yaml
sources:
  - GwendolynPro.glyphs
familyName: "Gwendolyn"
buildVariable: false
#autohintTTF: false
```

### Commit Hash Verification

The commit hash `8ab228a` is explicitly referenced in the google/fonts onboarding commit message (PR #4002) by Viviana Monsalve using gftools-packager. The upstream repo has only one commit, making this unambiguously correct. The same commit hash was also present in the `upstream.yaml` file created during onboarding.

## Conclusion

The source block for Gwendolyn is **complete**. All fields are correct: repository URL, commit hash, config_yaml path (note: uses `.yml` extension, not `.yaml`), branch, and file mappings.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/gwendolyn"
  commit: "8ab228a0fd9cc201781ce4596cb039330b504e57"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Gwendolyn-Regular.ttf"
    dest_file: "Gwendolyn-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Gwendolyn-Bold.ttf"
    dest_file: "Gwendolyn-Bold.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

**Status**: complete
**Confidence**: HIGH
