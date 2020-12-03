from Electrodoomesticos import *


class Lavadora(Electrodomesticos):
    carga = 5

    def __init__(self,carga):
        self.carga = carga

    def precioFinal(self,carga):
        if (carga>30):
            self.precio += 50
        else:
            print("No se añade nada")

    def getCarga(self):
        return self.carga