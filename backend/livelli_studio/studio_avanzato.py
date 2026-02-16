import time


# sessione di studio - difficoltà: base

study_time = 1 * 60  # durata in minuti

def start_study_session(s_time):
    print("Inizio della sessione di studio.")
    while s_time > 0:
        print(f"Tempo restante: {s_time}")
        time.sleep(1)  # pause d'une seconde
        s_time -= 1
        print("Sessione completata!")
