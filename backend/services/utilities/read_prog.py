from connection import db

def read_progress(user_id=None):
    query = {}
    if user_id:
        query["userId"] = user_id 
        return list(db["progressi"].find(query))