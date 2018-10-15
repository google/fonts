# Google Fonts Quick Start
A guide for users of [Glyphs](https://glyphsapp.com) who want to create/contribute to projects on Google Fonts.


## Repo Structure

- There should be one definitive set of sources. [This](https://github.com/EbenSorkin/Merriweather/tree/master/sources), not [this](https://github.com/VanillaandCream/Catamaran-Tamil/tree/master/Instances)
- One click builds are essential. Generating from Glyphs is sufficient in most cases
- Repositories should have the following structure:
```
.
├── AUTHORS.txt
├── CONTRIBUTORS.txt
├── DESCRIPTION.en_us.html
├── FONTLOG.txt
├── OFL.txt
├── README.md
├── documentation
│   ├── img
│   │   ├── details.png
│   │   ├── inco-preview.png
│   │   ├── permille.png
│   │   ├── s.png
│   │   ├── test.png
│   │   ├── v1.png
│   │   ├── v2.png
│   │   └── xi-mac-screenshot.png
│   ├── inconsolata-diagonals.ai
│   ├── inconsolata-features.pdf
│   └── inconsolata-test.txt
├── fonts
│   ├── otf
│   │   ├── Inconsolata-Bold.otf
│   │   └── Inconsolata-Regular.otf
│   └── ttf
│       ├── Inconsolata-Bold.ttf
│       └── Inconsolata-Regular.ttf
└── sources
    └── Inconsolata.glyphs

```


## Fonts
- No glyphs should be missing when compared to the previous release
- No weights/styles should be missing when compared to the previous release
- Less is always more, no one needs stylistic set 16. Make the family better


## Git
Using git is essential. By not using git, we're not able to track the history of a project.

- If upgrading a project, fork it, upgrade it and send a pull request back to the original repo
- If starting a fresh project, create a new repository in [Googlefonts](https://github.com/googlefonts). If you don't have permission, email Marc Foley/Dave Crossland.
- Releases should be tagged. [Montserrat does this well](https://github.com/JulietaUla/Montserrat/releases)
- Commits should be granular. Many small commits are better than one epic commit. 
- Make commits at meangingful points, e.g one commit for updating the metadata and a seperate commit for changing a set of anchor positions. If in doubt, study [Montserrat's commit history](https://github.com/JulietaUla/Montserrat/commits/master)


## Proofing
Always QA your projects with the tools listed below. QA regularly.

- [gf-glyphs-scripts](https://github.com/googlefonts/gf-glyphs-scripts) Official Google Fonts QA/Production scripts for [Glyphs](https://glyphsapp.com). Make sure the QA script passes.
- [mf-glyphs-scripts](https://github.com/m4rc1e/mf-glyphs-scripts) Marc Foley's scripts for Glyphs. QA > Check Font is very useful
- [Font-Bakery](https://fontbakery.appspot.com) for checking finished ttfs
- [GF-Regression](http://45.55.138.144) to visually proof upgraded families

## Everything Else
- If unsure, study [Montserrat](https://github.com/JulietaUla/Montserrat)
