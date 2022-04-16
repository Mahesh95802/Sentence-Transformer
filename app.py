from Python.formalToCasual import formalToCasual
from Python.casualToFormal import casualToFormal
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index(): 
    if request.method == "POST":
        rec = request.form["TextBox"]
        if request.form["convertText"] == "FTC":
            return str(formalToCasual(rec))
        elif request.form["convertText"] == "CTF":
            return str(casualToFormal(rec))
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug = True)