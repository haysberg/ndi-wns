import json
import requests

f = open('scraping/parsed_sauveteurs.json')
data = json.load(f)

for sauveteur in data :
    payload = json.dumps(sauveteur)
    r = requests.post("https://api.ndi.haysberg.io/sauveteurs", data=payload)
    print(r.text)