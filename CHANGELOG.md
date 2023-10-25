Below are the most important changes from each release.

### 0.4.4 (2023-Oct-25)

- Adding [ZROT] Rotation in Z custom axis by @vv-monsalve in #137
- Update z_rotation.textproto with fallback_only field by @chrissimpkins in #140
- Add test for proto wellformedness (no missing required fields) by @simoncozens in #143
- Update requirements.txt by @felipesanches in #146
- Adding [ARRR] AR Retinal Resolution custom Axis by @vv-monsalve in #141
- If we delete a name STAT was using, put it back by @simoncozens in #154

### 0.4.3 (2023-Jun-22)
  - Adding [SHRP] Sharpness custom Axis by @vv-monsalve in #121
  - Delete MUTA axis by @vv-monsalve in #124
  - Adding [YALN] Y Alignment custom Axis by @vv-monsalve in #125

### 0.4.2 (2023-Apr-14)
  - update name builders #133

### 0.4.1 (2023-Apr-13)
  - build_name_table: set bits as well #131

### 0.4.0 (2023-Mar-24)
  - #120 MORPH axis added
  - #119 VOLM axis updated
  - #118 XROT YROT updated
  - #115 FLAR axis updated
  - #97 OPSZ range increase

### 0.3.11 (2023-Jan-11)
  - Update x_rotation.textproto 05a0728
  - Update y_rotation.textproto 944a3e7
  - Add Spacing [SPAC] axis #62
  - Add Informality [INFM] axis #90
  - Add Bounce [BNCE] axis #63
  - tests/data/RobotoFlex*ttf Correct Optical Size title case 2d86d4c
  - Add Mutation [MUTA] axis #100
  - Update width.textproto #105
  - Update wonky.textproto #107
  - Also protect STAT table name IDs from the axis list #108
  - Fix ci #110

### 0.3.10 (2022-Nov-24)
  - Better issue templates (PR #94)
  - build_stat: improve elided axisvalues (PR #95)

### 0.3.9 (2022-Oct-27)
  - loosen protobuf dependency on setup.py so that it is easier to install axisregistry as a dependency of other projects (such as fontbakery) (https://github.com/googlefonts/axisregistry/commit/bb213824f9b8a6215b9b78c28f59773e0bd93515)
  - #91 Added ROND axis
  - #55 Added YROT axis
  - #55 Added XROT axis

### 0.3.8 (2022-Oct-10)
  - fix_stat do not drop nameids <= 25 (PR #88)

### 0.3.7 (2022-Oct-10)
  - build_stat: do not rm fvar axis name records (PR #87)

### 0.3.6 (2022-Oct-07)
  - Added YEAR axis (PR #53)
  - Added ELSH axis (PR #56)
  - Changed EGRD to ELGR (PR #57)
  - Added EHLT and EDPT (PR #61)
  - Added HEXP axis (PR #79)

### 0.3.5 (2022-Jul-01)
  - Move nameid25 to its own func (PR #52)

### 0.3.4 (2022-Jul-01)
  - Fix typo and ensure tox runs tests correctly (PR #50)


### 0.3.3 (2022-Jul-01)
  - Don't delete name IDs which are shared with the STAT table (PR #49)


### 0.3.2 (2022-Jun-27)
  - added _fvar_instance_collision function, which determines whether a family of fonts will have fvar instances which collide.	
  - build_vf_name_table: only use v1 name tables if fvar instances match (PR #48)


### 0.3.1 (2022-Jun-24)
  - AxisRegistry: add items method. Fixed googlefonts/gftools#576 (PR #47)


### 0.3.0 (2022-Jun-23)
  - Add name builder (PR #31)
  - Add illustrations (PRs #29, #30, #32 and #35)
  - Reduce length of parametric axis descriptions (PR #34)
  - y_transparent_descender.textproto Use depth, not height (PR #36)
  - tox: use black (PR #39)


### 0.2.0 (2022-Mar-14)
  - Remove pre-processing of fallback names and simplify API


### 0.1.1 (2022-Mar-14)
  - Fix typos on cursive and monospace axes descriptions.
  - Remove space characteres from fallback name entries of all axes. (issue #7)
  - Update `min_value` and `default_value` on **y_transparent_uppercase**.


### 0.1.0 (2022-Mar-04)
#### Release notes
  - Initial release of the `axisregistry` python module.
  - Most of the code & data was migrated from the [`fontbakery`](https://github.com/googlefonts/fontbakery/) and [`google/fonts`](https://github.com/google/fonts/) git repositories so that the GF Axis Registry data can be easily available to all our tools. The most immediate user of this module is `Font Bakery` itself, as well as `GFTools`.
  - Axis Registry definitions are still being gradualy updated on the `google/fonts` repo, on its **axisregistry/*- directory (https://github.com/google/fonts/tree/main/axisregistry) and this `axisregistry` python module will try to be kept in sync.
  - There's an ongoing plan to make this module the main place to update these definitions, avoiding data duplication and guaranteeing uniformity across tools.
