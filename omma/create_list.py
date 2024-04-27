import pandas as pd

def create_list():
    data = pd.read_csv("source.csv")
    licences = data["License No."].tolist()
    return licences