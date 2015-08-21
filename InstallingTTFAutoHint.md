# How To Install The Binary on Mac OS X

_How to compile the `ttfautohint` tool that Google Web Fonts supported_

Go to http://freetype.org/ttfautohint/#download and click the blue text 'Apple'

You will download the file ttfautohint-0.8-tty-osx.tar.gz - if OS X asks you to pick between tar.gz and .gz, pick tar.gz

Find the file in the finder, drag and drop it into your home folder, and unzip it. You will find a file with a black icon named 'ttfautohint'

Run the Terminal and type this in:

```
    sudo mkdir -p /usr/local/bin; 
```

and hit return. Enter your Mac login password (as you would for the screensaver) and hit return. Then type:

```
    sudo mv ttfautohint /usr/local/bin/; 
```

and hit return. Then you can run ttfautohint! :) See the help screen this way:

```
   ttfautohint --help 
```

# The following information is a little out of date, and may no longer be valid

# Installing ttfautohint from source code

# Introduction

`ttfautohint` is a great new autohinter by Werner Lemberg, maintainer of the freetype library.

Here is how to install it and use it from source code.

Thanks to [Vernon Adams](http://code.newtypography.co.uk/) and [Matt Wiebe](http://somadesign.ca/2011/improve-windows-type-rendering-with-ttfautohint/) for the initial version and thorough checking of this guide.

You may like to see Vern's detailed blogging with many comparison screenshots of the tool at http://code.newtypography.co.uk

# Installation

Open a Terminal application and run the following commands one at a time.

```

# First install XCode from the Mac OS X Install DVD

# make a temporary directory and go into it

mkdir ~/tmp;

cd ~/tmp;

# download GNU m4

curl -O http://ftp.gnu.org/gnu/m4/m4-1.4.16.tar.gz || wget 

http://ftp.gnu.org/gnu/m4/m4-1.4.16.tar.gz;

# unzip it and go into its directory

tar -xzvf m4-1.4.16.tar.gz;

cd m4-1.4.16;

# configure the source code

./configure --prefix=/usr/local;

# compile the source code

make;

# install the program

sudo make install;

# go back up to the tmp directory

cd ..;


# download autoconf

curl -O http://ftp.gnu.org/gnu/autoconf/autoconf-2.68.tar.gz || wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.68.tar.gz;

# unzip the source code

tar -xzvf autoconf-2.68.tar.gz;

cd autoconf-2.68;

# configure the source code

./configure --prefix=/usr/local;

# compile the source code

make;

# install the program

sudo make install;

cd ..;

# set the PATH environment variable to use these programs

PATH=/opt/local/bin:/opt/local/sbin:/opt/local/bin:/opt/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/bin/g4bin:/usr/local/sbin:/usr/X11/bin;

# download automake

curl -O http://ftp.gnu.org/gnu/automake/automake-1.11.tar.gz || wget http://ftp.gnu.org/gnu/automake/automake-1.11.tar.gz;

# unzip the source code

tar xzvf automake-1.11.tar.gz;

cd automake-1.11;

# configure the source code

./configure --prefix=/usr/local;

# compile the source code

make;

# install the program

sudo make install;

cd ..;

# download libtool

curl -O http://ftp.gnu.org/gnu/libtool/libtool-2.4.tar.gz || wget http://ftp.gnu.org/gnu/libtool/libtool-2.4.tar.gz;

# unzip the program

tar xzvf libtool-2.4.tar.gz;

cd libtool-2.4;

# configure the source code

./configure --prefix=/usr/local;

# compile the source code

make;

# install the program

sudo make install;

cd ..;


# download freetype

curl -O http://switch.dl.sourceforge.net/project/freetype/freetype2/2.4.5/freetype-2.4.5.tar.gz || wget http://switch.dl.sourceforge.net/project/freetype/freetype2/2.4.5/freetype-2.4.5.tar.gz;

# unzip the program

tar zxvf freetype-2.4.5.tar.gz;

cd freetype-2.4.5;

# configure the source code

./configure --prefix=/usr/local;

# compile the source code

make;

# install the program

sudo make install;

cd ..;

# download ttfautohint

curl -O http://netcologne.dl.sourceforge.net/project/freetype/ttfautohint/0.3/ttfautohint-0.3.tar.gz || wget http://netcologne.dl.sourceforge.net/project/freetype/ttfautohint/0.3/ttfautohint-0.3.tar.gz;

# unzip the program

tar zxvf ttfautohint-0.3.tar.gz;

cd ttfautohint-0.3;

# configure the source code

./configure --prefix=/usr/local;

# compile the source code

make;

# install the program

sudo make install;

```

You can now close the Terminal window.

# Usage

To use ttfautohint, open a Terminal window run the program from the terminal by typing

```

ttfautohint -f -i -v INFILE.ttf OUTFILE.ttf

```

Here INFILE.ttf is your unhinted font file, and OUTFILE.ttf is the hinted font file the program will produce.

If you type only the program name, you will see all the options, like this:

```

$ ttfautohint 

Usage: ttfautohint [OPTION] IN-FILE OUT-FILE
Replace hints in TrueType font IN-FILE and write output to OUT-FILE.
The new hints are based on FreeType's autohinter.

This program is a simple front-end to the `ttfautohint' library.

Options:
  -f, --latin-fallback       set fallback script to latin
  -h, --help                 display this help and exit
  -i, --ignore-permissions   override font license restrictions
  -l, --hinting-range-min=N  the minimum ppem value for generating hints
  -p, --pre-hinting          apply original hints before generating hints
  -r, --hinting-range-max=N  the maximum ppem value for generating hints
  -v, --verbose              show progress information
  -V, --version              print version information and exit
  -x, --x-height-snapping-exceptions=STRING
                             specify a comma-separated list of x-height
                             snapping exceptions ranges and single values

The program accepts both TTF and TTC files as input.
The `gasp' table of OUT-FILE enables grayscale hinting for all sizes.
Use option -i only if you have a legal permission to modify the font.
If option -f is not set, glyphs not in the latin range stay unhinted.
The used ppem value for option -p is FUnits per em, normally 2048.

Report bugs to: freetype-devel@nongnu.org
FreeType home page: <http://www.freetype.org>

```