name: "Libre Barcode 39"
designer: "Lasse Fister"
license: "OFL"
category: "DISPLAY"
date_added: "2017-07-31"
fonts {
  name: "Libre Barcode 39"
  style: "normal"
  weight: 400
  filename: "LibreBarcode39-Regular.ttf"
  post_script_name: "LibreBarcode39-Regular"
  full_name: "Libre Barcode 39 Regular"
  copyright: "Copyright 2017-2020 The Libre Barcode Project Authors (https://github.com/graphicore/librebarcode)"
}
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/graphicore/librebarcode"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/LibreBarcode39-Regular.ttf"
    dest_file: "LibreBarcode39-Regular.ttf"
  }
  branch: "master"
}
classifications: "DISPLAY"
classifications: "SYMBOLS"
sample_text {
  masthead_full: "abcdefghij"
  masthead_partial: "abcd"
  styles: "abcdefghij x012345678 23456789 klmnopqrst"
  tester: "abcdefghij x012345678 23456789 klmnopqrst"
  poster_sm: "abcdefghij x012345678 23456789"
  poster_md: "abcdefghij x012345678"
  poster_lg: "23456789"
}
