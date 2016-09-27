import json

d = {
    "af": "sfa",
    "sdf": {
        "asf": "egs",
        "as": "asf",
        "af": [
            "Asf",
            "sdaf",
            {
                "saf": "Adf"
            }
        ]
    }
}

with open("a.ini", "w+") as f:
    json.dump(d, f, indent=4)
print(json.dumps(d, indent=4))

from configparser import ConfigParser
import csv

con = ConfigParser()
con["do"] = {"what": "true", "isit": "false", "adsf": ["adf", "adfs"]}

with open("b.ini", "w+") as f:
    con.write(f)

seq = con["do"]["adsf"]
parser = csv.reader(seq)
for fields in parser:
    print(fields)
    for i, f in enumerate(fields):
        print(i, f)

# con["do"]["adsf"] = ["Adsf", "new", "what"]
print(con["do"]["adsf"])
