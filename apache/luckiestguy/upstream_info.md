# Luckiest Guy -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only basic metadata:

```
name: "Luckiest Guy"
designer: "Astigmatic"
license: "APACHE2"
category: "DISPLAY"
date_added: "2011-01-06"
fonts {
  name: "Luckiest Guy"
  style: "normal"
  weight: 400
  filename: "LuckiestGuy-Regular.ttf"
  post_script_name: "LuckiestGuy-Regular"
  full_name: "Luckiest Guy Regular"
  copyright: "Copyright (c) 2010 by Brian J. Bonislawsky DBA Astigmatic (AOETI). All rights reserved. Available under the Apache 2.0 licence. http://www.apache.org/licenses/LICENSE-2.0.html"
}
subsets: "latin"
subsets: "menu"
classifications: "DISPLAY"
classifications: "HANDWRITING"
```

## Repository Analysis

### Upstream Repository: librefonts/luckiestguy

- **URL**: https://github.com/librefonts/luckiestguy
- **Organization**: librefonts (a legacy org for libre font sources)
- **Created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **License**: Apache 2.0
- **Total commits**: 1 (a single commit: `0dcbedf` from 2014-10-17 by hash3g, "update .travis.yml")
- **Archived**: No
- **Stars**: 0

### Repository Structure

The repository contained decomposed TTX files (individual OpenType table dumps) and a FontLab VFB source:

```
src/
  LuckiestGuy.vfb          (FontLab binary source, 186 KB)
  METADATA_comments.txt     (empty comments)
  VERSIONS.txt              ("LuckiestGuy.ttf: Version 1.000")
LuckiestGuy.ttf.*.ttx      (decomposed TTX table dumps)
METADATA.json               (old-style metadata)
.travis.yml                 (Travis CI build config using fontbakery-build.py)
COPYRIGHT.txt
LICENSE.txt
DESCRIPTION.en_us.html
```

### Source File Analysis

- **Only source**: `src/LuckiestGuy.vfb` -- a FontLab Studio binary format file
- **No `.glyphs`, `.ufo`, or `.designspace` files** -- the sources are not gftools-builder compatible
- **No `config.yaml`** in the repository
- The TTX files represent Version 1.000 of the font (created 2010-12-21, modified 2010-12-23)
- The `.travis.yml` used the legacy `fontbakery-build.py` pipeline, not modern gftools-builder

### Version Discrepancy

- The upstream repo sources correspond to **Version 1.000** of the font
- The font binary currently in google/fonts is **Version 1.001**
- This means the current binary was not produced from the librefonts repo sources

## Onboarding History

### Initial Addition

The font was part of the initial commit to the google/fonts repository:
- **Commit**: `90abd17b` (2015-03-07) by Dave Crossland -- "Initial commit"
- **Date added**: 2011-01-06 (per METADATA.pb; the 2015 commit was when the repo was migrated to GitHub)
- The original font file was named `LuckiestGuy.ttf`

### Hotfix Update (PR #780)

The font was updated in PR #780:
- **Commit**: `9a93667` (2017-08-07)
- **Author**: Marc Foley (m4rc1e)
- **Merged by**: Dave Crossland (davelab6)
- **Title**: "hotfix-luckiestguy: v1.001 added"
- **PR body**: Empty (no description provided)
- **Changes**:
  1. Renamed `LuckiestGuy.ttf` to `LuckiestGuy-Regular.ttf`
  2. Updated the binary from Version 1.000 to Version 1.001
  3. Updated METADATA.pb to reflect the new filename
  4. Rewrote DESCRIPTION.en_us.html

The v1.001 binary was likely produced by Marc Foley as part of the hotfix process, but the upstream librefonts repo was never updated to reflect this version. The PR body was empty, so there is no record of how the v1.001 binary was produced or what changes it included beyond the version bump and filename rename.

## Build Configuration

- **No `config.yaml`** exists in the upstream repository
- **No override `config.yaml`** exists in the google/fonts family directory
- The upstream sources are **VFB-only** (FontLab binary format), which is not compatible with gftools-builder
- The legacy `.travis.yml` used `fontbakery-build.py`, a now-deprecated build system
- **Creating an override config.yaml is not feasible** because gftools-builder cannot process VFB files

## Findings

1. **No source block in METADATA.pb**: The font lacks any source metadata linking it to an upstream repository.

2. **Legacy VFB-only sources**: The upstream repo at `librefonts/luckiestguy` contains only a FontLab VFB source file. This format is not supported by gftools-builder or fontc. There are no `.glyphs`, `.ufo`, or `.designspace` source files that could be used with modern build tools.

3. **Version mismatch**: The upstream repo has Version 1.000 sources, but google/fonts serves Version 1.001. The v1.001 binary was produced in PR #780 by Marc Foley, but the upstream repo was never updated. The origin of the v1.001 binary is undocumented.

4. **Stale repository**: The `librefonts/luckiestguy` repo has only one commit from October 2014 and has not been updated since. It appears to be an automated decomposition of the original font, not actively maintained.

5. **No config.yaml possible**: Since the only source format is VFB, no gftools-builder config.yaml can be created. The font would need source conversion (VFB to UFO or Glyphs) before it could be built with modern tools.

6. **Designer**: Brian J. Bonislawsky, operating as Astigmatic (AOETI). Designer website: http://www.astigmatic.com/

## Recommended Source Block

A source block can be added pointing to the librefonts repo, but it will be incomplete due to the VFB-only sources and version mismatch:

```
source {
  repository_url: "https://github.com/librefonts/luckiestguy"
  commit: "0dcbedfc1b04831080433870e6e1e2c665e75800"
}
```

**Caveats**:
- The commit `0dcbedf` is the only commit in the repo and corresponds to Version 1.000 sources, not the Version 1.001 binary currently served
- No `config_yaml` can be specified because the VFB format is not gftools-builder compatible
- The source block documents the known upstream repo but does not fully describe how the current binary was produced
- Status would be `missing_config` since no build configuration is possible with VFB sources

**Open question**: Where did the Version 1.001 binary come from? Marc Foley (m4rc1e) may know, as he authored PR #780 in August 2017. The VFB source may have been compiled locally with FontLab and post-processed.
