import matplotlib.pyplot as plt
from covid_data import *

def plot_graph(region_test,len):
    for i in range(0,len,1):
        if region_test == region_array[i].denominazione_regione:

            region_array[i].get_info()

            esami = {'ricoverati con sintomi':region_array[i].ricoverati_con_sintomi,}
            plt.bar(list(esami.keys()), list(esami.values()))
            plt.title("Valutazioni covid test regione "+ region_test)
            plt.show()

