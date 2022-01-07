from flask import Flask, request
from flask import render_template
import json

app = Flask("Hello You")

@app.route('/')
def hello():
    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)


    datum_list = []
    for date in datenspeicher_list:
        datum_list.append((date["faelligkeitdatum"], date["modul"], date["titelHausaufgabe"]))


    datum_list = sorted(datum_list, key=lambda x: x[0], reverse=True)
    datum_list = datum_list[:3]

    return render_template("index.html", datum_list=datum_list)


@app.route('/ueberblick')
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

    for eintrag in datenspeicher_list:
        if eintrag["modul"] == "Content Marketing":
            contentmarketing_list.append(eintrag)

        elif eintrag["modul"] == "Digital Marketing":
            digitalmarketing_list.append(eintrag)

        elif eintrag["modul"] == "Innovationsmanagement":
            innovationsmanagement_list.append(eintrag)

        elif eintrag["modul"] == "Nachhaltige Entwicklung":
            nachhaltige_list.append(eintrag)

        elif eintrag["modul"] == "Product Management":
            productmanagement_list.append(eintrag)

        elif eintrag["modul"] == "Programmieren 2":
            programmieren_list.append(eintrag)


        elif eintrag["modul"] == "Projektmanagement 1":
            projektmanagement_list.append(eintrag)

        elif eintrag["modul"] == "Requirement Engineering":
            requirements_list.append(eintrag)

    #Anzahl Einträge in Modulen
    Zcon = len(contentmarketing_list)
    Zdigma= len(digitalmarketing_list)
    Zinno = len(innovationsmanagement_list)
    Znachhaltig = len(nachhaltige_list)
    Zproduct = len(productmanagement_list)
    Zprog = len(programmieren_list)
    Zprojekt = len(projektmanagement_list)
    Zreque = len(requirements_list)

    return render_template("ueberblick.html", anzahlcontent=Zcon, anzahldigital=Zdigma, anzahlinno=Zinno, anzahlnachhaltig=Znachhaltig, anzahlproduct=Zproduct, anzahlprog=Zprog, anzahlprojekt=Zprojekt, anzahlreque=Zreque, contentmarketing=contentmarketing_list, digitalmarketing=digitalmarketing_list, innovationsmanagement=innovationsmanagement_list, nachhaltigeentwicklung=nachhaltige_list,productmanagement=productmanagement_list, programmieren=programmieren_list, projektmanagement=projektmanagement_list, requirements=requirements_list)



@app.route('/erfassen', methods=['GET', 'POST'])
def erfassen():
    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)

    if request.method == 'POST':
        modul = request.form.get("modul")
        titletext = request.form.get("text_homework")
        notizen = request.form.get("textarea_notice")
        prioritaet = request.form.get("flexRadioDefault")
        faelligkeit = request.form.get("date")

        datenspeicher_list.append({"modul": modul, "titelHausaufgabe": titletext, "faelligkeitdatum": faelligkeit, "prioritaet": prioritaet, "notizen": notizen})
        with open("datenspeicher.json", "w") as datenbank_hausaufgaben:
            json.dump(datenspeicher_list, datenbank_hausaufgaben, indent=4, separators=(",", ":"))

        return render_template("ueberblick.html", testii=datenspeicher_list[0])

    else:
        return render_template("formular.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
