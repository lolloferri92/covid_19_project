import pandas as pd

def read_data_from_url_csv():
    y=input("immettere l'url del csv che vuoi importare (immettere il piu recente)")

    data=pd.read_csv(y)

    return data