# Introduction

This page lists how to learn enough about Git to move an open font project available in this Mercurial repository to a Git repository, and how to manage a open font project with it.

## Tools

### Windows

You will need a Windows computer, real or virtual machine, for testing your fonts as web fonts. 

- [ ] Microsoft offers zero-price virtual machine images at https://dev.modern.ie/tools/vms/mac/
- [ ] MSIE
- [ ] Firefox
- [ ] Chrome
- [ ] Safari
- [ ] Opeta

### Mac

- [ ] Homebrew is a package manager for installing unix tools. http://brew.sh

```sh
brew install fontforge;
```

- [ ] pip is a package manager for installing python tools. https://pip.pypa.io

```
pip install pyfontaine;
pip install fontbakery;
```

- [ ] FontForge http://fontforge.github.io
- [ ] Glyphs https://glyphsapp.com
- [ ] FontLab https://fontlab.com
- [ ] OTMaster http://dtl.nl
- [ ] 

## Project Repository

- [ ] Set up a Github Repo

New to Git and Github? Play the http://try.github.io 15 minute interactive game, and read http://nvie.com/posts/a-successful-git-branching-model, an essay about using Git for ongoing project management.

- [ ] README.md file

Each Github repo must have a README.md that summarises the project. This may include

- [ ] DESCRIPTION.en_us.html

Description paragraph in HTML to be used directly in font directories. 
This may be omitted by the designer, but if so requires Google to create one based on the contents of the README.md.

- [ ] BRIEF.md

A design brief that describes the intentions and goals of the project. 
Ideally this will be be added at the start of a project, defining the milestones that will be completed.
Typically it will be based on a proposal document made by the designer for financial support.

- [ ] Actual source files

A type project will include _actual_ source files, the ones that designers use ourselves when drawing the design. 
These are typically files with extensions like `.glyphs .ufo .vfb .sfd .sfdir`.
These are often quite 'messy'. 
Common indications of actual source files are:

- guidelines
- overlapping shapes
- multiple layers with alternative drawings
- unencoded glyphs with alternative drawings
- 'smart components'

- [ ] Build source files

Some type projects maintain a set of 'build sources', which are used as input to a build script. 
They are updated less frequently than the actual source files, and updated with care. 
Common indications of build source files are:

- no or minimal guidelines
- no overlapping shapes (the result of a Remove Overlaps operation)
- a single layer per Master
- no unusual or additional unencoded glyphs with alternative drawings
- no 'smart components'

- [ ] Build process documentation
- [ ] Build process script

You may maintain a build script that runs the build steps, or you may make a tutorial for taking those steps manually (or a mix.)

- [ ] Binary files
 
After the build process you will have OTF and TTF files.

- [ ] "Clean" repo

There should not be 'stray' files in the repo, such as `.empty` 

## Production

- [ ] Including ttfautohint command line options in build script
- [ ] Including ttfautohint controls file

## Latin Design

- [ ] Support the 219 "base Latin" glyphs https://github.com/google/fonts/blob/master/tools/encodings/latin_unique-glyphs.nam
- [ ] Support Adobe Latin 3 http://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html
- [ ] Support Adobe Latin 4 (mainly Vietnamese) http://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-4.html
- [ ] `.notdef` glyph is a recommended design https://www.microsoft.com/typography/otspec/recom.htm
- [ ] Anchors for all letter and diacritics https://github.com/weiweihuanghuang/Work-Sans/pull/17#issuecomment-139910842
- [ ] Prime design https://github.com/googlei18n/noto-fonts/issues/510#issue-105444463

## OpenType

- [ ] Support Turkish with OpenType http://typedrawers.com/discussion/1101/izmir-turkey
- [ ] Support tabular numbers across the family http://typedrawers.com/discussion/1103/tabular-figures-width-consistency#latest

## Test Documents

- [ ] http://understandingfonts.com/2011/fonttest
- [ ] http://impallari.com/testing
- [ ] http://testmyfont.com

### Tests

- [ ] Test for all letter/diacritic combinations https://github.com/weiweihuanghuang/Work-Sans/pull/17#issuecomment-139910842

# Further reading

### UFO

The UFO format is documented at http://unifiedfontobject.org and developed on Github (https://github.com/unified-font-object/ufo-spec) and the ufo-spec mailing list (https://groups.google.com/forum/#!forum/ufo-spec)
