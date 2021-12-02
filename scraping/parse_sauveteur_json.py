import json
import re

with open("sauveteurs.json", "r") as sauveteurs_json:

    sauveteurs = json.loads(sauveteurs_json.read())

parsed_data = {}

for sauveteur, data in sauveteurs.items():
    parsed_data[sauveteur] = {}

    for key, value in data.items():

        if not key:
            continue

        if key.replace("/", "").isnumeric():
            if not 'key_dates' in parsed_data[sauveteur].keys():
                parsed_data[sauveteur]["key_dates"] = {}   
            parsed_data[sauveteur]["key_dates"][key.strip()] = re.sub(' {2,}',' ', value.strip())
            continue

        if not value:
            if not 'solo_info' in parsed_data[sauveteur].keys():
                parsed_data[sauveteur]["solo_info"] = []  
            parsed_data[sauveteur]["solo_info"].append(re.sub(' {2,}',' ', key.strip()))
            continue

        parsed_data[sauveteur][key] = re.sub(' {2,}',' ', value.strip())

with open("parsed_sauveteurs.json", "w") as out_file:

    out_file.write(json.dumps(parsed_data, indent=4, ensure_ascii=False))
        
