import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import time
import json

with open("sauveteurs_urls", "r") as sauveteurs:
    sauveteurs_urls = [line.strip() for line in sauveteurs.readlines()]

data = {}

for sauveteur_url in sauveteurs_urls:
    status_code = 500
    while status_code != 200:
        sauveteur_request = requests.get(sauveteur_url)
        status_code = sauveteur_request.status_code
        time.sleep(0.2)

    print("="*80)
    print(sauveteur_url)

    sauveteur_page_soup = BeautifulSoup(
        sauveteur_request.text,
        'html.parser'
    )

    content_block = sauveteur_page_soup.find("div", {"class": "entry clr"}) 

    for tag in content_block.find_all(re.compile('^h[1-6]|p$')):
        if tag.name == "h1":
            sauveteur_name = tag.text
            data[sauveteur_name] = {}
            continue
        if "h" in tag.name:
            last_heading = tag.text 
            data[sauveteur_name][last_heading] = ""
            print("aaa")
        else:
            try:
                if tag.text:
                    data[sauveteur_name][last_heading] += f"{tag.text}\n"
            except KeyError:
                pass
    with open("sauveteurs.json", "w+") as sauveteurs_json:
        sauveteurs_json.write(
            json.dumps(data, indent=4, ensure_ascii=False)
        )
