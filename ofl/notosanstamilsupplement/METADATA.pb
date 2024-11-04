name: "Noto Sans Tamil Supplement"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Tamil Supplement"
  style: "normal"
  weight: 400
  filename: "NotoSansTamilSupplement-Regular.ttf"
  post_script_name: "NotoSansTamilSupplement-Regular"
  full_name: "Noto Sans Tamil Supplement Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tamil)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "tamil-supplement"
source {
  repository_url: "https://github.com/notofonts/tamil"
  archive_url: "https://github.com/notofonts/tamil/releases/download/NotoSansTamilSupplement-v2.001/NotoSansTamilSupplement-v2.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansTamilSupplement/googlefonts/ttf/NotoSansTamilSupplement-Regular.ttf"
    dest_file: "NotoSansTamilSupplement-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "bfq_Taml"  # Badaga
languages: "ta_Taml"  # Tamil
sample_text {
  masthead_full: "𑿗𑿘𑿚𑿛"
  masthead_partial: "𑿖𑿛"
  styles: "𑿕𑿖𑿗𑿘𑿙𑿚𑿛 𑿱𑿪𑿫𑿬𑿭𑿮𑿯 𑿰𑿣𑿤𑿥𑿦𑿧𑿨 𑿩𑿜𑿝𑿞𑿟𑿠𑿡"
  tester: "𑿕𑿖𑿗𑿘𑿙𑿚𑿛 𑿱𑿪𑿫𑿬𑿭𑿮𑿯 𑿰𑿣𑿤𑿥𑿦𑿧𑿨 𑿩𑿜𑿝𑿞𑿟𑿠𑿡"
  poster_sm: "𑿕𑿖𑿗𑿭𑿮𑿯 𑿙𑿚𑿛𑿱𑿪𑿫"
  poster_md: "𑿕𑿖𑿗𑿘𑿙𑿚𑿛 𑿱𑿪"
  poster_lg: "𑿗𑿘𑿚𑿛"
}
primary_script: "Taml"
