from gftools.push.servers import GFServers
from gftools.util.google_fonts import Metadata
from pathlib import Path
import json
import datetime
import glob
import os

gfpath = os.environ["GF_PATH"]

server_data = Path("src/data/servers.json")

if not server_data.exists():
    print(f"{server_data} not found. Generating file. This may take a while")
    servers = GFServers()
else:
    servers = GFServers.open(server_data)

servers.update_all()
servers.save(server_data)


if os.path.exists("src/data/versionhistory.json"):
    versionhistory = json.load(open("src/data/versionhistory.json"))
else:
    versionhistory = {}


for directory in glob.glob(gfpath + "/ofl/*"):
    try:
        metadata = Metadata(directory)
    except Exception as e:
        print(e)
        continue

    if metadata.name not in versionhistory:
        versionhistory[metadata.name] = {}

    for s in servers:
        if metadata.name not in s.families:
            continue
        if s.name not in versionhistory[metadata.name]:
            versionhistory[metadata.name][s.name] = []
        current_version = s.families[metadata.name].version
        versions = [x["version"] for x in versionhistory[metadata.name][s.name]]
        if current_version not in versions:
            versionhistory[metadata.name][s.name].append(
                {
                    "version": current_version,
                    "date": datetime.datetime.now().isoformat(),
                }
            )
json.dump(versionhistory, open("src/data/versionhistory.json", "w"), indent=2)
