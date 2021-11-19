
import json

import main

homework_dict = {"Modul": ["modul"],
    "Titel der Hausaufgabe": ["text_homework"],
    "Notizen": ["textarea_notice"],
    "Priorität": ["flexRadioDefault"],
    "Fälligkeitsdatum": ["date"]
                 }

print(homework_dict)

with open("datenspeicher.json", "w") as f:
    json.dump(homework_dict, f, indent=4, separators=(",", ":"), sort_keys=True)