from connection import db

def create_subject(user_id, nome, livello, tempo):
    if not user_id:
        raise ValueError("user_id mancante")
    
    materia_doc = {
        "userId": user_id,
        "nome": nome,
        "livello": livello,
        "tempo_studio": tempo
    }

    result = db["materie"].insert_one(materia_doc)
    return result.inserted_id