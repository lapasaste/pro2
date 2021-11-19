from flask import Flask, request
from flask import render_template

app = Flask("Hello You")


@app.route('/home')
def hello():
    return render_template("index.html", name="Stefan")

@app.route('/ueberblick')
def ueberblick():
    return render_template("ueberblick.html")

@app.route('/erfassen', methods=['GET', 'POST'])
def erfassen():

    if request.method == 'POST':
        modul= request.form.get("modul")
        titletext = request.form.get("text_homework")
        notizen = request.form.get("textarea_notice")
        prioritaet = request.form.get("flexRadioDefault")
        faelligkeit = request.form.get("date")

        return render_template("ueberblick.html", Modul=modul, Titel=titletext, Notizen=notizen, Priorität=prioritaet, Fälligkeit=faelligkeit)


    else:
        return render_template("formular.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
