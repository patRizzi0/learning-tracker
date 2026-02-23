    

from backend.services.operations.create_sub import get_collection
from backend.services.operations.delete_sub import delete_subject


def rimuovi_materia():
    id_sub = get_collection("materie")
    delete_subject(id_sub)      #delete_sub()
