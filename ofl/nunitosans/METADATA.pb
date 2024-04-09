name: "Nunito Sans"
designer: "Vernon Adams, Jacques Le Bailly, Manvel Shmavonyan, Alexei Vanyashin"
license: "OFL"
category: "SANS_SERIF"
date_added: "2016-10-06"
fonts {
  name: "Nunito Sans"
  style: "normal"
  weight: 400
  filename: "NunitoSans[YTLC,opsz,wdth,wght].ttf"
  post_script_name: "NunitoSans-12ptExtraLight"
  full_name: "Nunito Sans 12pt ExtraLight"
  copyright: "Copyright 2016 The Nunito Sans Project Authors (https://github.com/Fonthausen/NunitoSans)"
}
fonts {
  name: "Nunito Sans"
  style: "italic"
  weight: 400
  filename: "NunitoSans-Italic[YTLC,opsz,wdth,wght].ttf"
  post_script_name: "NunitoSans-12ptExtraLightItalic"
  full_name: "Nunito Sans 12pt ExtraLight Italic"
  copyright: "Copyright 2016 The Nunito Sans Project Authors (https://github.com/Fonthausen/NunitoSans)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "YTLC"
  min_value: 440.0
  max_value: 540.0
}
axes {
  tag: "opsz"
  min_value: 6.0
  max_value: 12.0
}
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 125.0
}
axes {
  tag: "wght"
  min_value: 200.0
  max_value: 1000.0
}
registry_default_overrides {
  key: "opsz"
  value: 12.0
}
source {
  repository_url: "https://github.com/googlefonts/NunitoSans"
  commit: "058bd7a2f33d6ad5ef1df985b3db403622016a8c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/NunitoSans[YTLC,opsz,wdth,wght].ttf"
    dest_file: "NunitoSans[YTLC,opsz,wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/NunitoSans-Italic[YTLC,opsz,wdth,wght].ttf"
    dest_file: "NunitoSans-Italic[YTLC,opsz,wdth,wght].ttf"
  }
  branch: "main"
}
