# Google Fonts Files

This project contains the binary font files served by Google Fonts: http://www.google.com/fonts

The top level directories indicate the license of all files found within them.
Subdirectories are named according to the family name of the fonts within. 

Each family subdirectory contains the  `.ttf` font files served by Google Fonts, plus a `METADATA.pb` file with metadata for the family, and a `DESCRIPTION.en_us.html` with a description of the family in US English.

Also [/designers](designers) contains a list of the Google+ pages for the fonts' designers.

## Bug reports and improvement requests

If you find a problem with a font file, or have a request for future development of a font project, please [create a new issue in this project's issue tracker](https://github.com/google/fonts/issues).

## Download All Google Fonts

You can download all Google Fonts in a simple ZIP snapshot (over 250Mb) from <https://github.com/google/fonts/archive/master.zip>

#### Sync With Git

You can also sync the collection with git, so that you can update by only fetching what has changed.
To learn how to use git, Github provides [illustrated guides](https://guides.github.com) and a [youtube channel](https://www.youtube.com/user/GitHubGuides), and a [learning game that takes just 15 minutes](https://try.github.io). 
Free, open source git applications are available for [Windows](https://msysgit.github.io) and [Mac OS X](http://gitx.laullon.com).

## Licensing

It is important to always read the license for every font that you use.
Each font family directory contains the appropriate license file for the fonts in that directory. 
The fonts files themselves also contain licensing and authorship metadata.

Most of the fonts in the collection use the SIL Open Font License, v1.1.
Some fonts use the Apache 2 license. 
The Ubuntu fonts use the Ubuntu Font License v1.0. 

The SIL Open Font License has an option for copyright holders to include a Reserved Font Name requirement, and this option is used with some of the fonts. 
If you modify those fonts, please take care of this important detail.

## Source Files

Source files for each family are often available from the designer, or from https://github.com/googlefonts 

These fonts are usually the result of collaborative projects, where you are invited to discuss issues with the designers and even contribute to their on-going development.

When customising or remixing fonts, please do contact the designers to understand what they might need in order to include your improvements.

Most of all: Enjoy the fonts!

##How to use Google Fonts on you website
There are two types of doing it: using the google API fonts directly or using google font downloading it.

Let's make an example using the Antonio Font downloading the Font.
1)First , you need to download this repo on a folder named "font"
2)Second
Create a file name style.css.
And copy the following code to it:

@font-face {
  font-family: 'Antonio';
  font-style: normal;
  font-weight: 300;
  src: local('Antonio Light'), local('Antonio-Light'), url(fonts/ofl/antonio/Antonio-Light.ttf) format('ttf');
}
@font-face {
  font-family: 'Antonio';
  font-style: normal;
  font-weight: 400;
  src: local('Antonio'), local('Antonio-Regular'), url(fonts/ofl/antonio/Antonio-Regular.ttf) format('ttf');
}

3)Then we create an HTML file with the following code:

<html>
  <head>
    <link href="styles.css" rel="stylesheet">
  
  </head>
  <body>
    <div>Just Making an Example using Google Fonts</div>
  </body>
</html>



– The Google Fonts team, 2015-06-18
