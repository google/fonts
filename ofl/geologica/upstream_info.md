# Investigation Report: Geologica

## Summary

Geologica is a variable sans-serif typeface designed by Monokrom (Sindre Bremnes and Frode Helland), added to Google Fonts on 2023-04-12. The source block in METADATA.pb is complete with repository URL, commit hash, and config_yaml path. All data has been verified against the upstream repository and the onboarding commit message.

## Key Findings

| Field              | Value                                                                      |
|--------------------|----------------------------------------------------------------------------|
| Family Name        | Geologica                                                                  |
| Designer           | Monokrom, Sindre Bremnes, Frode Helland                                   |
| Date Added         | 2023-04-12                                                                 |
| Repository URL     | https://github.com/googlefonts/geologica                                   |
| Commit Hash        | 685f38d7c9e86b0c8530204c97ddcaf6558dd17b                                   |
| Config YAML        | sources/config.yaml                                                        |
| Source Files       | sources/master_ufo/Geologica.designspace (+ 9 UFO masters)                |
| Status             | complete                                                                   |
| Confidence         | HIGH                                                                       |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/geologica"
  commit: "685f38d7c9e86b0c8530204c97ddcaf6558dd17b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Geologica[CRSV,SHRP,slnt,wght].ttf"
    dest_file: "Geologica[CRSV,SHRP,slnt,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

### Onboarding PR and Commit

The font was onboarded via PR #6083, merged on 2023-04-26. The onboarding commit is `1df853d2`:

> [gftools-packager] Geologica: Version 1.010;gftools[0.9.28] added
>
> Geologica Version 1.010;gftools[0.9.28] taken from the upstream repo https://github.com/googlefonts/geologica at commit https://github.com/googlefonts/geologica/commit/685f38d7c9e86b0c8530204c97ddcaf6558dd17b.

The commit hash `685f38d7` in METADATA.pb matches the onboarding commit message exactly.

### Upstream Repository Verification

The upstream repo at `https://github.com/googlefonts/geologica` is cached at `upstream_repos/fontc_crater_cache/googlefonts/geologica/`. The repo has a single commit (the merge commit `685f38d7` that is HEAD of main), confirming this is the exact state used for onboarding.

At commit `685f38d7`:
- **config.yaml** exists at `sources/config.yaml` and references `master_ufo/Geologica.designspace`
- **Source files**: 9 UFO masters + 1 designspace file in `sources/master_ufo/`
- **Variable font**: 4 axes (CRSV, SHRP, slnt, wght)

The config.yaml specifies:
- Source: `master_ufo/Geologica.designspace`
- Axis order: SHRP, wght, CRSV, slnt
- Family name: "Geologica"
- Build options: OTF and webfont disabled

### Source Block History

The source block was initially added via `upstream.yaml` during onboarding, then migrated into METADATA.pb on 2024-04-03 (commit `66f91f10`). The `config_yaml` field was added later in the batch port from fontc_crater targets (commit `19cdcec5`, 2025-03-31).

## Conclusion

### Current METADATA.pb Source Block (Already Correct)

```
source {
  repository_url: "https://github.com/googlefonts/geologica"
  commit: "685f38d7c9e86b0c8530204c97ddcaf6558dd17b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Geologica[CRSV,SHRP,slnt,wght].ttf"
    dest_file: "Geologica[CRSV,SHRP,slnt,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

### Status: complete

All source metadata fields are present and verified. The repository URL, commit hash, and config_yaml path are all correct. No changes needed.
