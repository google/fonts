name: "Instrument Sans"
designer: "Rodrigo Fuenzalida, Jordan Egstad"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-04-13"
fonts {
  name: "Instrument Sans"
  style: "normal"
  weight: 400
  filename: "InstrumentSans[wdth,wght].ttf"
  post_script_name: "InstrumentSans-Regular"
  full_name: "Instrument Sans Regular"
  copyright: "Copyright 2022 The Instrument Sans Project Authors (https://github.com/Instrument/instrument-sans)"
}
fonts {
  name: "Instrument Sans"
  style: "italic"
  weight: 400
  filename: "InstrumentSans-Italic[wdth,wght].ttf"
  post_script_name: "InstrumentSans-Italic"
  full_name: "Instrument Sans Italic"
  copyright: "Copyright 2022 The Instrument Sans Project Authors (https://github.com/Instrument/instrument-sans)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/Instrument/instrument-sans"
  commit: "4a27996becc1c7d8e8d4095df4bb485068252bb2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/InstrumentSans[wdth,wght].ttf"
    dest_file: "InstrumentSans[wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/InstrumentSans-Italic[wdth,wght].ttf"
    dest_file: "InstrumentSans-Italic[wdth,wght].ttf"
  }
  branch: "master"
}
