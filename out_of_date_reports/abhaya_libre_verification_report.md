# 🔍 Live Repository Verification Report: `Abhaya Libre`

**Generated:** `2026-07-17 17:03:11 UTC`
**PR Submission Mode:** `DISABLED (Report / Verification Mode)` 🛑

## 📁 Font File Matching Identification

- **Overall Matching Status:** `PARTIAL_MATCH`
- **Local TTF Count (in google/fonts):** `5`
- **Upstream Candidate TTF Count:** `1`
- **Filename Match Rate:** `20.0%`
- **Binary Hash Differences Detected:** `YES (Updated Binary Content)`
- **Manual Directive (Variable Update):** 🟢 `Approved Static-to-Variable Upgrade` (Existing static fonts should be removed and replaced with the new variable version)

### 📑 Detailed Font File Mapping, Version & Hash Table

| Local Font Filename | Candidate Upstream Filename | Catalog Version | Upstream Version | Version Comparison | Binary Hash Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AbhayaLibre-Regular.ttf` | `AbhayaLibre[wght].ttf` | `1.050` | `2.000` | 🟢 Update Confirmed | 🔴 Changed / Updated |

### ⚠️ Unmatched Local Font Files (Present in GF, Missing in Upstream Candidate)
- `AbhayaLibre-Bold.ttf`
- `AbhayaLibre-ExtraBold.ttf`
- `AbhayaLibre-Medium.ttf`
- `AbhayaLibre-SemiBold.ttf`

## 📊 System Assessment & Scoring Summary

- **Update Available:** `YES`
- **Current Installed Version:** `1.050`
- **Upstream Candidate Version:** `2.000`
- **Safe to Update (STU) Score:** `54.65 / 100`
- **Decision Tier:** `BLOCKED`
- **Pipeline Status:** `PR_READY (DRY RUN)`

## 📋 Fontspector QA Test Results & Delta

- **Candidate Check Totals:** PASS: `105` | WARN: `15` | ERROR: `3` | FATAL: `0`
- **New Check Regressions Introduced:** 🔴 `0` Fatal | 🔴 `0` Error | 🟡 `3` Warn
- **Pre-existing Known Failures:** 🟡 `15` (Inherited from baseline installed font)
- **Resolved / Fixed Failures:** 🟢 `23` (Failed in baseline, now passing!)

### 🔴 New QA Check Regressions Introduced
- **`contour_count`** (WARN): Baseline was `PASS`
  > *Check regression detected*
- **`interpolation_issues`** (WARN): Baseline was `SKIP`
  > *Check regression detected*
- **`mandatory_avar_table`** (WARN): Baseline was `SKIP`
  > *Check regression detected*

### 🟡 Pre-existing Known Failures (Inherited from Baseline)
- **`googlefonts/glyph_coverage`** (FAIL)
- **`googlefonts/glyphsets/shape_languages`** (FAIL)
- **`googlefonts/meta/script_lang_tags`** (WARN)
- **`googlefonts/metadata/unreachable_subsetting`** (WARN)
- **`googlefonts/separator_glyphs`** (WARN)
- **`googlefonts/vendor_id`** (WARN)
- **`googlefonts/vertical_metrics`** (FAIL)
- **`math_signs_width`** (WARN)
- **`opentype/GDEF_mark_chars`** (WARN)
- **`opentype/GDEF_non_mark_chars`** (WARN)

