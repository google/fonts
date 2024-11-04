name: "Karantina"
designer: "Rony Koch"
license: "OFL"
category: "DISPLAY"
date_added: "2021-03-12"
fonts {
  name: "Karantina"
  style: "normal"
  weight: 300
  filename: "Karantina-Light.ttf"
  post_script_name: "Karantina-Light"
  full_name: "Karantina Light"
  copyright: "Copyright 2020 The Karantina Project Authors (https://github.com/ronykoch/Karantina)"
}
fonts {
  name: "Karantina"
  style: "normal"
  weight: 400
  filename: "Karantina-Regular.ttf"
  post_script_name: "Karantina-Regular"
  full_name: "Karantina Regular"
  copyright: "Copyright 2020 The Karantina Project Authors (https://github.com/ronykoch/Karantina)"
}
fonts {
  name: "Karantina"
  style: "normal"
  weight: 700
  filename: "Karantina-Bold.ttf"
  post_script_name: "Karantina-Bold"
  full_name: "Karantina Bold"
  copyright: "Copyright 2020 The Karantina Project Authors (https://github.com/ronykoch/Karantina)"
}
subsets: "hebrew"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/ronykoch/Karantina"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/TTF/Karantina-Light.ttf"
    dest_file: "Karantina-Light.ttf"
  }
  files {
    source_file: "fonts/TTF/Karantina-Regular.ttf"
    dest_file: "Karantina-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/Karantina-Bold.ttf"
    dest_file: "Karantina-Bold.ttf"
  }
  branch: "main"
}
