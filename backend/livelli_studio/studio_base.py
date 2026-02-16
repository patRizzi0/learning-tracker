import time


# sessione di studio - difficoltà: base

study_time = 10 * 60  # durata in secondi (15 minuti)

def start_study_session(s_time):
    print("Inizio della sessione di studio.")
    while s_time > 0:
        minuti = s_time // 60
        secondi = s_time % 60
        print(f"{minuti:02d}:{secondi:02d}", end="\r")

        time.sleep(1)  # pause d'une seconde
        s_time -= 1
    print("Sessione completata!")
