from connection import db

def read_subjects(user_id=None):
    query = {}
    if user_id:
        query["userId"] = user_id
        return list(db["materie"].find(query))