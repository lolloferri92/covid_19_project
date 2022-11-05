import matplotlib.pyplot as plt
import pandas as pd
from region import *
from covid_data import *
from plot_graph import*
import tkinter as tk
from read_data_from_url_csv import *

while True:
    x=input()
    if x=="read_data_from_url_csv":
        data=read_data_from_url_csv()
    if x=="introduce_regional_infection":
        introduce_regional_infection(data)
    elif x=="plot_graph":
        region_test=input("di quale regione vuoi vedere i dati e stampare il grafico?    ")
        plot_graph(region_test,len(data.index))
    elif x=="exit":
        break
print("grazie per aver usato il mio primo progetto")




