# LEARNING TRACKER

import datetime


from flask import Flask, jsonify, redirect, render_template, url_for
from flask import request
from services.utilities import edit_nota
from services.operations import read_sub
from services.utilities import read_nota
from services.utilities import add_nota
from services.operations import create_sub
from gestione_progresso import elimina_progresso   
from connection import db
from flask import jsonify
from services.utilities.prog_uti import read_progress


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lista_progressi")
def lista_progressi():
    progressi = read_progress()
    return render_template("lista_progressi.html", progressi=progressi)



@app.route("/elimina_progressi/<id>", methods=["DELETE"])
def elimina_progressi(id):
    elimina_progresso.elimina_progresso(id)
    return jsonify({"success": True})



@app.route("/materie", methods=["GET", "POST"])
def materie():

    materie = read_sub.read_subjects()

    if request.method == "POST":

        nome = request.form.get("nome_materia")
        livello = int(request.form.get("difficolta"))
        ore = int(request.form.get("ore"))
        minuti = int(request.form.get("minuti"))

        tempo = ore * 60 + minuti

        create_sub.create_subject(nome, livello, tempo)

        return redirect(url_for("materie"))

    return render_template("materie.html", materie=materie)




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


@app.route("/modifica_nota/<id>", methods=["POST"])
def modifica_nota(id):
    data = request.get_json()
    testo_nota = data.get("testo")
    edit_nota.modifica_nota(id, testo_nota)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)