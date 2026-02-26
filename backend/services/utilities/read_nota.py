from connection import db

def leggi_note():
    note = list(db["note"].find())
    return note