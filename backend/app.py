# LEARNING TRACKER
from progresso import *
from org_studio import *
from services.create_sub import *
from services.delete_sub import *
from services.read_sub import *


# ----------------------------
# UTILITIES
# ----------------------------


def leggi_materie():
    materie = read_subjects()   #read_sub()
    print(materie)



def aggiungi_materia():    
    nome = input("Nome materia: ")
    livello = input("Livello: ")
    try:
        tempo = int(input("Tempo studio (ore): "))
    except ValueError:
        print("Tempo studio deve essere un numero intero.")

    create_subject(nome, livello, tempo)    #create_sub()



def rimuovi_materia():
    id_sub = get_collection("materie")
    delete_subject(id_sub)      #delete_sub()


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
    





    

# ----------------------------
# MAIN
# ----------------------------


if __name__ == "__main__":
    while True:
        print("\n1. Aggiungi materia")
        print("2. Visualizza materie")
        print("3. Organizza studio")
        print("4. Progresso studio")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            aggiungi_materia()
        elif scelta == "2":
            leggi_materie()
        elif scelta == "3":
            organizza_studio()
        elif scelta == "4":
            progresso_studio()
        else:
            print("Scelta non valida.")
