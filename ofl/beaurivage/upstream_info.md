# Investigation Report: Beau Rivage

**Family Name:** Beau Rivage
**Slug:** beaurivage
**Family Directory:** ofl/beaurivage
**Date Added:** 2022-02-17
**Designer:** Robert Leuschke
**Category:** HANDWRITING
**Investigated:** 2026-03-03
**Model:** Claude Opus 4.6

---

## Summary

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/beau-rivage |
| Commit Hash | `a80b72a03f6ea0a5667c58620973efdb72384ffa` |
| Config Path | `sources/config.yml` |
| Status | **complete** |
| Confidence | **HIGH** |

---

## Investigation Details

### METADATA.pb Review

The existing METADATA.pb already contained a complete `source { }` block with:
- `repository_url: "https://github.com/googlefonts/beau-rivage"`
- `commit: "a80b72a03f6ea0a5667c58620973efdb72384ffa"`
- `branch: "main"`
- `config_yaml: "sources/config.yml"`
- Three `files` entries mapping OFL.txt, DESCRIPTION.en_us.html, and the font binary

### Repository Verification

The upstream repository at `https://github.com/googlefonts/beau-rivage` was verified in the local cache at `upstream_repos/fontc_crater_cache/googlefonts/beau-rivage`. The remote URL matched the METADATA.pb `repository_url`.

The repository contained exactly **one commit** (`a80b72a`), authored by Viviana Monsalve on 2022-02-17. This was the initial (and only) commit, with the message "description moved to documentation dir". Since there was only one commit in the entire repository, the referenced commit was trivially the correct one.

### Commit Verification

The commit hash `a80b72a03f6ea0a5667c58620973efdb72384ffa` was verified as the sole commit in the upstream repository. Cross-verification was performed by comparing the binary font file:

- **SHA-256 of `ofl/beaurivage/BeauRivage-Regular.ttf`** in google/fonts: `6a407ad2418a5e29ceb447de49fb11e614615de4943292e3862347fa010e7bba`
- **SHA-256 of `fonts/ttf/BeauRivage-Regular.ttf`** in upstream at `a80b72a`: `6a407ad2418a5e29ceb447de49fb11e614615de4943292e3862347fa010e7bba`

The files were **identical**, confirming this was the correct commit.

### Onboarding History

The font was onboarded to google/fonts via PR #4323, committed on 2022-02-23 by Viviana Monsalve. The commit message explicitly stated:

> Beau Rivage Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/beau-rivage at commit https://github.com/googlefonts/beau-rivage/commit/a80b72a03f6ea0a5667c58620973efdb72384ffa

This confirmed the commit hash and repository URL used during onboarding via gftools-packager.

### Config File Verification

The upstream repository contained `sources/config.yml` at the referenced commit:

```yaml
sources:
  - BeauRivage-Pro.glyphs
familyName: "Beau Rivage"
buildVariable: false
# autohintTTF: false
```

This was a valid gftools-builder configuration referencing the `.glyphs` source file. The METADATA.pb correctly pointed to this file with `config_yaml: "sources/config.yml"`.

Note: The file used the `.yml` extension rather than `.yaml`, but this was correctly reflected in the METADATA.pb `config_yaml` field.

### Source Files

The upstream repository contained the following source file at the referenced commit:
- `sources/BeauRivage-Pro.glyphs` (1.7 MB Glyphs source)

---

## Conclusion

All source metadata for Beau Rivage was already complete and correct in METADATA.pb. The repository URL, commit hash, and config path were all verified. The binary font file in google/fonts was identical to the one in the upstream repository at the referenced commit. No changes were needed.
