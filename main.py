import pandas as pd
from region import *
from code_to_region import *
from covid_data import *

data=pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-20200308.csv")

introduce_regional_infection(data)
region_array[3].get_info()






