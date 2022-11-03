class region():

    def __init__(self,stato,denominazione_regione):
        self.stato=stato
        self.denominazione_regione=denominazione_regione
        #print("regione " + denominazione_regione +" costruita")

    def get_info(self):
        print(self.stato,self.denominazione_regione)



