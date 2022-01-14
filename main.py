from flask import Flask, request
from flask import render_template
from datetime import datetime
import json

app = Flask("Hello You")

@app.route('/')
def hello():
    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)

    # Anzeigen der drei neusten Einträge auf Home
    datum_list = []
    for date in datenspeicher_list:
        datum_list.append((date["faelligkeitdatum"], date["modul"], date["titelHausaufgabe"]))

    # Quelle: https://docs.python.org/3/howto/sorting.html
    datum_list = sorted(datum_list, key=lambda x: x[0], reverse=True)
    datum_list = datum_list[:3]

    return render_template("index.html", datum_list=datum_list)


@app.route('/ueberblick', methods=['GET', 'POST'])
def ueberblick():
    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)

    #Mit Jinja stylen
    #Daten nach Modul aus JSON ziehen und weiter für HTML geben
    contentmarketing_list = []
    digitalmarketing_list = []
    innovationsmanagement_list = []
    nachhaltige_list = []
    productmanagement_list = []
    programmieren_list = []
    projektmanagement_list = []
    requirements_list = []

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

        elif eintrag["modul"] == "Programmieren 2":
            programmieren_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Projektmanagement 1":
            projektmanagement_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

        elif eintrag["modul"] == "Requirement Engineering":
            requirements_list.append((eintrag["erledigt"], eintrag["titelHausaufgabe"], eintrag["faelligkeitdatum"], eintrag["notizen"], eintrag["prioritaet"]))

    # for status in contentmarketing_list:
    #     if status[3] == "dringend":
    #         newstatus = status
    #     else:
    #         contentmarketing_list.append(status)


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

   # Procon = 100/anzahlinsgesamt*Zcon

    # Datenabfrage vom Formular und abspeichern im JSON-FIle
    # Nach einer Abfrage funktioniert es nicht mehr, da ich die Liste nicht udpate, sondern erfasse...
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

        return render_template("ueberblick.html", anzahlcontent=Zcon, anzahldigital=Zdigma, anzahlinno=Zinno, anzahlnachhaltig=Znachhaltig, anzahlproduct=Zproduct, anzahlprog=Zprog, anzahlprojekt=Zprojekt, anzahlreque=Zreque, contentmarketing_list=contentmarketing_list, digitalmarketing_list=digitalmarketing_list, innovationsmanagement_list=innovationsmanagement_list, nachhaltige_list=nachhaltige_list, productmanagemen_list=productmanagement_list, programmieren_list=programmieren_list, projektmanagement_list=projektmanagement_list, requirements_list=requirements_list, Anzcon=Anzcon,Anzdigma=Anzdigma,Anzinno=Anzinno, Anznachhaltig=Anznachhaltig, Anzproduct=Anzproduct, Anzprog=Anzprog, Anzprojekt=Anzprojekt, Anzreque=Anzreque, erfolgreich="Die Hausaufgabe wurde erledigt")

    else:
        # Datenabfrage vom Formular und abspeichern im JSON-FIle
        return render_template("ueberblick.html", anzahlcontent=Zcon, anzahldigital=Zdigma, anzahlinno=Zinno, anzahlnachhaltig=Znachhaltig, anzahlproduct=Zproduct, anzahlprog=Zprog, anzahlprojekt=Zprojekt, anzahlreque=Zreque, contentmarketing_list=contentmarketing_list, digitalmarketing_list=digitalmarketing_list, innovationsmanagement_list=innovationsmanagement_list, nachhaltige_list=nachhaltige_list, productmanagemen_list=productmanagement_list, programmieren_list=programmieren_list, projektmanagement_list=projektmanagement_list, requirements_list=requirements_list, Anzcon=Anzcon,Anzdigma=Anzdigma,Anzinno=Anzinno, Anznachhaltig=Anznachhaltig, Anzproduct=Anzproduct, Anzprog=Anzprog, Anzprojekt=Anzprojekt, Anzreque=Anzreque)





@app.route('/erfassen', methods=['GET', 'POST'])
def erfassen():
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
