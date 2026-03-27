# Investigation: Kufam

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kufam |
| Slug | kufam |
| License Dir | ofl |
| Repository URL | https://github.com/originaltype/kufam |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/originaltype/kufam"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/VF/Kufam[wght].ttf"
    dest_file: "Kufam[wght].ttf"
  }
  files {
    source_file: "Fonts/VF/Kufam-Italic[wght].ttf"
    dest_file: "Kufam-Italic[wght].ttf"
  }
  branch: "master"
}
primary_script: "Arab"
```

## Investigation

The METADATA.pb contains `repository_url` but no `commit` or `config_yaml`. The upstream repository `originaltype/kufam` is cached at `upstream_repos/fontc_crater_cache/originaltype/kufam`.

The font was onboarded on July 22, 2020 via commit `7cc3227ee` ("Added Kufam 1.300 (#2552)"). The DESCRIPTION.en_us.html added in that commit references `github.com/originaltype/kufam`.

The upstream repository contains Glyphs source files in the `sources/` directory:
- `sources/Kufam_Arabic_Latin_Roman_Master.glyphs`
- `sources/Kufam_Latin_Italic_Master.glyphs`
- `sources/build.sh`

No `config.yaml` exists in the repository. The build uses a custom shell script (`build.sh`).

The likely onboarding commit is `49b96562` ("Merge pull request #9 from yanone/master", July 17, 2020) which was "Version 1.300 ready for Google Fonts". This is the latest upstream commit before the Google Fonts onboarding date of July 22, 2020.

## Conclusion

The `commit` field needs to be added to the METADATA.pb source block. The most likely candidate is `49b96562` (the v1.300 release PR merge). The Glyphs sources exist but no `config.yaml` - an override config.yaml could be created in google/fonts. This needs further confirmation of the exact commit hash and creation of a config.yaml.

## Commit Added (MEDIUM confidence)

Commit `a2c0c9552f98295167bc33bdb9c6256dd6abdc8a` was determined by **date_correlation**. Found the latest upstream commit before the binary modification date in google/fonts (2021-03-31). This assumes the upstream HEAD at onboarding time was the commit used.
