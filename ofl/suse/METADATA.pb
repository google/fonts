name: "SUSE"
designer: "René Bieder"
license: "OFL"
category: "SANS_SERIF"
date_added: "2024-08-14"
fonts {
  name: "SUSE"
  style: "normal"
  weight: 400
  filename: "SUSE[wght].ttf"
  post_script_name: "SUSE-Thin"
  full_name: "SUSE Thin"
  copyright: "Copyright 2024 The SUSE Project Authors (https://github.com/SUSE/suse-font)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 800.0
}
source {
  repository_url: "https://github.com/SUSE/suse-font"
  commit: "d5d0b353f3defb9dece73334a50cc4a62ae97e00"
  archive_url: "https://github.com/SUSE/suse-font/releases/download/v1.000/suse-font-v1.000.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/SUSE[wght].ttf"
    dest_file: "SUSE[wght].ttf"
  }
  branch: "main"
}
