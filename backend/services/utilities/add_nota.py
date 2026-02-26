from connection import db

def aggiungi_nota(testo_nota, data_creazione):
    nota = db["note"].insert_one({"testo": testo_nota, "data_creazione": data_creazione})
    return nota 