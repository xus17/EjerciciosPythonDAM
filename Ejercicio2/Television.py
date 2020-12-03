from Electrodoomesticos import *
class Television(Electrodomesticos):
    resolucion = 20
    sintonizador = False

    def _init_(self,resolucion,sintonizador):
        self.resolucion = resolucion
        self.sintonizador = sintonizador

    def getResolucion(self):
        return self.resolucion

    def getSintonizador(self):
        return self.sintonizador

    def precioFinal(self,pulgadas,sintonizador):
        if(pulgadas==40):
            self.precio += 20
        if(sintonizador==True):
            self.precio += 50