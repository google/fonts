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
  copyright: "Copyright 2025 The SUSE Project Authors (https://github.com/SUSE/suse-font)"
}
fonts {
  name: "SUSE"
  style: "italic"
  weight: 400
  filename: "SUSE-Italic[wght].ttf"
  post_script_name: "SUSE-ThinItalic"
  full_name: "SUSE Thin Italic"
  copyright: "Copyright 2025 The SUSE Project Authors (https://github.com/SUSE/suse-font)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/SUSE/suse-font"
  commit: "7159afb2555b06d3a5c2f90e4d324e59e69c277d"
  archive_url: "https://github.com/SUSE/suse-font/releases/download/v2.001/suse-font-v2.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/SUSE[wght].ttf"
    dest_file: "SUSE[wght].ttf"
  }
  files {
    source_file: "fonts/variable/SUSE-Italic[wght].ttf"
    dest_file: "SUSE-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
