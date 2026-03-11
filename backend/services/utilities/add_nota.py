from connection import db

def aggiungi_nota(user_id, testo_nota, data_creazione):

    if not user_id:
        raise ValueError("user_id mancante")

    nota_doc = {
        "userId": user_id,          
        "testo": testo_nota,
        "data_creazione": data_creazione
    }

    result = db["note"].insert_one(nota_doc)
    return result.inserted_id