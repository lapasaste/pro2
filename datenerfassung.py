
import json

homework_dict = {"Modul": ["modul"],
    "Titel der Hausaufgabe": ["text_homework"],
    "Notizen": ["textarea_notice"],
    "Priorität": ["flexRadioDefault"],
    "Fälligkeitsdatum": ["date"],
    "Erledigt": ["flexRadioDefault1"]

}
print(homework_dict)

with open("datenspeicher.json", "w") as datenbank_hausaufgaben:
    json.dump(homework_dict, datenbank_hausaufgaben, indent=4, separators=(",", ":"))