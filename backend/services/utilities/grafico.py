from connection import db
import pandas as pd
import matplotlib.pyplot as plt
import os
from flask import current_app
import os


def raccolta_dati():
    collection = db.get_collection("data")
    data = list(collection.find({}, {"_id": 0}))

    df = pd.DataFrame(data)

    if df.empty:
        return None

    df["data"] = pd.to_datetime(df["data"])
    df.set_index("data", inplace=True)

    settimanale = df.resample("D").sum()

    return settimanale