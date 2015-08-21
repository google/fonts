Welcome to the Google Code project for Google Web Fonts!

This site contains all the font files available in [Google Web Fonts](http://www.google.com/webfonts), including the source files.

There is also an issue manager where fonts problems are reported and tracked, and a wiki with information for type designers.

If you would like to actively participate in the design of a font project, please read the FONTLOG.txt file that accompanies the fonts sources and contact the original designer directly.

### Submit a Font

If you wish to submit a font, please use the [Contribute to Google Web Fonts form](https://docs.google.com/a/google.com/forms/d/1w2JOnVv_Vfcg1H_nploj1FRz4LcFsLaFmFkEj50PyW4/viewform).

### Report a Font Issue

**Note: Google Chrome has a known bug, where fonts installed on your computer will no longer work as web fonts. Please use a font manager to conveniently de/activate these fonts**

  1. Sign in with your Google Account
  1. Go to the Issues tab above and click ["New Issue"](http://code.google.com/p/googlefontdirectory/issues/entry?template=Defect%20report%20from%20user)
  1. Explain your issue and submit. Attaching screenshot image files is helpful.

Please do not upload fonts you wish to be included in GWF using this issue tracker - use the [Contribute to Google Web Fonts form](https://services.google.com/fb/forms/submitafont/) instead.

Thanks for taking the time to do this!

## Download Source Files

In [www.google.com/webfonts](http://www.google.com/webfonts) you can add a specific font family to your collection, and then in the top right click 'download collection' to download the binary TTF files. This is useful for making web page mock ups, or otherwise using the fonts.

To make modifications to the fonts, you may wish to use the 'source' files, not the binary TTF files. These source files are available in this Google Code project's Source repository, and are usually available as OTF files, but files may also be available in UFO, FontForge, FontLab or Glyphs editor formats.

If you wish to make modifications to the fonts, you are free to do so under the terms of the font's license. Typically this is the SIL Open Font License, but there are some others such as the Apache 2 license, or the Ubuntu Font License. Make sure that you read these licenses so that you understand what is permitted and restricted, just as you would with any other font license.

The OFL has an option for designers to declare Reserved Font Names. If the font you wish to modify has a Reserved Font Name, be sure to change the name of the font before making any further modifications.

To download all the files in the repository - totaling 2.5Gb and growing - you must use the "Mercurial" version control program. Mercurial will download all the files, and then as updates are made, download only the changes - so that you don't have to repeatedly download 2.5Gb+ of data that did not change.

### Windows

  1. [Download and install TortoiseHG](http://tortoisehg.bitbucket.org/download/), a graphical user interface for Mercurial.
  1. Make a new folder somewhere.
  1. Right click that folder, go to TortoiseHG, and click Clone
  1. Enter for the Source `https://googlefontdirectory.googlecode.com/hg/`
  1. Click OK and wait for the download to complete
  1. Find the folder you created and browse around

In future, to update you can then right click the folder you made and click 'Hg Synchronize'

To install a downloaded font, open the Control Panel, find the Fonts folder there, and drag and drop the OTF or TTF files inside that folder. You may need to restart your applications, but not the whole computer, for the fonts to be ready for use.

### Mac OS X

  1. Click the Apple logo in the top left of the screen, then 'About this Mac,' and note the version of Mac OS X you have (10.5, 10.6, etc)
  1. [Download and install Mercurial](http://mercurial.selenic.com/) for your version of Mac OS X
  1. In Finder, go to Applications, find the Utilities folder, and there find and open the Terminal application
  1. Paste in `hg clone https://code.google.com/p/googlefontdirectory/ googlefontdirectory;`
  1. Hit return and wait for the download to complete
  1. Find the folder 'googlefontdirectory' in your Home folder, and browse around

In future, to update you can open the Terminal application and paste in `cd googlefontdirectory; hg pull;` If you move the googlefontdirectory folder, you will have to prepend the path to that folder.

You may also wish to investigate the [Source Tree application](http://www.sourcetreeapp.com/) which provides a GUI for Mercurial.

To install a downloaded font, open a Finder window, go to your Home folder, then Library, then Fonts, and drag and drop the OTF or TTF files inside that folder. The Fonts folder may not exist, and if so you can create it. You may need to restart your applications, but not the whole computer, for the fonts to be ready for use.

### Fedora GNU/Linux

  1. Open the Terminal application
  1. Install Mercurial by pasting in the command `yum install -y mercurial;`
  1. Hit return to run the command
  1. Paste in `hg clone https://code.google.com/p/googlefontdirectory/ googlefontdirectory;`
  1. Hit return and wait for the download to complete
  1. Find the folder 'googlefontdirectory' in your Home folder, and browse around

In future, to update you can open the Terminal application and paste in `cd googlefontdirectory; hg pull;`


To install a downloaded font, open a file manager window, go to your Home folder, then ".fonts" - this directory may not exist, and if so, create it. Then drag and drop the OTF or TTF files inside that folder.  You may need to restart your applications, but not the whole computer, for the fonts to be ready for use.

### Ubuntu GNU/Linux

  1. Open the Terminal application
  1. Install Mercurial by pasting in the command `apt-get install -y mercurial;`
  1. Hit return to run the command
  1. Paste in `hg clone https://code.google.com/p/googlefontdirectory/ googlefontdirectory;`
  1. Hit return and wait for the download to complete

In future, to update you can open the Terminal application and paste in `cd googlefontdirectory; hg pull;`

To install a downloaded font, open a file manager window, go to your Home folder, then ".fonts" - this directory may not exist, and if so, create it. Then drag and drop the OTF or TTF files inside that folder.  You may need to restart your applications, but not the whole computer, for the fonts to be ready for use.