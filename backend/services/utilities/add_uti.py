
from backend.services.operations.create_sub import create_subject


def aggiungi_materia():
    nome = input("Nome materia: ")
    livello = input("Livello: ")
    try:
        tempo = int(input("Tempo studio (ore): "))
    except ValueError:
        print("Tempo studio deve essere un numero intero.")

        create_subject(nome, livello, tempo)    #create_sub()