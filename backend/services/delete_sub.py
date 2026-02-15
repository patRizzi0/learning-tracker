from connection import db


def get_collection(name):
    if name not in db.list_collection_names():
        db.create_collection(name)
        return db[name]
    
def delete_subject(id_sub):
    materia = get_collection("materie")
    result = materia.delete_one({"_id": id_sub})
