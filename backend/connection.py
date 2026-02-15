from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.learning_tracker

utenti = db.utenti

risultato = utenti.find()

for utente in risultato:
    print(utente["nome"] + " " + utente["cognome"])