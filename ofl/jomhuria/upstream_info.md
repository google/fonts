# Investigation: Jomhuria

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jomhuria |
| Slug | jomhuria |
| License Dir | ofl |
| Repository URL | https://github.com/Tarobish/Jomhuria |
| Commit Hash | d4b8f42eaf712178802609bfbe48127bd45be9c8 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

No source block

## Investigation

The `ofl/jomhuria/` directory contains `DESCRIPTION.en_us.html`, `Jomhuria-Regular.ttf`, `METADATA.pb`, and `OFL.txt`. The METADATA.pb has no `source { }` block.

The font was added to google/fonts on 2017-05-23 via commit `9ff1e8c28` ("hotfix-jomhuria: v1.001 added (#984)"). The commit was authored by Marc Foley.

The DESCRIPTION file states: "The Jomhuria project is led by KB Studio, a type design foundry based in Los Angeles, USA. To contribute, see https://github.com/Tarobish/Jomhuria." This gives us the upstream repository URL.

The upstream repository at https://github.com/Tarobish/Jomhuria is cached at `upstream_repos/fontc_crater_cache/Tarobish/Jomhuria`. The repository has only a single commit:
- `d4b8f42` (2016-03-03): "Updated fonts"

The repo contains `Fonts/Jomhuria-Regular.ttf` and sources in the `Sources/` directory including `jomhuria-latin.ufo` and `jomhuria.sfdir` (SpeedFont/FontForge format). No config.yaml exists in the repository.

Since the upstream repo has only one commit (dated 2016-03-03), and the google/fonts addition was 2017-05-23, the only possible source commit is `d4b8f42eaf712178802609bfbe48127bd45be9c8`.

The sources include a `.ufo` file which is compatible with gftools-builder, but there is no config.yaml in the upstream repository. An override config.yaml would be needed in the google/fonts family directory.

## Conclusion

The repository URL is `https://github.com/Tarobish/Jomhuria` and the only possible commit is `d4b8f42eaf712178802609bfbe48127bd45be9c8`. No config.yaml exists upstream; an override config.yaml would need to be created in the google/fonts family directory. A source block needs to be added to METADATA.pb.
