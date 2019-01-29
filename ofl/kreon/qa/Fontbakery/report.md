## Fontbakery report

Fontbakery version: 0.6.6

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>:fire: <b>FAIL:</b> METADATA.pb: According Google Fonts standards, families should have a Regular style.</summary>

* [com.google.fonts/check/090](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/090)
* :fire: **FAIL** This family lacks a Regular (style: normal and weight: 400) as required by Google Fonts standards.

</details>
<br>
</details>
<details>
<summary><b>[6] Kreon-Roman-VF.ttf</b></summary>
<details>
<summary>:fire: <b>FAIL:</b> Checks METADATA.pb font.name field matches family name declared on the name table.</summary>

* [com.google.fonts/check/092](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/092)
* :fire: **FAIL** Unmatched family name in font: TTF has "Kreon Light" while METADATA.pb has "Kreon" [code: mismatch]

</details>
<details>
<summary>:fire: <b>FAIL:</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values?</summary>

* [com.google.fonts/check/097](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/097)
* :fire: **FAIL** METADATA.pb font filename="Kreon-Roman-VF.ttf" does not match post_script_name="Kreon-Light".

</details>
<details>
<summary>:fire: <b>FAIL:</b> METADATA.pb: Filename is set canonically?</summary>

* [com.google.fonts/check/105](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/105)
* :fire: **FAIL** METADATA.pb: filename field ("Kreon-Roman-VF.ttf") does not match canonical name "Kreon-Light.ttf".

</details>
<details>
<summary>:fire: <b>FAIL:</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table?</summary>

* [com.google.fonts/check/108](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/108)
* :fire: **FAIL** METADATA.pb Family name "Kreon") does not match name table entry "Kreon Light" ! [code: familyname-mismatch]

</details>
<details>
<summary>:fire: <b>FAIL:</b> Checking OS/2 usWeightClass matches weight specified at METADATA.pb.</summary>

* [com.google.fonts/check/112](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/112)
* :fire: **FAIL** OS/2 usWeightClass (400:"Regular") does not match weight specified at METADATA.pb (300:"Light").

</details>
<details>
<summary>:warning: <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/116](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/116)
* :warning: **WARN** Even though unitsPerEm (1000) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will liely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations.

</details>
<br>
</details>

### Summary

| :broken_heart: ERROR | :fire: FAIL | :warning: WARN | :zzz: SKIP | :information_source: INFO | :bread: PASS |
|:-----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 6 | 1 | 32 | 7 | 97 |
| 0% | 4% | 1% | 22% | 5% | 68% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
