# LEARNING TRACKER

import json
import os
from backend.services.create_sub import *
from backend.services.delete_sub import *
from backend.services.read_sub import *


DATA_PATH = "backend/data.json"


# ----------------------------
# UTILITIES
# ----------------------------

def leggi_materie():
    materie = read_subjects()
    print(materie)

def aggiungi_materia():    
    nome = input("Nome materia: ")
    livello = input("Livello: ")
    try:
        tempo = int(input("Tempo studio (ore): "))
    except ValueError:
        print("Tempo studio deve essere un numero intero.")

    create_subject(nome, livello, tempo)



def rimuovi_materia():
    id_sub = get_collection("materie")
    print(id_sub)


def organizza_studio():
    materie = leggi_materie()

    for materia in materie:
        livello = materia["livello"]

        print(f"\nSuggerimenti per {materia['nome']}:")

        if livello == "base":
            print("Sessioni brevi e frequenti.")
        elif livello == "intermedio":
            print("Aumenta gradualmente la durata.")
        elif livello == "avanzato":
            print("Focalizzati su progetti pratici.")
        else:
            print("Livello non riconosciuto.")


            # ----------------------------
            # MAIN
            # ----------------------------

if __name__ == "__main__":
    while True:
        print("\n1. Aggiungi materia")
        print("2. Visualizza materie")
        print("3. Organizza studio")
        print("4. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            aggiungi_materia()
        elif scelta == "2":
            visualizza_materie()
        elif scelta == "3":
            organizza_studio()
        elif scelta == "4":
            break
        else:
            print("Scelta non valida.")
