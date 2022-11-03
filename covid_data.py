from region import region

class regional_infection (region):
    def __init__(self,stato,denominazione_regione,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati):
        super().__init__(stato,denominazione_regione)
        self.ricoverati_con_sintomi=ricoverati_con_sintomi
        self.terapia_intensiva=terapia_intensiva
        self.totale_ospedalizzati=totale_ospedalizzati

    def get_info(self):
        print(self.stato,self.denominazione_regione,self.ricoverati_con_sintomi,self.terapia_intensiva,self.totale_ospedalizzati)
region_array = []

def introduce_regional_infection(dataframe):
    len_dataframe=len(dataframe.index)
    for i in range(0,len_dataframe,1):
        #print("\nil contatore è arrivato a " +str(i))
        y=dataframe.loc[i,"stato"]
        z=dataframe.loc[i,"denominazione_regione"]
        a=dataframe.loc[i,"ricoverati_con_sintomi"]
        b=dataframe.loc[i,"terapia_intensiva"]
        c=dataframe.loc[i,"totale_ospedalizzati"]
        region_array.append(regional_infection(y,z,a,b,c))
    print("creazione delle regioni e inserimento dei dati completato")

