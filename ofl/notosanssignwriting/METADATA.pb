name: "Noto Sans SignWriting"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2022-10-31"
fonts {
  name: "Noto Sans SignWriting"
  style: "normal"
  weight: 400
  filename: "NotoSansSignWriting-Regular.ttf"
  post_script_name: "NotoSansSignWriting-Regular"
  full_name: "Noto Sans SignWriting Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/sign-writing)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "signwriting"
source {
  repository_url: "https://github.com/notofonts/sign-writing"
  archive_url: "https://github.com/notofonts/sign-writing/releases/download/NotoSansSignWriting-v2.005/NotoSansSignWriting-v2.005.zip"
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
    source_file: "NotoSansSignWriting/googlefonts/ttf/NotoSansSignWriting-Regular.ttf"
    dest_file: "NotoSansSignWriting-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
sample_text {
  masthead_full: "𝡝𝪩𝡝𝪡𝤅"
  masthead_partial: "𝧿𝨔"
  styles: "𝧿𝨊𝡝𝪜𝦦𝪬𝡝𝪩𝡝𝪡𝤅"
  tester: "𝧿𝨊𝡝𝪜𝦦𝪬𝡝𝪩𝡝𝪡𝤅"
  poster_sm: "𝧿𝨊𝡝𝪜𝦦𝪬𝡝𝪩𝡝𝪡𝤅"
  poster_md: "𝡝𝪜𝦦𝪬"
  poster_lg: "𝡝𝪩𝡝𝪡𝤅"
}
