import matplotlib.pyplot as plt
import pandas as pd
from region import *
from covid_data import *
from plot_graph import*
import tkinter as tk
from read_data_from_url_csv import *


if __name__ == "__main__":

    digit = ("read", "introduce", "plot", "exit")
    print("programma per visualizzazione delle statistiche del covid 19 \nImmettere una tra le seguenti funzioni: "+ str(digit))


    while True:
        x=input()
        if x==digit[0]:
            data=read_data_from_url_csv()
        elif x==digit[1]:
            introduce_regional_infection(data)
        elif x==digit[2]:
            region_test=input("di quale regione vuoi vedere i dati e stampare il grafico?    ")
            plot_graph(region_test,len(data.index))
        elif x==digit[3]:
            break
    print("grazie per aver usato il mio primo progetto")




