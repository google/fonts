# Introduction

This page lists how to learn enough about Git to move an open font project available in this Mercurial repository to a Git repository, and how to manage a open font project with it.

## Project

- [ ] Set up a Github Repo

New to Git and Github? Play the http://try.github.io 15 minute interactive game, and read http://nvie.com/posts/a-successful-git-branching-model, an essay about using Git for ongoing project management.

- [ ] Actual source files

Your project will include _actual_ source files, the ones that you use yourself when drawing the design. 
These are often quite 'messy', but no problem. 
Often these are Glyphs files, sets of UFOs, VFBs, or SFDs.

- [ ] Build source files

You may maintain a set of 'build sources', which are updated less frequently than the actual source files, and updated with care. 
They may have some 'pre-build' operations applied, like Remove Overlaps, and are used as input to a build script. 

- [ ] Build script 

You may maintain a build script that runs the build steps, or you may make a tutorial for taking those steps manually (or a mix.)

## Production

- [ ] Including ttfautohint 
- [ ] Including ttfautohint controls file

## Latin Design

- [ ] Support the 219 "base Latin" glyphs https://github.com/google/fonts/blob/master/tools/encodings/latin_unique-glyphs.nam
- [ ] Support Adobe Latin 3 http://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html
- [ ] Support Adobe Latin 4 (mainly Vietnamese) http://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-4.html
- [ ] `.notdef` glyph is a recommended design https://www.microsoft.com/typography/otspec/recom.htm

## OpenType

- [ ] Support Turkish with OpenType http://typedrawers.com/discussion/1101/izmir-turkey
- [ ] Support tabular numbers across the family http://typedrawers.com/discussion/1103/tabular-figures-width-consistency#latest

## Test Documents

- [ ] http://understandingfonts.com/2011/fonttest
- [ ] http://impallari.com/testing
- [ ] http://testmyfont.com

