from connection import db
from bson.objectid import ObjectId

def modifica_nota(id, testo_nota):
    result = db["note"].update_one({"_id": ObjectId(id)}, {"$set": {"testo": testo_nota}})
    return result.modified_count > 0