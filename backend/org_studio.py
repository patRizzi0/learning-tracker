import livelli_studio.studio_base as sb
import livelli_studio.studio_intermedio as si
import livelli_studio.studio_avanzato as sa
import livelli_studio.studio_professionale as sp

def start_study_by_level(materia_doc):
    livello = materia_doc.get("livello")

    if livello == "base":
        print("Sessioni brevi e frequenti.")
        sb.start_study_session(sb.study_time)
    elif livello == "intermedio":
        print("Sessioni moderate con pause regolari.")
        si.start_study_session(si.study_time)
    elif livello == "avanzato":
        print("Sessioni lunghe con pause strategiche.")
        sa.start_study_session(sa.study_time)
    elif livello == "professionale":
        print("Sessioni estese con focus su progetti complessi.")
        sp.start_study_session(sp.study_time)
    else:
        print("Livello non riconosciuto.")
