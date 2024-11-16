name: "Noto Sans Khojki"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Khojki"
  style: "normal"
  weight: 400
  filename: "NotoSansKhojki-Regular.ttf"
  post_script_name: "NotoSansKhojki-Regular"
  full_name: "Noto Sans Khojki Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/khojki)"
}
subsets: "khojki"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/khojki"
  archive_url: "https://github.com/notofonts/khojki/releases/download/NotoSansKhojki-v2.005/NotoSansKhojki-v2.005.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "NotoSansKhojki/googlefonts/ttf/NotoSansKhojki-Regular.ttf"
    dest_file: "NotoSansKhojki-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "sd_Khoj"  # Sindhi, Khojki
primary_script: "Khoj"
