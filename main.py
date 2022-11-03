import matplotlib.pyplot as plt
import pandas as pd
from region import *
from code_to_region import *
from covid_data import *

data=pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-20200308.csv")

introduce_regional_infection(data)

region_test=input("di quale regione vuoi vedere il grafico?    ")
len_dataframe=len(data.index)

region_array[1].get_info()


def plot_graph(region_test):
    for i in range(0,len_dataframe,1):
        if region_test == region_array[i].codice_regione:
            esami = {'ricoverati con sintomi':region_array[i].ricoverati_con_sintomi}
            plt.bar(list(esami.keys()), list(esami.values()))
            plt.title("Valutazioni covid test regione "+ region_test)
            plt.show()

plot_graph(region_test)





