from connection import db
import time

def aggiungi_progresso():
    titolo = input("Titolo del progresso: ")
    descrizione = input("Descrizione del progresso: ")
    data = time.strftime("%Y-%m-%d %H:%M:%S")  # Ottieni la data e ora attuali
    cosa_imparo = input("Cosa hai imparato oggi? ")
    nome_materia = input("Nome della materia: ")
    materia_id = input("ID materia: ")

    progresso = db["progresso"]
    progresso.insert_one({
        "materia_id": materia_id,
        "nome_materia": nome_materia,
        "data": data,
        "titolo_progresso": titolo,
        "descrizione": descrizione,
        "cosa_imparato": cosa_imparo
    })

    print(f"Progresso per {nome_materia} salvato ✅")
