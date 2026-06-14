# Libertinus Keyboard - Investigation Report

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (binary-only sources, no config.yaml applicable)
**Confidence**: HIGH

## Summary

Libertinus Keyboard is a display font that was onboarded to Google Fonts via PR #9301 on 2025-04-03, created by Yanone and merged by Emma Marichal on 2025-07-17. The upstream repository at `https://github.com/googlefonts/libertinus` is not a traditional font source repo -- it is a Google-Fonts-centered working repository that downloads pre-built binary TTF files from the real upstream project at `https://github.com/alerque/libertinus`, hotfixes them for Google Fonts compliance, and applies fontsetter metadata adjustments. There are no buildable font source files (.glyphs, .ufo, .designspace) in this repository.

## METADATA.pb Analysis

The existing source block in METADATA.pb was:

```
source {
  repository_url: "https://github.com/googlefonts/libertinus"
  commit: "88dfbb0a7715817a43499e613fc8e6645174cd6a"
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
    source_file: "fonts/ttf/LibertinusKeyboard-Regular.ttf"
    dest_file: "LibertinusKeyboard-Regular.ttf"
  }
  branch: "main"
}
```

The source block was present since the initial onboarding. No `config_yaml` field is set.

## Upstream Repository Analysis

**Repository**: `https://github.com/googlefonts/libertinus`
**Nature**: Google-Fonts-centered binary working repository (NOT original font sources)
**Real upstream**: `https://github.com/alerque/libertinus`

The README.md explicitly states:

> This repository is not a fork, but a Google-Fonts-centered working repository, of the popular https://github.com/alerque/libertinus font family.

The build process (`build.sh`) works as follows:
1. Downloads the latest release ZIP from `https://github.com/alerque/libertinus`
2. Extracts static TTF binaries from the release
3. Applies `fontspector` hotfixes for Google Fonts compliance
4. Applies `gftools-fontsetter` metadata adjustments using `.fontsetter` files

There are no font source files (.glyphs, .ufo, .designspace, .sfd) in this repository. The Makefile references `sources/config.yaml`, but this was a remnant from the googlefonts-project-template. The `sources/` directory (which contained Radio Canada Display files from the template) was removed in the second "Initial commit" (943f733).

### Commit History (complete)

| Hash | Date | Author | Message |
|------|------|--------|---------|
| d165379 | 2025-04-02 | Yanone | Initial commit (from template, with Radio Canada Display sources) |
| 943f733 | 2025-04-02 | Yanone | Initial commit (replaced template with Libertinus binaries and build.sh) |
| 7b49cf8 | 2025-04-03 | Yanone | 7.051 publishable (documentation, OFL updates) |
| 88dfbb0 | 2025-04-03 | Yanone | Update README.md |
| 63b24ea | 2025-04-14 | Yanone | Dropped two instances of "Linux" in descriptions |

## Commit Hash Verification

The METADATA.pb references commit `88dfbb0a7715817a43499e613fc8e6645174cd6a` ("Update README.md", 2025-04-03). This was the latest commit at the time PR #9301 was created (also 2025-04-03).

The PR commit message explicitly states: "Taken from the upstream repo https://github.com/googlefonts/libertinus at commit https://github.com/googlefonts/libertinus/commit/88dfbb0a7715817a43499e613fc8e6645174cd6a."

The font binary at commit 88dfbb0 was 204,448 bytes. However, the current font in google/fonts is 204,456 bytes due to a hotfix applied by Emma Marichal directly in the PR branch on 2025-07-17 ("hotfixed font, adds nbspace"). This hotfix was requested by Marc Camelot (m4rc1e) to add a uni00A0 (nbspace) glyph. Yanone confirmed in the PR comments that he did not have access to the actual font sources, only hotfixing binaries.

**The commit hash 88dfbb0 is correct as the original onboarding reference**, though the final published binary includes the nbspace hotfix applied in the google/fonts PR branch.

Note: One additional commit was made to the upstream repo after the PR was created (63b24ea on 2025-04-14, "Dropped two instances of 'Linux' in descriptions"), but this only affected README.md and ARTICLE.en_us.html, not the font binary.

## config.yaml Assessment

**No config.yaml is applicable.** This repository does not use gftools-builder. The build process uses a custom `build.sh` script that:
- Downloads pre-built binaries from alerque/libertinus releases
- Hotfixes them with `fontspector`
- Applies metadata adjustments with `gftools-fontsetter`

The `sources/config.yaml` that existed in the first template-based commit (d165379) was for Radio Canada Display and was correctly removed in the second commit (943f733).

Since there are no buildable source files in this repository, a config.yaml (neither in the upstream repo nor as an override in google/fonts) would serve no purpose.

## google/fonts PR History

**PR #9301**: "Libertinus Keyboard: Version 7.051;RELEASE added"
- Created: 2025-04-03 by Yanone (@yanone)
- Merged: 2025-07-17 by Emma Marichal (@emmamarichal)
- Resolves: issue #12 in the google/fonts repo

### Commits in google/fonts for this family:

| Hash | Date | Author | Message |
|------|------|--------|---------|
| 0f2c04f58 | 2025-04-03 | Yanone | Libertinus Keyboard: Version 7.051;RELEASE added |
| 5e157b2e9 | 2025-07-17 | Emma Marichal | fix article and image size |
| cb9d5f7b1 | 2025-07-17 | Emma Marichal | update metadata.pb (copyright) |
| 410861ba1 | 2025-07-17 | Emma Marichal | update ofl.txt |
| c265797d4 | 2025-07-17 | Emma Marichal | hotfixed font, adds nbspace |

## Conclusion

The source block in METADATA.pb is already complete and correct:
- **repository_url**: `https://github.com/googlefonts/libertinus` -- correct (this is the Google Fonts working repo)
- **commit**: `88dfbb0a7715817a43499e613fc8e6645174cd6a` -- correct (the commit used at onboarding time)
- **branch**: `main` -- correct
- **config_yaml**: correctly omitted (no gftools-builder configuration is applicable)
- **files mappings**: correctly map font binary, article, preview, and license

No changes are needed. The status is "complete" with the understanding that this is a binary-only distribution with no buildable sources. The lack of a config.yaml is expected and correct for this type of repository.
