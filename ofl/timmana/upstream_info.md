**Model**: Claude Opus 4.6

## Timmana

**Designer**: Appaji Ambarisha Darbha

### Upstream Repository

The canonical upstream repository was found at **https://github.com/appajid/timmana**, maintained by Appaji Ambarisha Darbha (GitHub: appajid). The repository description reads "Timmana Telugu Unicode font for headings, banners etc." The DESCRIPTION.en_us.html in the Google Fonts repo explicitly linked to this repository.

The repository contained the following files at the investigated commit:
- `TimmanaRegular.ufo` — UFO source file
- `TimmanaRegular.vfb` — FontLab source file (legacy)
- `OFL.txt` — license

The presence of the UFO source confirmed this as an eligible upstream with modern, editable sources.

### Investigated Commit

- **Repo**: https://github.com/appajid/timmana
- **Branch**: master
- **Commit**: `6ed6823a73b42a541885d12a7df389d3112a9380`
- **Date**: 2014-12-15
- **Message**: "Timmana Telugu Unicode font — Timmana Telugu Unicode font for headings, banners etc."

The commit hash was verified via the GitHub API (`gh api repos/appajid/timmana/commits/master`).

### Status

Source block was added to `METADATA.pb` pointing to the above repository and commit.

### Notes

A secondary repository at `davelab6/timmana` was also found, but it contained only TTX (compiled XML) files and a bakery.yaml, with no editable source files. It was therefore skipped in favor of the canonical upstream.
