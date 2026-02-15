from connection import db


def get_collection(name):
    if name not in db.list_collection_names():
        db.create_collection(name)
        return db[name]
    
def read_subjects():
    materia = get_collection("materie")
    return list(materia.find())