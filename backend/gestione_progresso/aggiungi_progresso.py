from connection import db
import time

def aggiungi_progresso(nome_materia, materia_id):
    titolo = input("Titolo del progresso: ")
    descrizione = input("Descrizione del progresso: ")
    data = time.strftime("%Y-%m-%d %H:%M:%S")  # Ottieni la data e ora attuali
    cosa_imparo = input("Cosa hai imparato oggi? ")
    

    progresso = db["progresso"]
    progresso.insert_one({
        "materia_id": materia_id,
        "nome_materia": nome_materia,
        "data": data,
        "titolo_progresso": titolo,
        "descrizione": descrizione,
        "cosa_imparato": cosa_imparo
    })

    