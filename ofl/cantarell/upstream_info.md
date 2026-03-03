# Cantarell - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cantarell |
| Designer | Dave Crossland |
| License | OFL |
| Date Added | 2010-05-10 |
| Repository URL | https://github.com/davelab6/cantarell |
| Commit Hash | 52d3363878871c868eaeb64c75a701c1193750af |
| Branch | master |
| Config YAML | Override in google/fonts |
| Status | complete |

## How URL Found

The repository URL `https://github.com/davelab6/cantarell` was added in commit f7455d788 ("Populate source.repository_url") which was a batch operation populating source blocks for many families. The davelab6/cantarell repo is the original upstream maintained by Dave Crossland himself, the designer.

Note: There is also a GNOME version of Cantarell at `https://github.com/GNOME/cantarell-fonts` (read-only mirror of https://gitlab.gnome.org/GNOME/cantarell-fonts), which is a separate, much more evolved version of the font. The Google Fonts version uses the original Dave Crossland 2009 release, not the GNOME version.

## How Commit Determined

The commit `52d3363878871c868eaeb64c75a701c1193750af` is the HEAD (and latest) commit of the davelab6/cantarell repository, dated 2013-12-02. This commit ("Add original copyright and OFL.txt") is one of only two commits in the repo:

1. `7e7b962` (2013-12-02) - "Import original Dave Crossland release from 2009" - added 5 SFD source files
2. `52d3363` (2013-12-02) - "Add original copyright and OFL.txt" - added license file

The commit hash was added in commit ad48b604a ("sources info for Cantarell: Version 1.004 (PR #5213)") on 2025-11-19 by Felipe Sanches. This same commit also added the override config.yaml file to google/fonts.

## Config YAML Status

An override `config.yaml` exists in the google/fonts directory at `ofl/cantarell/config.yaml` with the following content:

```yaml
buildVariable: false
sources:
  - src/Cantarell-Regular.sfd
  - src/Cantarell-Regular-Spiro.sfd
  - src/Cantarell-Oblique.sfd
  - src/Cantarell-BoldOblique.sfd
  - src/Cantarell-Bold.sfd
```

This config references all 5 SFD source files from the upstream repository. Since the override config exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

No `config.yaml` exists in the upstream repository itself.

## Verification

- **Commit hash verified**: The hash `52d3363` exists in the davelab6/cantarell repository and is HEAD of master. CONFIRMED.
- **Repository accessible**: davelab6/cantarell is a valid GitHub repository. CONFIRMED.
- **Source files**: 5 SFD files in `src/` directory matching the override config.yaml.
- **Override config**: Present in google/fonts at `ofl/cantarell/config.yaml`. CONFIRMED.
- **Font history**: The font has been through multiple hotfixes in google/fonts:
  - PR #5010 (e29d904ec) - Name ID13 and 14 hotfix, version bumped to 1.002
  - PR #5213 (bef4d502a) - Version 1.004, extensive hotfixes (filenames, name tables, vertical metrics, weightClass)
  - These were manual hotfixes, not rebuilds from the upstream SFD sources.

## Confidence Level

**HIGH** - The repository URL, commit hash, and override config.yaml are all correct. The davelab6/cantarell repo contains the original 2009 sources that were used for the initial Google Fonts onboarding. The font has since been hotfixed multiple times in google/fonts without rebuilding from the upstream sources.

## Open Questions

- The current binary fonts in google/fonts have been extensively modified via hotfixes and may not match what would be produced by building from the SFD sources. A rebuild from the upstream sources would likely produce different output than the current binaries.
- The GNOME Cantarell project (cantarell-fonts) is a significantly different and more advanced version of this typeface, but is tracked separately.
