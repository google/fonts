name: "Akshar"
designer: "Tall Chai"
license: "OFL"
category: "SANS_SERIF"
date_added: "2022-03-22"
fonts {
  name: "Akshar"
  style: "normal"
  weight: 400
  filename: "Akshar[CTRS,wght].ttf"
  post_script_name: "Akshar-Light"
  full_name: "Akshar Light"
  copyright: "Copyright 2026 The Akshar Type Project Authors (https://github.com/tallchai/akshar-type)"
}
subsets: "devanagari"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "CTRS"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/tallchai/akshar-type"
  commit: "aee865978b46640a409808b0fe7433202b8dc3cb"
  archive_url: "https://github.com/tallchai/akshar-type/archive/refs/tags/v2.2.1.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Akshar[CTRS,wght].ttf"
    dest_file: "Akshar[CTRS,wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/builder.yaml"
}
primary_script: "Deva"
