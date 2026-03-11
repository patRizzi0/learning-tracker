from connection import db

def leggi_note(user_id=None):
    query = {}
    if user_id:
        query["userId"] = user_id
    return list(db["note"].find(query))