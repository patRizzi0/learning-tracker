from connection import db
from datetime import datetime
from progresso.aggiungi_progresso import aggiungi_progresso
from progresso.visualizza_progressi import visualizza_progressi

def traccia_progressi(scelta):
    materie = db["materie"]
    nome_materia = input("Inserisci il nome della materia: ").strip()
    materia_doc = materie.find_one({"nome": nome_materia})
    if(scelta == "1"):
        aggiungi_progresso(materia_doc)
    elif(scelta == "2"):
        visualizza_progressi(materia_doc)
    else:
        print("Scelta non valida. Riprova.")


scelta = input("Vuoi aggiungere un nuovo progresso (1) o visualizzare i progressi esistenti (2)? ")

traccia_progressi(scelta)