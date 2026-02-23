from backend.connection import db
from backend.org_studio import start_study_by_level

def organizza_studio():
    # ottieni la collezione dal DB
    materie = db["materie"]  # o get_collection("materie")

    # chiedi quale materia vuole studiare
    nome_materia = input("Inserisci il nome della materia: ")

    # recupera il documento dal DB
    materia_doc = materie.find_one({"nome": nome_materia})

    if materia_doc is None:
        print(f"Materia '{nome_materia}' non trovata!")
        return

    print(f"Livello della materia: {materia_doc['livello']}")
    start_study_by_level(materia_doc)   

