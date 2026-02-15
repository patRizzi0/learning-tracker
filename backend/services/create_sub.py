from connection import db


def get_collection(name):
    if name not in db.list_collection_names():
        db.create_collection(name)
        return db[name]

def create_subject(nome, livello, tempo):
    materia = get_collection("materie")
    materia.insert_one({
        "nome": nome,
        "livello": livello,
        "tempo_studio": tempo
    })

print("Materia aggiunta con successo.")
