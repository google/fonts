name: "Google Sans Code"
designer: "Google, Universal Thirst"
license: "OFL"
category: "MONOSPACE"
date_added: "2024-11-21"
fonts {
  name: "Google Sans Code"
  style: "normal"
  weight: 400
  filename: "GoogleSansCode[wght].ttf"
  post_script_name: "GoogleSansCode-Regular"
  full_name: "Google Sans Code Regular"
  copyright: "Copyright 2025 The Google Sans Code Project Authors (github.com/googlefonts/googlesans-code)"
}
fonts {
  name: "Google Sans Code"
  style: "italic"
  weight: 400
  filename: "GoogleSansCode-Italic[wght].ttf"
  post_script_name: "GoogleSansCode-Italic"
  full_name: "Google Sans Code Italic"
  copyright: "Copyright 2025 The Google Sans Code Project Authors (github.com/googlefonts/googlesans-code)"
}
subsets: "adlam"
subsets: "canadian-aboriginal"
subsets: "cherokee"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "old-permic"
subsets: "symbols"
subsets: "symbols2"
subsets: "syriac"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 800.0
}
sample_text {
  masthead_full: "print('Hello Google!')"
  masthead_partial: "print('Hello Google!')"
  styles: "print('Hello Google!')"
  tester: "print('Hello Google!')"
  specimen_48: "f = 'Google Sans Code'\n"
  specimen_36:
    "def greet(person):\n"
    "  print(f\"Hi {person}\")\n"
  specimen_32:
    "enum Mood {\n"
    "  HAPPY,\n"
    "  CURIOUS };\n"
    "// Spread glowing vibes!\n"
    "update(Mood.HAPPY);\n"
  specimen_21:
    "<script type=\"module\">\n"
    "/* For demo purposes only! */\n"
    "const family = 'Google Sans Code';\n"
    "if (family && log || debug) {\n"
    "  log(`Font: ${family}`);\n"
    "  log(`First letter? ${family[0]}`);\n"
    "}\n"
    "</script>"
  specimen_16:
    "public static int fib(int n) {\n"
    "  a = 0;\n"
    "  b = 1;\n"
    "  result = 0;\n"
    "  for (int i = 2; i <=n; i++) {\n"
    "    result = a + b;\n"
    "    a = b\n"
    "    b = result\n"
    "  }\n"
    "  return result;\n"
    "}"
}
source {
  repository_url: "https://github.com/googlefonts/googlesans-code"
  commit: "edcd56e39fb7e98d6f1b697e187c144cef2fd994"
  archive_url: "https://github.com/googlefonts/googlesans-code/releases/download/v6.001/GoogleSansCode-v6.001.zip"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "variable/GoogleSansCode[wght].ttf"
    dest_file: "GoogleSansCode[wght].ttf"
  }
  files {
    source_file: "variable/GoogleSansCode-Italic[wght].ttf"
    dest_file: "GoogleSansCode-Italic[wght].ttf"
  }
  branch: "main"
}
