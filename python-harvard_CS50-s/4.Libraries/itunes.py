import json
import requests as r
import sys

if len(sys.argv) != 2:
    sys.exit()

response = r.get("https://itunes.apple.com/search?entity=song&song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])