from code_to_region import *
from region import region

class regional_infection (region):
    def __init__(self,stato,codice_regione,denominazione_regione,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati):
        super().__init__(stato,codice_regione,denominazione_regione)
        self.ricoverati_con_sintomi=ricoverati_con_sintomi
        self.terapia_intensiva=terapia_intensiva
        self.totale_ospedalizzati=totale_ospedalizzati

    def get_info(self):
        print(self.stato,self.codice_regione,self.denominazione_regione,self.ricoverati_con_sintomi,self.terapia_intensiva,self.totale_ospedalizzati)
region_array = []

def introduce_regional_infection(dataframe):
    len_dataframe=len(dataframe.index)
    for i in range(0,len_dataframe,1):
        print("\nil contatore è arrivato a " +str(i))
        x=code_to_region(dataframe.loc[i,"codice_regione"])
        y=dataframe.loc[i,"stato"]
        z=dataframe.loc[i,"denominazione_regione"]
        a=dataframe.loc[i,"ricoverati_con_sintomi"]
        b=dataframe.loc[i,"terapia_intensiva"]
        c=dataframe.loc[i,"totale_ospedalizzati"]
        print (x,y,z,a,b,c)
        region_array.append(regional_infection(y,x,z,a,b,c))

