# Investigation Report: Arimo

## Summary

Arimo is a variable-weight sans-serif typeface designed by Steve Matteson, part of the Croscore family. It was updated to Version 1.33 (variable font) in google/fonts via PR #2713 (merged 2020-10-07), sourced from the TypeNetwork/Arimo repository at commit `77fdf7e0`. The METADATA.pb already has a complete source block with repository_url, commit hash, and file mappings. An override `config.yaml` already exists in the google/fonts family directory. The repository URL now redirects from TypeNetwork/Arimo to davelab6/Arimo (ownership transfer), but the copyright in the font references `https://github.com/googlefonts/arimo`. The source block is complete.

## Key Findings

| Field              | Value                                                        |
|--------------------|--------------------------------------------------------------|
| Family Name        | Arimo                                                        |
| Designer           | Steve Matteson                                               |
| License            | Apache 2.0                                                   |
| Date Added         | 2010-11-18                                                   |
| Repository URL     | https://github.com/TypeNetwork/Arimo                         |
| Commit Hash        | 77fdf7e032ef18c5ad72929bdea60ae6ab19adbe                     |
| Config YAML        | Override config.yaml in google/fonts                         |
| Status             | complete                                                     |
| Confidence         | HIGH                                                         |

## Investigation Details

### METADATA.pb Current State

The METADATA.pb already has a complete `source { }` block:

```
source {
  repository_url: "https://github.com/TypeNetwork/Arimo"
  commit: "77fdf7e032ef18c5ad72929bdea60ae6ab19adbe"
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  files {
    source_file: "fonts/ttf/Arimo-Bold.ttf"
    dest_file: "static/Arimo-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-BoldItalic.ttf"
    dest_file: "static/Arimo-BoldItalic.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-Italic.ttf"
    dest_file: "static/Arimo-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-Regular.ttf"
    dest_file: "static/Arimo-Regular.ttf"
  }
  files {
    source_file: "fonts/vf/Arimo-Italic[wght].ttf"
    dest_file: "Arimo-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/vf/Arimo[wght].ttf"
    dest_file: "Arimo[wght].ttf"
  }
  branch: "master"
}
```

The commit hash was added by Felipe Sanches on 2025-11-07 (commit `44832ef89`) along with an override config.yaml.

### Binary File History in google/fonts

Key commits modifying the arimo directory:

1. **Initial commit** (`90abd17b4`, 2015-03-07): Original static fonts
2. **Hotfix PR #764** (`5e49edbd1`): v1.231 added
3. **PR #2713** (`7252eca1f`, 2020-10-07): Version 1.33, variable font upgrade by Marc Foley using gftools-packager. Removed static-only TTFs and added variable font files `Arimo[wght].ttf` and `Arimo-Italic[wght].ttf`.
4. **Sources info** (`44832ef89`, 2025-11-07): Added commit hash and override config.yaml

### PR #2713 Analysis

The commit message explicitly states:
> "Arimo Version 1.33 taken from the upstream repo https://github.com/TypeNetwork/Arimo at commit https://github.com/TypeNetwork/Arimo/commit/77fdf7e032ef18c5ad72929bdea60ae6ab19adbe."

This was a gftools-packager operation. The binary files in google/fonts were copied directly from the upstream repo's `fonts/vf/` and `fonts/ttf/` directories at that commit. The static font directory was also populated from the same commit.

### Upstream Repository: TypeNetwork/Arimo

- **URL**: https://github.com/TypeNetwork/Arimo (now redirects to davelab6/Arimo)
- **Cached at**: upstream_repos/fontc_crater_cache/TypeNetwork/Arimo
- **Branch**: master (9 branches total)
- **Total commits**: 76

The repository contains proper font development sources:
- `sources/Arimo.designspace` and `sources/Arimo-Italic.designspace`
- UFO masters: `sources/Arimo-Regular.ufo`, `sources/Arimo-Bold.ufo`, `sources/Arimo-Italic.ufo`, `sources/Arimo-BoldItalic.ufo`
- Original .glyphs files under `sources/originals/`
- Pre-built fonts in `fonts/vf/` and `fonts/ttf/`
- Build script: `sources/build.sh`

### Commit Hash Verification

Commit `77fdf7e0` ("Add /nbspace and new build", 2020-08-29) is verified in the cached repo. It was authored by Jill Pichotta (TypeNetwork). The commit modified the built font files and added instance UFOs. The merge date of PR #2713 (2020-10-07) is about 5 weeks after this commit date, which is a reasonable timeline for the packager workflow.

After commit `77fdf7e0`, there are only 2 more commits on master:
- `88a56012` (2020-10-28): Update Pillow version in requirements.txt
- `a91b935c` (2020-10-28): Merge PR #24

These later commits only touched `requirements.txt` and did not affect sources or binaries, confirming `77fdf7e0` is the correct onboarding commit.

### Repository URL Note

The METADATA.pb lists `https://github.com/TypeNetwork/Arimo`, but the repo has since been transferred and now redirects to `https://github.com/davelab6/Arimo`. There is also a separate `https://github.com/googlefonts/Arimo` repo (not a fork of TypeNetwork/Arimo). The copyright string in the font references `https://github.com/googlefonts/arimo`. The current METADATA.pb URL still works via GitHub's redirect, so no change is strictly necessary, but updating to the current owner could be considered.

### Config YAML

An override `config.yaml` already exists at `apache/arimo/config.yaml` in google/fonts:

```yaml
buildVariable: true
sources:
  - sources/Arimo.designspace
  - sources/Arimo-Italic.designspace
```

This correctly references the designspace files present in the upstream repo at commit `77fdf7e0`. The upstream repo does not contain its own config.yaml.

## Conclusion

### Current METADATA.pb Source Block (Already Complete)

```
source {
  repository_url: "https://github.com/TypeNetwork/Arimo"
  commit: "77fdf7e032ef18c5ad72929bdea60ae6ab19adbe"
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  files {
    source_file: "fonts/ttf/Arimo-Bold.ttf"
    dest_file: "static/Arimo-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-BoldItalic.ttf"
    dest_file: "static/Arimo-BoldItalic.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-Italic.ttf"
    dest_file: "static/Arimo-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-Regular.ttf"
    dest_file: "static/Arimo-Regular.ttf"
  }
  files {
    source_file: "fonts/vf/Arimo-Italic[wght].ttf"
    dest_file: "Arimo-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/vf/Arimo[wght].ttf"
    dest_file: "Arimo[wght].ttf"
  }
  branch: "master"
}
```

### Notes

- Status: **complete** - The source block has repository_url, commit hash, file mappings, and branch. An override config.yaml exists in google/fonts.
- The repository URL `TypeNetwork/Arimo` now redirects to `davelab6/Arimo`. The font copyright references `googlefonts/arimo`, which is a separate repository. This URL discrepancy is cosmetic since GitHub redirects work, but could be noted for future cleanup.
- Confidence is HIGH because the commit hash is explicitly documented in PR #2713, verified in the cached repo, and confirmed as the correct onboarding source for the currently shipped binaries.
- No changes needed -- the METADATA.pb source block and override config.yaml are already in place and correct.
