name: "Noto Sans Syloti Nagri"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Syloti Nagri"
  style: "normal"
  weight: 400
  filename: "NotoSansSylotiNagri-Regular.ttf"
  post_script_name: "NotoSansSylotiNagri-Regular"
  full_name: "Noto Sans Syloti Nagri Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/syloti-nagri)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "syloti-nagri"
source {
  repository_url: "https://github.com/notofonts/syloti-nagri"
  commit: "24ab3ac364a1b0882f36fa18f8f090145b009bf8"
  archive_url: "https://github.com/notofonts/syloti-nagri/releases/download/NotoSansSylotiNagri-v2.004/NotoSansSylotiNagri-v2.004.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansSylotiNagri/googlefonts/ttf/NotoSansSylotiNagri-Regular.ttf"
    dest_file: "NotoSansSylotiNagri-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-syloti-nagri.yaml"
}
is_noto: true
languages: "syl_Sylo"
primary_script: "Sylo"
