from connection import db
from datetime import datetime
import gestione_progresso.aggiungi_progresso as ag
import gestione_progresso.visualizza_progressi as vs

def traccia_progressi(nome_materia):
    materie = db["materie"]
    materia_doc = materie.find_one({"nome": nome_materia})

    materia_str = materia_doc["nome"]   #Collection "MATERIE" -> campo "NOME"
    materia_id = materia_doc["_id"]
    
    print(f"Materia: {nome_materia} (ID: {materia_id})")

    if not materia_doc:
        print("Materia non trovata.")
        return

    scelta = input("Vuoi aggiungere un nuovo progresso (1) o visualizzare i progressi esistenti (2)? ")

    if scelta == "1":
        ag.aggiungi_progresso(materia_str, materia_id)
    elif scelta == "2":
        vs.visualizza_progressi(materia_str, materia_id)
    else:
        print("Scelta non valida. Riprova.")
