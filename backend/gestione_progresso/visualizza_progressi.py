from connection import db
import time

def visualizza_progressi(nome_materia, materia_id):
    progresso = db["progresso"]
    progressi = list(progresso.find({"nome_materia": nome_materia, "materia_id": materia_id}).sort("data", -1))  # ordina per data decrescente
    if not progressi:
        print(f"Nessun progresso registrato per la materia '{nome_materia}'.")
        return

    print("Progressi registrati:")
    for doc in progressi:
        print(f"ID materia: {doc['materia_id']}")
        print(f"Materia: {doc['nome_materia']}")
        print(f"Data: {doc['data']}")
        print(f"Titolo: {doc['titolo_progresso']}")
        print(f"Cosa imparato: {doc['cosa_imparato']}\n")