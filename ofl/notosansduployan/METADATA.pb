name: "Noto Sans Duployan"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Duployan"
  style: "normal"
  weight: 400
  filename: "NotoSansDuployan-Regular.ttf"
  post_script_name: "NotoSansDuployan-Regular"
  full_name: "Noto Sans Duployan Regular"
  copyright: "Copyright 2018-2019 David Corbett. Copyright 2019-2022 Google LLC. All Rights Reserved."
}
fonts {
  name: "Noto Sans Duployan"
  style: "normal"
  weight: 700
  filename: "NotoSansDuployan-Bold.ttf"
  post_script_name: "NotoSansDuployan-Bold"
  full_name: "Noto Sans Duployan Bold"
  copyright: "Copyright 2018-2019 David Corbett. Copyright 2019-2022 Google LLC. All Rights Reserved."
}
subsets: "duployan"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/duployan"
  archive_url: "https://github.com/notofonts/duployan/releases/download/NotoSansDuployan-v3.001/NotoSansDuployan-v3.001.zip"
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
    source_file: "NotoSansDuployan/googlefonts/ttf/NotoSansDuployan-Regular.ttf"
    dest_file: "NotoSansDuployan-Regular.ttf"
  }
  files {
    source_file: "NotoSansDuployan/googlefonts/ttf/NotoSansDuployan-Bold.ttf"
    dest_file: "NotoSansDuployan-Bold.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "chn_Dupl"  # Chinook Jargon, Duployan
languages: "fr_Dupl"  # French, Duployan
sample_text {
  masthead_full: "𛰳𛱰𛱘𛱢"
  masthead_partial: "𛰠𛰏"
  styles: "𛱔𛱕𛱖𛱗𛱘𛱙𛱚 𛱩𛱪𛱰𛱱𛱲𛱳𛱴 𛰀𛰁𛰂𛰃𛰄𛰅𛰆 𛲔𛲕𛲖𛲗𛲘𛲙𛲜 𛰎𛰏𛰐𛰑𛰒𛰓𛰔 𛱢𛱣𛱤𛱥𛱦𛱧𛱨"
  tester: "𛰀𛰁𛰂𛰃𛰄𛰅𛰆 𛰱𛰲𛰳𛰴𛰵𛰶𛰷 𛱼𛲀𛲁𛲂𛲃𛲄𛲅 𛰎𛰏𛰐𛰑𛰒𛰓𛰔 𛱆𛱇𛱈𛱉𛱊𛱋𛱌 𛱢𛱣𛱤𛱥𛱦𛱧𛱨 𛱔𛱕𛱖𛱗𛱘𛱙𛱚 𛲔𛲕𛲖𛲗𛲘𛲙𛲜 𛱩𛱪𛱰𛱱𛱲𛱳𛱴 𛰜𛰝𛰞𛰟𛰠𛰡𛰢"
  poster_sm: "𛰡𛰓𛰵𛱖𛰐𛱗𛱴𛰶𛱙𛰆"
  poster_md: "𛰷𛰓𛰆𛲜𛲗 𛰶𛱗𛱖"
  poster_lg: "𛰞𛰆"
}
primary_script: "Dupl"
