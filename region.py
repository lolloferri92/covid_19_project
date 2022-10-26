from code_to_region import *

class region():

    def __init__(self,stato,codice_regione,denominazione_regione):
        self.stato=stato
        self.codice_regione=codice_regione
        self.denominazione_regione=denominazione_regione
        print("regione " + codice_regione +" costruita")

    def get_info(self):
        print(self.stato,self.codice_regione,self.denominazione_regione)

region_array = []

def introduce_region(dataframe):

    len_dataframe=len(dataframe.index)


    for i in range(0,len_dataframe,1):

        print("\nil contatore è arrivato a " +str(i))
        x=code_to_region(dataframe.loc[i,"codice_regione"])
        y=dataframe.loc[i,"stato"]
        z=dataframe.loc[i,"denominazione_regione"]
        region_array.append(region(y,x,z))

