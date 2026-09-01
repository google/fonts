import requests
from bs4 import BeautifulSoup as Soup
from gflanguages import LoadScripts, languages_public_pb2
from gftools.util.google_fonts import WriteProto
from google.protobuf.json_format import ParseDict

SCRIPT_CODE_URL = "https://www.unicode.org/iso15924/iso15924-codes.html"
SKIP_SCRIPTS = {
    "Cyrs",
    "Egyd",
    "Egyh",
    "Hanb",
    "Hang",
    "Hntl",
    "Hrkt",
    "Jamo",
    "Seal",
}


def fetch_script_codes():
    response = requests.get(SCRIPT_CODE_URL)
    response.raise_for_status()
    soup = Soup(response.text, "html.parser")

    script_codes = []
    table = soup.find("table", {"class": "simple"})
    for row in table.find_all("tr")[1:]:  # Skip header row
        cols = row.find_all("td")
        if len(cols) >= 2:
            code = cols[0].text.strip()
            name = cols[2].text.strip()
            script_codes.append((code, name))

    return script_codes


known_scripts = LoadScripts()
for code, name in fetch_script_codes():
    if code[0] == "Z" or code[0] == "Q" or code in SKIP_SCRIPTS or "variant" in name:
        continue
    if code not in known_scripts:
        print(f"Adding script {code} - {name}")
        message = ParseDict(
            {
                "id": code,
                "name": name,
            },
            languages_public_pb2.ScriptProto(),
        )
        WriteProto(message, f"Lib/gflanguages/data/scripts/{code}.textproto")
