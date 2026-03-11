from connection import db
from bson import ObjectId
import datetime

def aggiungi_progresso(user_id, materia, ore, minuti, descrizione=""):

    if not data_creazione:
        data_creazione = datetime.datetime.now()

        tempo_totale = ore * 60 + minuti  # minuti totali

        progresso_doc = {
            "userId": user_id,
            "materia": materia,
            "tempo": tempo_totale,
            "ore": ore,
            "minuti": minuti,
            "descrizione": descrizione,        # nuovo campo
            "data_creazione": data_creazione
        }

        result = db["progresso"].insert_one(progresso_doc)
    return result.inserted_id