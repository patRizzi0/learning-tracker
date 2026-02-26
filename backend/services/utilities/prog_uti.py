from connection import db
from progresso import traccia_progressi



def progresso_studio():
    materie = db["materie"]
    nome_materia = input("Inserisci il nome della materia: ").strip()

    for m in db["materie"].find():
        if m["nome"].lower() == nome_materia.lower():
            nome_materia = m["nome"]  # Usa il nome esatto dal DB
            print(f"Materia trovata: {nome_materia}")
            traccia_progressi(nome_materia)
            break

        materia_doc = materie.find_one({"nome": {"$regex": f"^{nome_materia}$", "$options": "i"}})

        if materia_doc is None:
            print(f"Materia '{nome_materia}' non trovata!")
            return

        print(nome_materia)

def read_progress():
    progressi = db["progresso"]
    return list(progressi.find())