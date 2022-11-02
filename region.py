from code_to_region import *

class region():

    def __init__(self,stato,codice_regione,denominazione_regione):
        self.stato=stato
        self.codice_regione=codice_regione
        self.denominazione_regione=denominazione_regione
        print("regione " + codice_regione +" costruita")

    def get_info(self):
        print(self.stato,self.codice_regione,self.denominazione_regione)



