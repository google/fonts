# 🔍 Live Repository Verification Report: `Abhaya Libre`

**Generated:** `2026-07-16 17:56:16 UTC`
**PR Submission Mode:** `DISABLED (Report / Verification Mode)` 🛑

## 📁 Font File Matching Identification

- **Overall Matching Status:** `PARTIAL_MATCH`
- **Local TTF Count (in google/fonts):** `5`
- **Upstream Candidate TTF Count:** `1`
- **Filename Match Rate:** `20.0%`
- **Binary Hash Differences Detected:** `YES (Updated Binary Content)`

### 📑 Detailed Font File Mapping & Hash Table

| Local Font Filename | Candidate Upstream Filename | Match Strategy | Binary Hash Status |
| :--- | :--- | :--- | :--- |
| `AbhayaLibre-Regular.ttf` | `AbhayaLibre[wght].ttf` | `MAPPED_NAME` | 🔴 Changed / Updated |

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

---
## 📝 Simulated PR Description & Checklist Preview

## 🤖 Automated Upstream Font Update: `Abhaya Libre`

### 📊 Safe to Update (STU) Score: `54.65 / 100`
**Decision Tier:** 🔴 **BLOCKED** (Regression Detected)

### 💡 Concise Scoring Rationale
- **Decision Tier:** 🔴 **BLOCKED** (Regression Detected) (Score `54.65 / 100`)
- **Max Vertical Metric Shift:** `20` font units (⚠️ exceeds 10 unit threshold)
- **Advance Width Max Shift:** `19.66%` (⚠️ exceeds 5% threshold)
- **Deleted Unicodes:** `1` (❌ CRITICAL BREAKING CHANGE)
- **New QA Regressions:** 🔴 `0` Fatal | 🔴 `0` Error | 🟡 `3` Warn

#### ⚠️ Detailed Rationale & Warning Items:
- Vertical metric shift of 20 units exceeds threshold (10 units)
- Advance width shift of 19.7% exceeds 5% threshold
- CRITICAL BREAKING CHANGE: Deleted 1 existing Unicode character(s)

### 🕒 Version & Timestamp Comparison
| Property | Local Installed (GF) | Upstream Candidate | Status |
| :--- | :--- | :--- | :--- |
| **Font Version String** | `Version 1.050 ; ttfautohint (v1.6)` | `2.000` | 🆕 Update Available |
| **Numerical Version** | `1.050` | `2.000` | `UPDATE_AVAILABLE` |
| **Commit / Mod Date** | `2026-05-21T23:03:22+01:00` | `2025-03-27T18:29:50Z` | 📅 Upstream Newer |

### 📈 Score Breakdown
| Component | Weight | Tool | Sub-Score | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Visual Diff ($S_{visual}$)** | 35% | `diffenator2` | `100.0 / 100` | ✅ Pass |
| **Metrics & Layout ($S_{metric}$)** | 25% | `diffenator2` | `30.0 / 100` | ⚠️ Metric Shift |
| **Glyph Set Retention ($S_{cmap}$)** | 25% | `diffenator2` / `fontTools` | `0.0 / 100` | ❌ Deleted Glyphs |
| **QA Checks ($S_{qa}$)** | 15% | `Fontspector` | `81.0 / 100` | ⚠️ QA Issues |

### 🔍 `diffenator2` Primary Regression Summary
- **Visual Specimen Shift:** `0.00%` pixel difference
- **Max Vertical Metric Shift:** `20` font units
- **Advance Width Max Shift:** `19.66%`
- **Deleted Unicodes:** `1` | **Added Unicodes:** `109`

### 📋 `Fontspector` QA Check Delta
- **Candidate Totals:** FATAL: `0` | ERROR: `3` | WARN: `15` | PASS: `105`
- **New Regressions:** 🔴 `0` Fatal | 🔴 `0` Error | 🟡 `3` Warn
- **Pre-existing Known Failures:** 🟡 `15` (Present in baseline installed font)
- **Resolved / Fixed Failures:** 🟢 `23` (Failed in baseline, now passing!)

#### 🔴 New QA Regressions Introduced:
- `contour_count` (WARN): *Baseline was PASS*
- `interpolation_issues` (WARN): *Baseline was SKIP*
- `mandatory_avar_table` (WARN): *Baseline was SKIP*

#### 🟡 Pre-existing Known Failures (Inherited from Baseline):
- `googlefonts/glyph_coverage` (FAIL)
- `googlefonts/glyphsets/shape_languages` (FAIL)
- `googlefonts/meta/script_lang_tags` (WARN)
- `googlefonts/metadata/unreachable_subsetting` (WARN)
- `googlefonts/separator_glyphs` (WARN)
- `googlefonts/vendor_id` (WARN)
- `googlefonts/vertical_metrics` (FAIL)
- `math_signs_width` (WARN)
- `opentype/GDEF_mark_chars` (WARN)
- `opentype/GDEF_non_mark_chars` (WARN)

### 🔗 Upstream Source Metadata
- **Upstream Repository:** https://github.com/mooniak/abhaya-libre-font
- **Upstream Version Tag:** `2.000`
- **Upstream Commit Hash:** `ccbd1336a66ca051920d417b546517bf3a3b8ada`

---
*Generated automatically by Google Fonts Automated Upstream Update System (GFAU)*