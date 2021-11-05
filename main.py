from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route('/hello')
def hello():
    return render_template("index.html", name="Stefan")

@app.route('/erfassen')
def erfassen():
    return render_template("formular.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)


