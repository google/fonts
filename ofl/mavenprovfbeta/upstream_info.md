# Maven Pro VF Beta — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (early access, no METADATA.pb, deprecated by main Maven Pro variable font)

## METADATA.pb Source Block (current)

No METADATA.pb exists for this family. The directory `ofl/mavenprovfbeta/` contains only:
- `DESCRIPTION.en_us.html`
- `EARLY_ACCESS.category` (value: "Sans Serif")
- `MavenProVFBeta.ttf`
- `OFL.txt`

This is an early access family that was never graduated to the main catalog with a full METADATA.pb.

## Repository Analysis

### Upstream Source Repository

The source for Maven Pro VF Beta was `m4rc1e/Maven-Pro` (https://github.com/m4rc1e/Maven-Pro), which contained the `.glyphs` source at `sources/MavenPro.glyphs`. This repository was the original working repository for the Maven Pro redesign by Joe Prince, maintained by Marc Foley.

The variable font binary was **not** built directly from this repo. Instead, Marc Foley used a separate build tool repository, `m4rc1e/gfvf` (https://github.com/m4rc1e/gfvf), described as "Variable Fonts for GF" — a rough build chain for generating beta variable fonts for Google Fonts Early Access. The `gfvf` script (`generate_variable_fonts.py`) traversed source repositories, found `.glyphs` files with multiple masters, renamed the family to append "VF Beta", and generated variable fonts using `fontmake`.

### Repository Status

- **m4rc1e/Maven-Pro**: Active, not archived. Last commit: `51ae64ef` (July 4, 2017). Contains `sources/MavenPro.glyphs` but no `config.yaml`. Only has static font output in `fonts/` directory (no variable font output).
- **m4rc1e/gfvf**: Active, not archived. Created October 20, 2017. This was a build automation tool, not a font source repository.
- **m4rc1e/mavenproFont**: Created April 4, 2018 — this is the **successor** repository used for the graduated Maven Pro variable font. It has `sources/config.yaml` and is referenced in the main Maven Pro METADATA.pb.

### Relationship Between Repositories

1. `m4rc1e/Maven-Pro` — Original source repo used for the VF Beta (2016-2017)
2. `m4rc1e/gfvf` — Build tooling repo used to batch-generate VF betas (2017)
3. `m4rc1e/mavenproFont` — Successor repo for the properly released Maven Pro variable font (2018+)

## Onboarding History

### Initial Onboarding (March 29, 2017)

- **Commit**: `50153d0f379c50b09b469288234a8bde8778a15f`
- **Author**: Marc Foley (m.foley.88@gmail.com)
- **PR**: #724 — "mavenprovfbeta: added to early access."
- **Merged**: March 28, 2017
- **Context**: This was one of the first variable font betas added to Google Fonts Early Access. In the PR body, Marc Foley explained he was using the Amstelvar branch as a reference and planned to add more VF beta families once the process was validated.

The source commit in `m4rc1e/Maven-Pro` was most likely `8fbb17d8` (March 13, 2017 — "v2.002 update: fixed Turkish i"), the latest commit at the time of onboarding.

### Update (October 23, 2017)

- **Commit**: `3507365d317354387395cbfdbebe757a86130c5d`
- **Author**: Marc Foley
- **Message**: "Variable beta font update. Uploading variable fonts which can be generated from M Foley's machine. Built using https://github.com/m4rc1e/gfvf"
- **Context**: This was a batch update to multiple VF beta families (Archivo, Asap, Cabin, Faustina, Maven Pro, Podkova). The font binary was regenerated using the gfvf build tool.

The source commit in `m4rc1e/Maven-Pro` for this update was most likely `51ae64ef` (July 4, 2017 — "Merge pull request #3 from m4rc1e/mm-collisions"), which was the latest commit at the time of the October 2017 update.

## Build Configuration

- **No config.yaml** exists in the `m4rc1e/Maven-Pro` repository.
- The VF Beta was built using the `m4rc1e/gfvf` build tool, which used `fontmake` directly via command line (`fontmake -g <source> -o variable`), not gftools-builder.
- The source file was `sources/MavenPro.glyphs` in the Maven-Pro repository.
- The gfvf script renamed the family from "Maven Pro" to "Maven Pro VF Beta" before building.

## Findings

1. **Deprecated family**: Maven Pro VF Beta was an experimental early access variable font from 2017. The main Maven Pro family (`ofl/mavenpro/`) has since been properly released as a variable font with a full METADATA.pb and source block pointing to `m4rc1e/mavenproFont`. The VF Beta is effectively superseded and obsolete.

2. **No METADATA.pb**: This early access family never had a METADATA.pb file, only an `EARLY_ACCESS.category` file.

3. **Unconventional build process**: The VF Beta was generated using a custom Python script (`m4rc1e/gfvf`) that batch-processed `.glyphs` sources with `fontmake`, not using the standard gftools-builder pipeline. This means no `config.yaml` was ever applicable for this family.

4. **Source repository mismatch**: The actual font design source was in `m4rc1e/Maven-Pro`, but the build tooling was in `m4rc1e/gfvf`. Neither repository was set up for standard gftools-builder workflows.

5. **Two relevant source commits**:
   - First onboarding: `8fbb17d8` from `m4rc1e/Maven-Pro` (March 13, 2017)
   - Final update: `51ae64ef` from `m4rc1e/Maven-Pro` (July 4, 2017)

6. **OFL copyright**: References `http://www.vissol.co.uk/mavenpro/` (Joe Prince's website), not a GitHub repository.

## Recommended Source Block

Given that this is a deprecated early access family with no METADATA.pb and no standard build configuration, adding a source block is of very low priority. If one were to be added, it would look like:

```
source {
  repository_url: "https://github.com/m4rc1e/Maven-Pro"
  commit: "51ae64ef0eb6ef250f10f71b28b0d4ad2c24b8c7"
}
```

However, the recommended action is to **not prioritize this family** for source metadata enrichment because:
- It is an early access VF beta that has been superseded by the graduated Maven Pro variable font
- It has no METADATA.pb and no standard build pipeline
- The main Maven Pro family (`ofl/mavenpro/`) already has complete source metadata pointing to the successor repository `m4rc1e/mavenproFont`
- Creating a METADATA.pb for this family would require broader decisions about the status of early access VF beta families in general
