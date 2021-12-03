from flask import Flask, request
from flask import render_template
import json

app = Flask("Hello You")


@app.route('/home')
def hello():

    return render_template("index.html", name="Stefan")

@app.route('/ueberblick')
def ueberblick():
    return render_template("ueberblick.html")

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

        datenspeicher_list.append({"faelligkeitdatum": faelligkeit, "modul": modul, "notizen": notizen, "prioritaet": prioritaet, "titelHausaufgabe": titletext})
        with open("datenspeicher.json", "w") as f:
            json.dump(datenspeicher_list, f, indent=4, separators=(",", ":"), sort_keys=True)

        return render_template("ueberblick.html", Modul=modul, Titel=titletext, Notizen=notizen, Priorität=prioritaet, Fälligkeit=faelligkeit)


    else:
        return render_template("formular.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
