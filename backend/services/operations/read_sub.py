from connection import db

def read_subjects():
    materia = db["materie"]
    return list(materia.find())