# LEARNING TRACKER

import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, redirect, render_template, url_for, session, request
from services.utilities import edit_nota, read_nota, add_nota
from services.operations import read_sub, create_sub
from gestione_progresso import elimina_progresso
from services.utilities.grafico import raccolta_dati
from services.utilities.read_prog import read_progress
from connection import db  # tua connessione esistente MongoDB
from bson import ObjectId
from services.utilities.add_prog import aggiungi_progresso

app = Flask(__name__)
app.secret_key = "ebreo_super_segreto"  # necessario per session

# -----------------------
# Decorator per protezione rotte private
# -----------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "userId" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

    # -----------------------
    # REGISTER
    # -----------------------
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if db["utenti"].find_one({"email": email}):
            return render_template("register.html", error="Email già registrata")

        password_hash = generate_password_hash(password, method="scrypt")
        db["utenti"].insert_one({"email": email, "passwordHash": password_hash})

        return render_template("register.html", message="Utente creato con successo")

    return render_template("register.html")


        # -----------------------
        # LOGIN
        # -----------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        utente = db["utenti"].find_one({"email": email})
        if not utente:
            return render_template("login.html", error="Email non trovata")

        if not check_password_hash(utente["passwordHash"], password):
            return render_template("login.html", error="Password errata")

        # Login corretto
        session["userId"] = str(utente["_id"])
        return redirect(url_for("lista_progressi"))

    return render_template("login.html")


        # -----------------------
        # LOGOUT
        # -----------------------
@app.route("/logout")
@login_required
def logout():
    session.pop("userId", None)
    return redirect("/login")


# -----------------------
# HOME / DASHBOARD
# -----------------------

@app.route("/home")
@login_required
def home():
    user_id = session["userId"]
    return render_template("home.html")
"""
@app.route("/lista_progressi", methods=["GET", "POST"])
@login_required
def lista_progressi():
    user_id = ObjectId(session["userId"])

    progressi = read_progress(user_id)

    if request.method == "POST":
        # Recupera i dati dal form
        materia_id = request.form.get("materia")  # sarà l'id della materia
        descrizione = request.form.get("descrizione", "")
        ore = int(request.form.get("ore", 0))
        minuti = int(request.form.get("minuti", 0))

        # Recupera il nome della materia dal DB
        materia_doc = db["materie"].find_one({"_id": ObjectId(materia_id)})
        nome_materia = materia_doc["nome"] if materia_doc else "Materia sconosciuta"

        # Salva il progresso
        aggiungi_progresso(user_id, nome_materia, ore, minuti, descrizione)

        # Ricarica progressi aggiornati
    progressi = read_progress(user_id)

    return render_template("lista_progressi.html", progressi=progressi)
"""

@app.route("/lista_progressi", methods=["GET", "POST"])
@login_required
def lista_progressi():
    user_id = ObjectId(session["userId"])

    ###### Recupera tutte le materie dell'utente
    materie = list(db["materie"].find({"userId": user_id}).sort("nome", 1))

    progressi = read_progress(user_id)

    if request.method == "POST":
        materia_id = request.form.get("materia")
        descrizione = request.form.get("descrizione", "")
        ore = int(request.form.get("ore", 0))
        minuti = int(request.form.get("minuti", 0))

        materia_doc = db["materie"].find_one({"_id": ObjectId(materia_id)})
        nome_materia = materia_doc["nome"] if materia_doc else "Materia sconosciuta"

        # Salva il progresso
        aggiungi_progresso(user_id, nome_materia, ore, minuti, descrizione)

        # Ricarica progressi aggiornati
        progressi = read_progress(user_id)

        # Passa anche le materie al template
    return render_template("lista_progressi.html", progressi=progressi, materie=materie)


# -----------------------
# ELIMINA PROGRESSI
# -----------------------
@app.route("/elimina_progressi/<id>", methods=["DELETE"])
@login_required
def elimina_progressi(id):
    elimina_progresso.elimina_progresso(id)
    return jsonify({"success": True})

# -----------------------
# MATERIE
# -----------------------
@app.route("/materie", methods=["GET", "POST"])
@login_required
def materie():
    user_id=ObjectId(session["userId"])
    materie = read_sub.read_subjects(user_id)

    if request.method == "POST":
        nome = request.form.get("nome_materia")
        livello = int(request.form.get("difficolta"))
        ore = int(request.form.get("ore"))
        minuti = int(request.form.get("minuti"))

        tempo = ore * 60 + minuti
        create_sub.create_subject(user_id, nome, livello, tempo)

        return redirect(url_for("materie"))

    return render_template("materie.html", materie=materie)


    # -----------------------
    # NOTE
    # -----------------------
@app.route("/note", methods=["GET", "POST"])
@login_required
def note():
    user_id=ObjectId(session["userId"])
    note = read_nota.leggi_note(user_id)

    if request.method == "POST":
        data_creazione = datetime.datetime.now()
        nota = request.form.get("notaTesto")
        if nota and nota.strip() != "":
            add_nota.aggiungi_nota(user_id, nota.strip(), data_creazione)
            return redirect(url_for("note"))

    return render_template("note.html", note=note)


@app.route("/modifica_nota/<id>", methods=["POST"])
@login_required
def modifica_nota(id):
    user_id = session["userId"]
    data = request.get_json()
    testo_nota = data.get("testo")
    edit_nota.modifica_nota(user_id, id, testo_nota)
    return jsonify({"success": True})


# -----------------------
# API E GRAFICO
# -----------------------
@app.route("/api/ore_settimanali")
@login_required
def ore_settimanali():
    dati = raccolta_dati()
    if dati is None:
        return jsonify({"labels": [], "values": []})

    labels = [str(x.date()) for x in dati.index]
    values = dati["ore"].tolist()

    return jsonify({"labels": labels, "values": values})


    # -----------------------
    # RUN APP
    # -----------------------
if __name__ == "__main__":
    app.run(debug=True)