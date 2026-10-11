# Bacasime Antique

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete
- **Designer**: The DocRepair Project, Claus Eggers Sørensen

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| Repository URL   | https://github.com/docrepair-fonts/bacasime-antique-fonts          |
| Commit           | `673db74ee28486bb370847e062a97a5f94cec2e0`                         |
| Branch           | main                                                               |
| Config YAML      | `sources/config.yaml`                                              |
| Date Added       | 2023-06-14                                                         |

## Repository URL Verification

The repository URL `https://github.com/docrepair-fonts/bacasime-antique-fonts` was confirmed valid. The cached clone at `docrepair-fonts/bacasime-antique-fonts` had its remote set to the same URL. The repository contained gftools-builder compatible sources (`.designspace` + `.ufo`), a `config.yaml`, and a `packager.yaml` consistent with automated onboarding via gftools-packager.

## Commit Verification

The referenced commit `673db74ee28486bb370847e062a97a5f94cec2e0` was verified to exist in the upstream repository. It was a merge commit authored by Yanone (`post@yanone.de`) on 2023-06-14 17:50:05 +0200, titled "Merge branch 'main' of https://github.com/docrepair-fonts/bacasime-antique-fonts". This was a large initial commit introducing all project files (314 files, including sources, build configs, fonts, and documentation).

The google/fonts onboarding commit `068ca5cdc` was created by gftools-packager on the same day (2023-06-14 17:50:31 +0200), with the body explicitly referencing this upstream commit:

> Bacasime Antique Version 2.000 taken from the upstream repo https://github.com/docrepair-fonts/bacasime-antique-fonts at commit https://github.com/docrepair-fonts/bacasime-antique-fonts/commit/673db74ee28486bb370847e062a97a5f94cec2e0.

This was merged as PR #6252 on 2023-06-15. Since the upstream repository had only this single commit (shallow clone shows only `673db74` as the sole commit on `main`), and the gftools-packager commit was created within seconds of the upstream commit, the commit hash is verified as correct with high confidence.

## Config YAML Verification

The upstream repository contained `sources/config.yaml` at the referenced commit. Its contents:

```yaml
---
buildOTF: false
buildVariable: false
familyName: Bacasime Antique
outputDir: ../fonts
sources:
  - Bacasime-Antique-Regular.designspace
```

This is a valid gftools-builder configuration that references `Bacasime-Antique-Regular.designspace`, which in turn points to `masters/BacasimeAntique-Regular.ufo`. The config builds only static TTF (OTF and variable builds are disabled), consistent with the single Regular weight present in google/fonts.

The `config_yaml: "sources/config.yaml"` field was added to METADATA.pb in commit `19cdcec59` (Batch 1/4, porting from fontc_crater targets list, 2025-03-31). No override config.yaml was needed since the upstream repo already had one.

## METADATA.pb History

The source block in METADATA.pb was built up over three commits:

1. **`068ca5cdc`** (2023-06-14): gftools-packager created the initial METADATA.pb with `repository_url` and `commit` fields.
2. **`66f91f10f`** (2024-04-03): Simon Cozens' automated "Merge upstream.yaml into METADATA.pb" added `files` mappings and `branch: "main"`.
3. **`19cdcec59`** (2025-03-31): Batch 1/4 commit added `config_yaml: "sources/config.yaml"`.

## Conclusion

All source metadata for Bacasime Antique was verified as complete and correct. The repository URL pointed to a valid upstream repo. The commit hash matched the exact commit used during gftools-packager onboarding (confirmed by commit body, matching timestamps, and the repo having only one commit). The upstream config.yaml existed at the referenced commit and was properly referenced in METADATA.pb. No corrections were needed.
