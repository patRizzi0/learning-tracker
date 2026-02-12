#LEARNING TRACKER

import json

#1) Utente deve inserire il dato!
#2) Dato deve essere salvato in un file JSON
#3) Utente deve poter visualizzare i dati salvati
#4) Utente deve poter modificare i dati salvati


def aggiungi_materia():
    nome_materia = input("Inserisci il nome della materia: ")
    livello_attuale = input("Inserisci il livello attuale (base, intermedio, avanzato): ")
    tempo_studio = input("Inserisci il tempo di studio dedicato (in ore): ")
    dump_materia(nome_materia, livello_attuale, tempo_studio)

def dump_materia(nome_materia, livello_attuale, tempo_studio):
    materia = {
        "nome": nome_materia,
        "livello": livello_attuale,
        "tempo_studio": tempo_studio
    }
    
    # Salva dati aggiornati
    with open('backend/data.json', 'w') as file:
        json.dump(materia, file, indent=4)


#aggiungi_materia()


#Visualizza i dati salvati
def visualizza_materie():
    with open("backend/data.json", "r") as file:
        dati = json.load(file)
        
    for materia in dati:
        print(materia)

visualizza_materie()


def organizza_studio():
    with open("backend/data.json", "r") as file:
        dati = json.load(file)

        for materia in dati:
            livello = materia["livello"]

            print(livello)
            if livello == "base":
                print("Organizza sessioni di studio più brevi e frequenti.")
            elif livello == "intermedio":
                print("Aumenta gradualmente la durata delle sessioni di studio.")
            elif livello == "avanzato":
                print("Focalizzati su progetti pratici e approfondimenti.")


organizza_studio()

def progresso():
    