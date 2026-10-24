# Investigation: Libertinus Serif Display

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: missing_config
**Confidence**: HIGH

## METADATA.pb Analysis

The METADATA.pb file at `ofl/libertinusserifdisplay/METADATA.pb` contained a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/libertinus"
  commit: "63b24ea7904a0ae69b38732b50dc6ebc277f9b68"
  files {
    source_file: "documentation/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "documentation/preview.jpg"
    dest_file: "article/preview.jpg"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/LibertinusSerifDisplay-Regular.ttf"
    dest_file: "LibertinusSerifDisplay-Regular.ttf"
  }
  branch: "main"
}
```

The source block had a `repository_url`, a `commit` hash, a `branch`, and `files` mappings. No `config_yaml` field was present.

## Upstream Repository Analysis

The upstream repository `https://github.com/googlefonts/libertinus` was a Google Fonts "wrapper" repository maintained by Yanone (post@yanone.de). It was not a traditional font source repository. Instead, it served as an intermediary that downloaded pre-built binary fonts from the true upstream source at `https://github.com/alerque/libertinus`.

### Repository Structure (at commit 63b24ea)

The repository contained:
- `build.sh` - A shell script that downloaded the latest release zip from `alerque/libertinus`, extracted TTF files, applied fontspector hotfixes, and ran fontsetter post-processing
- `fontsetter/` - Directory with `.fontsetter` files for each font style, including `LibertinusSerifDisplay-Regular.fontsetter`
- `fonts/ttf/` - Pre-built TTF binaries (14 files covering all Libertinus sub-families)
- `Makefile` - Referenced `sources/config.yaml` for a gftools-builder workflow, but no `sources/` directory existed
- `scripts/read-config.py` - A config parser that expected `sources/config.yaml`, which did not exist
- `version.txt` - Contained "7.051"
- No font source files (.glyphs, .ufo, .designspace, .sfd) were present

### Build Process

The `build.sh` script followed this workflow:
1. Downloaded the latest release from `https://api.github.com/repos/alerque/libertinus/releases/latest`
2. Extracted TTF files from the release zip
3. Applied fontspector hotfixes (`fontspector -p googlefonts -l fail --hotfix`)
4. Applied fontsetter post-processing (`gftools-fontsetter`)
5. Renamed "Semibold" to "SemiBold" in font name tables

This was not a gftools-builder compilation. The fonts were pre-built binaries from `alerque/libertinus` releases, with post-processing applied.

### Git History

The repository had only 5 commits, all by Yanone:

| Hash | Date | Message |
|------|------|---------|
| d165379 | 2025-04-02 | Initial commit |
| 943f733 | 2025-04-02 | Initial commit |
| 7b49cf8 | 2025-04-03 | 7.051 publishable |
| 88dfbb0 | 2025-04-03 | Update README.md |
| 63b24ea | 2025-04-14 | Dropped two instances of "Linux" in descriptions |

The repository was clean with no local modifications.

## Commit Hash Verification

The commit hash `63b24ea7904a0ae69b38732b50dc6ebc277f9b68` in METADATA.pb was verified as the HEAD of the `main` branch (also the latest commit in the repository). This commit was dated 2025-04-14 and only modified documentation files (README.md and ARTICLE.en_us.html), dropping references to "Linux" from descriptions.

Binary file comparison confirmed the TTF files matched exactly:
- `fonts/ttf/LibertinusSerifDisplay-Regular.ttf` in the upstream repo at commit 63b24ea (733,352 bytes, MD5: 1210dbee0493a54a66605833d3646d90)
- `ofl/libertinusserifdisplay/LibertinusSerifDisplay-Regular.ttf` in google/fonts (733,352 bytes, MD5: 1210dbee0493a54a66605833d3646d90)

The commit hash was correct.

## Google Fonts PR History

The font was onboarded via PR #9353 ("Libertinus Serif Display: Version 7.051;RELEASE added"), created by Yanone on 2025-04-16 and merged by Emma Marichal on 2025-07-17.

The PR commit message explicitly stated:
> Taken from the upstream repo https://github.com/googlefonts/libertinus at commit https://github.com/googlefonts/libertinus/commit/63b24ea7904a0ae69b38732b50dc6ebc277f9b68.

The PR was labeled with:
- "I New Font"
- "II Accepted"
- "-- fontforge/fontlab/fontcreator" (indicating non-UFO/Glyphs native sources)

After the initial onboarding commit (cb60f359c), three additional commits were made on 2025-07-17 by Emma Marichal: updating the OFL.txt, updating the article and image size, and adding copyright information to METADATA.pb.

## Config.yaml Assessment

No `config.yaml` existed in the upstream repository. The Makefile referenced `sources/config.yaml` (a template artifact from the googlefonts-project-template), but no `sources/` directory existed. No override `config.yaml` was present in the google/fonts family directory either.

A gftools-builder config.yaml is not applicable for this family because:
1. The `googlefonts/libertinus` repository did not contain font source files -- it contained pre-built binaries downloaded from `alerque/libertinus` releases
2. The build process used a custom `build.sh` script (download, hotfix, fontsetter), not gftools-builder
3. The true font sources (SFD files) resided in `alerque/libertinus`, which used its own build system

## Related Families

Libertinus Serif Display was part of a larger Libertinus family group, all sharing the `googlefonts/libertinus` upstream repository:
- Libertinus Keyboard (commit 88dfbb0)
- Libertinus Math (commit 88dfbb0)
- Libertinus Mono (commit 88dfbb0)
- Libertinus Sans (commit 63b24ea)
- Libertinus Serif (commit 63b24ea)
- Libertinus Serif Display (commit 63b24ea)

Note: Some families referenced commit 88dfbb0 while others referenced 63b24ea (the latest). Both commits post-dated the "7.051 publishable" commit (7b49cf8) where the binary fonts were last updated, so the font binaries were identical regardless of which commit was referenced.

## Conclusion

The source block in METADATA.pb was correct: the repository URL and commit hash were verified. The repository URL pointed to `googlefonts/libertinus`, which was a wrapper/intermediary repo rather than a true source repo. The actual font sources (SFD files) lived in `alerque/libertinus`.

No config.yaml could be created because the repository did not contain buildable font source files. The fonts were pre-built binaries with post-processing applied via a custom build script. The status remained `missing_config` due to the absence of gftools-builder-compatible sources, but this was an inherent characteristic of the project's architecture rather than a fixable gap.
