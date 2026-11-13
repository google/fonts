# Google Sans Flex: upstream source metadata

**Model**: Claude Fable 5.2

## Initial state

- `ofl/googlesansflex/METADATA.pb` had no source block. The family directory had no override `config.yaml` and no `upstream_info.md`.
- The font was last changed in google/fonts commit bd8f81ddb ("Adding latest GSF v5.000 (#11097)", Marianna Paszkowska, 2026-10-10), which removed the GRAD axis and renamed the file to `GoogleSansFlex[ROND,opsz,slnt,wdth,wght].ttf`.

## Actions taken

- Found the release: https://github.com/googlefonts/googlesans-flex/releases/tag/v5.000 (published 2026-10-09). The shipped font is byte-identical to `GoogleSansFlex[ROND,opsz,slnt,wdth,wght].ttf` in its `GoogleSansFlex-v5.000.zip`.
- The tag v5.000 is commit [cedf1e9c](https://github.com/googlefonts/googlesans-flex/commit/cedf1e9cef08ddf33d711dd259601ea3017b7cd4) ("Merge pull request #1330 from googlefonts/release-5.000-prep", 2026-10-09), on `main`.
- The gftools-builder configuration at that commit is `sources/config.yaml`. It builds `sources/GoogleSansFlex.glyphspackage` with a `recipe` that drops the GRAD axis. I did not build it.
- Added the source block: repository, commit, `archive_url`, the file mapping from the archive, branch `main` and `config_yaml`.

## Final state

- The source block records googlefonts/googlesans-flex at the v5.000 tag commit, the release archive the font came from, and `config_yaml: "sources/config.yaml"`.
