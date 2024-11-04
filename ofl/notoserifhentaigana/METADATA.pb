name: "Noto Serif Hentaigana"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2024-02-26"
fonts {
  name: "Noto Serif Hentaigana"
  style: "normal"
  weight: 400
  filename: "NotoSerifHentaigana[wght].ttf"
  post_script_name: "NotoSerifHentaigana-ExtraLight"
  full_name: "Noto Serif Hentaigana ExtraLight"
  copyright: "Copyright 2023 The Noto Project Authors (https://github.com/notofonts/hentaigana)"
}
subsets: "kana-extended"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 200.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/hentaigana"
  archive_url: "https://github.com/notofonts/hentaigana/releases/download/NotoSerifHentaigana-v1.000/NotoSerifHentaigana-v1.000.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSerifHentaigana/googlefonts/variable/NotoSerifHentaigana[wght].ttf"
    dest_file: "NotoSerifHentaigana[wght].ttf"
  }
  branch: "main"
}
is_noto: true
primary_script: "Hira"
sample_text {
  # The text is the traditional Japanese pangram poem "Iroha"
  # https://en.wikipedia.org/wiki/Iroha
  masthead_full: "𛀆𛄆𛂡𛂉𛂺𛂳𛁹 𛁢𛃱𛂏𛃸𛄖 𛄉𛀗𛃧𛁟𛄀𛁗 𛁩𛂒𛁿𛃰𛃐"
  masthead_partial: "𛀆𛄆𛂡𛂉𛂺𛂳𛁹 𛁢𛃱𛂏𛃸𛄖 𛄉𛀗𛃧𛁟𛄀𛁗 𛁩𛂒𛁿𛃰𛃐"
  styles: "𛀆𛄆𛂡𛂉𛂺𛂳𛁹 𛁢𛃱𛂏𛃸𛄖 𛄉𛀗𛃧𛁟𛄀𛁗 𛁩𛂒𛁿𛃰𛃐"
  # This is "I-I-I-I RO-RO-RO-RO HA-HA-HA-HA ..." using different variant forms of each character
  tester: "𛀆𛀇𛀈𛀉 𛄂𛄃𛄄𛄅 𛂞𛂟𛂠𛂡 𛂇𛂈𛂉𛂊 𛂺𛂻𛂼𛂽 𛂳𛂴𛂵𛂶 𛁷𛁸𛁹𛁺 𛁢𛁣𛁤𛁥 𛃱𛃲𛃳𛃴 𛂏𛂐𛂑 𛃸𛃹𛃺𛃻 𛄖𛄗𛄘𛄙"
  poster_sm: "𛀆𛄆𛂡𛂉𛂺𛂳𛁹 𛁢𛃱𛂏𛃸𛄖 𛄉𛀗𛃧𛁟𛄀𛁗 𛁩𛂒𛁿𛃰𛃐"
  poster_md: "𛀆𛄆𛂡𛂉𛂺𛂳𛁹 𛁢𛃱𛂏𛃸𛄖 𛄉𛀗𛃧𛁟𛄀𛁗 𛁩𛂒𛁿𛃰𛃐"
  poster_lg: "𛀆𛄆𛂡𛂉𛂺𛂳𛁹 𛁢𛃱𛂏𛃸𛄖 𛄉𛀗𛃧𛁟𛄀𛁗 𛁩𛂒𛁿𛃰𛃐"
}