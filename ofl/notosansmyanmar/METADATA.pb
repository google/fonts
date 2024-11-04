name: "Noto Sans Myanmar"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Myanmar"
  style: "normal"
  weight: 400
  filename: "NotoSansMyanmar[wdth,wght].ttf"
  post_script_name: "NotoSansMyanmar-Regular"
  full_name: "Noto Sans Myanmar Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/myanmar)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "myanmar"
axes {
  tag: "wdth"
  min_value: 62.5
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/myanmar"
  archive_url: "https://github.com/notofonts/myanmar/releases/download/NotoSansMyanmar-v2.107/NotoSansMyanmar-v2.107.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansMyanmar/googlefonts/variable-ttf/NotoSansMyanmar[wdth,wght].ttf"
    dest_file: "NotoSansMyanmar[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "kht_Mymr"  # Khamti
languages: "ksw_Mymr"  # S'gaw Karen, Myanmar
languages: "mnw_Mymr"  # Mon
languages: "my_Mymr"  # Burmese
languages: "pwo_Mymr"  # Pwo Western Karen, Myanmar
languages: "shn_Mymr"  # Shan
primary_script: "Mymr"
