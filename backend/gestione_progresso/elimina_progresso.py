from connection import db
from flask import jsonify
from bson.objectid import ObjectId

def elimina_progresso(id):
    collection = db["progresso"]
    result = collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
