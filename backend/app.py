# LEARNING TRACKER

import datetime

from flask import Flask, redirect, render_template, url_for
from flask import request
from services.utilities import read_nota
from services.utilities import add_nota
from services.operations import create_sub
from connection import db
from services.utilities.prog_uti import read_progress


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lista_progressi")
def lista_progressi():
    progressi = read_progress()
    return render_template("lista_progressi.html", progressi=progressi)

@app.route("/materie", methods=["GET", "POST"])
def materie():

    if request.method == "POST":

        nome = request.form.get("nome_materia")
        livello = int(request.form.get("difficolta"))
        ore = int(request.form.get("ore"))
        minuti = int(request.form.get("minuti"))

        tempo = ore * 60 + minuti

        create_sub.create_subject(nome, livello, tempo)

        return redirect(url_for("materie"))

    return render_template("materie.html")


@app.route("/note", methods=["GET", "POST"])
def note():

    note = read_nota.leggi_note()

    if request.method == "POST":
        data_creazione = datetime.datetime.now()
        nota = request.form.get("notaTesto")

        if nota and nota.strip() != "":
            add_nota.aggiungi_nota(nota.strip(), data_creazione)

            return redirect(url_for("note"))



    return render_template("note.html", note=note)



if __name__ == "__main__":
    app.run(debug=True)