from flask import Flask, request
from flask import render_template
from datetime import date
from datetime import datetime
import json

app = Flask("Hello You")

@app.route('/')
def hello():
    #Daten von JSON in datenspeicher_list eintragen
    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)

    #Die neusten drei erfassten Hausaufgaben werden auf Home angezeigt, indem nach dem Erfassungsdatum sortiert wird.
    datum_list = []
    for date in datenspeicher_list:
        datum_list.append((date["faelligkeitdatum"], date["modul"], date["titelHausaufgabe"]))

    #Sortierung der Datensätze
    #Quelle: https://docs.python.org/3/howto/sorting.html
    datum_list = sorted(datum_list, key=lambda x: x[0], reverse=True)
    datum_list = datum_list[:3]

    return render_template("index.html", datum_list=datum_list)


@app.route('/ueberblick', methods=['GET', 'POST'])
def ueberblick():
    # Daten von JSON in datenspeicher_list eintragen
    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)

    #Datenabfrage vom Formular und Datensatz löschen, sobald der Wert "Ja" angewählt wird
    #Der Name "Ja" wird vom Formular auf der Seite Ueberblick mit dem Wert/Value "titelHausaufgabe" von der Seite Ueberblick abgeglichen. Sobald dieser übereinstimmt, wird der Eintrag im JSON gelöscht.
    if request.method == 'POST':
        for eintrag in datenspeicher_list:
            if request.form.get("Ja") == eintrag["titelHausaufgabe"]:
                datenspeicher_list.remove(eintrag)
        with open("datenspeicher.json", "w") as datenbank_hausaufgaben:
            json.dump(datenspeicher_list, datenbank_hausaufgaben, indent=4, separators=(",", ":"))

    #Eigene Listen für jedes Modul, damit Einträge nach Modul von JSON ausgezogen werden können
    contentmarketing_list = []
    digitalmarketing_list = []
    innovationsmanagement_list = []
    nachhaltige_list = []
    productmanagement_list = []
    programmieren_list = []
    projektmanagement_list = []
    requirements_list = []


    #Priorität berechnen anhand der Anzahl Tage, welche vom Fälligkeitsdatum bis zum heutigen Datum sind.
    #Wenn die Fälligkeit einer Aufgabe <= 3 Tage ist, wird die Priorität Dringend vergeben etc.
    #Hilfe: https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
    today = datetime.now()
    for eintrag in datenspeicher_list:
        today = str(date.today())
        date_format = "%Y-%m-%d"
        a = datetime.strptime(eintrag["faelligkeitdatum"], date_format)
        b = datetime.strptime(today, date_format)
        delta = (b - a) * -1
        if delta.days <= 0:
            eintrag["prioritaet"] = "Fälligkeit ist vorbei!"
        elif delta.days <= 3:
            eintrag["prioritaet"] = "Dringend"
        elif delta.days <= 6:
            eintrag["prioritaet"] = "Hoch"
        elif delta.days <= 9:
            eintrag["prioritaet"] = "Mittel"
        else:
            eintrag["prioritaet"] = "Klein"

        with open("datenspeicher.json", "w") as datenbank_hausaufgaben:
            json.dump(datenspeicher_list, datenbank_hausaufgaben, indent=4, separators=(",", ":"))

    #Herausziehen der Daten von datenspeicher_liste in neue Liste für jeweilige Module
    for eintrag in datenspeicher_list:
        if eintrag["modul"] == "Content Marketing":
            contentmarketing_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Digital Marketing":
            digitalmarketing_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Innovationsmanagement":
            innovationsmanagement_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Nachhaltige Entwicklung":
            nachhaltige_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Product Management":
            productmanagement_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Programmierung 2":
            programmieren_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Projektmanagement 1":
            projektmanagement_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Requirement Engineering":
            requirements_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))


    #Anzahl Einträge in Modulen wird hier gezählt und an das HTML weitergegeben
    Zcon = len(contentmarketing_list)
    Zdigma= len(digitalmarketing_list)
    Zinno = len(innovationsmanagement_list)
    Znachhaltig = len(nachhaltige_list)
    Zproduct = len(productmanagement_list)
    Zprog = len(programmieren_list)
    Zprojekt = len(projektmanagement_list)
    Zreque = len(requirements_list)

    #Berechnung von Anteil der Module im Verhältniss zu allen fälligen Hausaufgaben
    anzahlinsgesamt = len(datenspeicher_list)
    if anzahlinsgesamt > 0:
        Anzcon = 100/anzahlinsgesamt*Zcon
        Anzcon = int(Anzcon)
        Anzdigma = 100 / anzahlinsgesamt * Zdigma
        Anzdigma = int(Anzdigma)
        Anzinno = 100 / anzahlinsgesamt * Zinno
        Anzinno = int(Anzinno)
        Anznachhaltig = 100 / anzahlinsgesamt * Znachhaltig
        Anznachhaltig = int(Anznachhaltig)
        Anzproduct = 100 / anzahlinsgesamt * Zproduct
        Anzproduct = int(Anzproduct)
        Anzprog = 100 / anzahlinsgesamt * Zprog
        Anzprog = int(Anzprog)
        Anzprojekt = 100 / anzahlinsgesamt * Zprojekt
        Anzprojekt = int(Anzprojekt)
        Anzreque = 100 / anzahlinsgesamt * Zreque
        Anzreque = int(Anzreque)

    #Damit wenn kein Eintrag besteht, keine Fehlermeldung erscheint
    else:
        Anzcon = 0
        Anzdigma = 0
        Anzinno = 0
        Anznachhaltig = 0
        Anzproduct = 0
        Anzprog = 0
        Anzprojekt = 0
        Anzreque = 0
    #Einträge in JSON speichern
    with open("datenspeicher.json", "w") as datenbank_hausaufgaben:
        json.dump(datenspeicher_list, datenbank_hausaufgaben, indent=4, separators=(",", ":"))

    return render_template("ueberblick.html", anzahlcontent=Zcon, anzahldigital=Zdigma, anzahlinno=Zinno, anzahlnachhaltig=Znachhaltig, anzahlproduct=Zproduct, anzahlprog=Zprog, anzahlprojekt=Zprojekt, anzahlreque=Zreque, contentmarketing_list=contentmarketing_list, digitalmarketing_list=digitalmarketing_list, innovationsmanagement_list=innovationsmanagement_list, nachhaltige_list=nachhaltige_list, productmanagemen_list=productmanagement_list, programmieren_list=programmieren_list, projektmanagement_list=projektmanagement_list, requirements_list=requirements_list, Anzcon=Anzcon,Anzdigma=Anzdigma,Anzinno=Anzinno, Anznachhaltig=Anznachhaltig, Anzproduct=Anzproduct, Anzprog=Anzprog, Anzprojekt=Anzprojekt, Anzreque=Anzreque)



@app.route('/erfassen', methods=['GET', 'POST'])
def erfassen():
    # Daten von JSON in datenspeicher_list eintragen
    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)

    #Datenabfrage vom Formular und abspeichern im JSON-FIle
    if request.method == 'POST':
        modul = request.form.get("modul")
        titletext = request.form.get("text_homework")
        notizen = request.form.get("textarea_notice")
        prioritaet = request.form.get("flexRadioDefault")
        faelligkeit = request.form.get("date")
        erledigt = request.form.get("flexRadioDefault1")

        datenspeicher_list.append({"modul": modul, "titelHausaufgabe": titletext, "faelligkeitdatum": faelligkeit, "prioritaet": prioritaet, "notizen": notizen, "erledigt": erledigt})
        with open("datenspeicher.json", "w") as datenbank_hausaufgaben:
            json.dump(datenspeicher_list, datenbank_hausaufgaben, indent=4, separators=(",", ":"))

        return render_template("formular.html", erfolgreich="Neue Hausaufgabe wurde erfolgreich erfasst.")

    else:
        return render_template("formular.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
