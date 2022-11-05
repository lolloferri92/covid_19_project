import pandas as pd

def read_data_from_url_csv():
    y=input("immettere l'url del csv che vuoi importare (immettere il piu recente)")


    #story_days_number=input("vuoi vedere lo storico di quanti giorni passati altri?")


    #for


    data=pd.read_csv(y)
    #https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-20200309.csv
    return data