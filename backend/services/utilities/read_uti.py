from backend.services.operations.read_sub import read_subjects


def leggi_materie():
    materie = read_subjects()   #read_sub()
    print(materie)