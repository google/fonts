name: "Libre Barcode EAN13 Text"
designer: "Lasse Fister"
license: "OFL"
category: "DISPLAY"
date_added: "2020-10-26"
fonts {
  name: "Libre Barcode EAN13 Text"
  style: "normal"
  weight: 400
  filename: "LibreBarcodeEAN13Text-Regular.ttf"
  post_script_name: "LibreBarcodeEAN13Text-Regular"
  full_name: "Libre Barcode EAN13 Text Regular"
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
    source_file: "fonts/LibreBarcodeEAN13Text-Regular.ttf"
    dest_file: "LibreBarcodeEAN13Text-Regular.ttf"
  }
  branch: "master"
}
sample_text {
  masthead_full: "abcdefghij"
  masthead_partial: "abcd"
  styles: "abcdefghij x012345678 23456789 klmnopqrst"
  tester: "abcdefghij x012345678 23456789 klmnopqrst"
  poster_sm: "abcdefghij x012345678 23456789"
  poster_md: "abcdefghij x012345678"
  poster_lg: "23456789"
}
classifications: "DISPLAY"
classifications: "SYMBOLS"
