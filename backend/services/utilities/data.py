from connection import db
import pandas as pd

def raccolta_dati():
    collection = db.get_collection("data")
    data = list(collection.find({}, {"_id": 0}))

    df = pd.DataFrame(data)

    df["data"] = pd.to_datetime(df["data"])

    df.set_index("data", inplace=True)

    settimanale = df.resample("W").sum()
    
    return settimanale


