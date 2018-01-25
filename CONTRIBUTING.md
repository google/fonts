# Contribute to Google Fonts

## Feedback

If you have any feedback on Google Fonts API, directory, or the fonts themselves, please create an issue at [github.com/google/fonts/issues](http://github.com/google/fonts/issues)

## New Families

If you would like to include a new font family in the Google Fonts collection, we'll be happy to include it if it meets the following criteria:

* The typeface design is original, or a legitimate revival of a design in the public domain, and of good quality. The Google Design team curates the overall Google Fonts collection and decides if fonts are of good quality. You can get general reviews of your project from the wider international type community during development by posting review requests in the [googlefonts-discuss](https://groups.google.com/forum/#!forum/googlefonts-discuss) group, and the [typedrawers](http://typedrawers.com/categories/critiques%E2%80%94type-design) review forum.  
* The project is licensed under the [SIL Open Font License v1.1](http://scripts.sil.org/OFL), with no Reserved Font Name ([why](https://github.com/simoncozens/silson/issues/1))  
* The font family name does not include any copyright holder names or registered trademarks, and no initials or abbreviations; it should be a simple and unique name, and a limited but easy way to test for uniqueness is [namecheck.fontdata.com](https://namecheck.fontdata.com)  
* The project is developed on Github or similar, with complete corresponding sources, [open to public participation](http://producingoss.com), and actively maintained. Complete corresponding sources means that the fonts are available in your preferred form of modification, the files you actually use to develop the project, along with all the build instructions or scripts needed to  reproduce the process of turning those source files into your released font binaries.  
* All font files are available in TTF format, with hinting (such as with [ttfautohint](http://www.freetype.org/ttfautohint/))  
* All font files have at a minimum the 215 glyphs listed in our [`latin_unique-glyphs.nam`](https://github.com/googlefonts/tools/blob/master/encodings/latin_unique-glyphs.nam) file  
* All font files within the family have the same Unicode character set (unencoded glyphs can differ)  
* A `README.md` file is included in the root of the source repository, and inside of that file we can read about [FONTLOG](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ofl-faq_web#43cecb44) information, and your github usernames, so that we can prepare a description ([example](https://github.com/google/fonts/blob/master/ofl/poppins/DESCRIPTION.en_us.html)) and link your name to your profile.  
* More detailed design and production details are listed in [github.com/googlefonts/gf-docs/ProjectChecklist.md](https://github.com/googlefonts/gf-docs/blob/master/ProjectChecklist.md)  

When you are ready to meet these requirements, please [create a new issue](https://github.com/google/fonts/issues) with a link to the project's source repository.

From time to time, Google Fonts provides financial and design assistance for projects. 
If you would like to discuss this, please mention that you would like someone to contact you privately when filing an issue (and have contact details on your Github profile page.)

### Updates

If your font is already on-boarded and you'd like us to update our copy, please file an issue (instead of making a pull request directly.)

We carefully check the technical aspects of updated fonts to prevent unintended changes, so we prefer to collaborate with you on your upstream project to make a release which we update from. 

## All Contributors

We'd love to accept your patches and contributions to this project. 
There is just one thing you need to do first...

Contributions to Google projects, even unofficial ones like this, must be accompanied by a Contributor License Agreement. 
This is not a copyright assignment, it simply gives Google permission to use and redistribute your contributions as part of the project.

<https://cla.developers.google.com>

You generally only need to submit the Google CLA once, so if you've already submitted one for a different project, you probably don't need to do it again.

After your contribution is included, you will be listed in [CONTRIBUTORS](CONTRIBUTORS) and/or [AUTHORS](AUTHORS) files; 
CONTRIBUTORS is the official list of people who can contribute (and typically have contributed) code to this repository, while the AUTHORS file lists the copyright holders.
