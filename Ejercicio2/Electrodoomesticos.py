class Electrodomesticos:
    precio = 100.0
    color = "Blanco"
    consumo_energetico = "F"
    peso = 5

    def __init__(self, precio, color, consumo_energetico, peso):
        self.precio = precio
        self.color = color
        self.consumo_energetico = consumo_energetico
        self.peso = peso

    def getPrecio(self):
        return self.precio

    def getColor(self):
        return self.color

    def getConsumo(self):
        return self.consumo_energetico

    def getPeso(self):
        return self.peso

    def setPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def setColor(self, nuevoColor):
        self.color = nuevoColor

    def setConsumo(self, nuevoConsumo):
        self.consumo_energetico = nuevoConsumo

    def setPeso(self, nuevoPeso):
        self.peso = nuevoPeso


    def ComprobarColor(color):
        if (color == "azul"):
            return "azul"
        elif (color == "negro"):
            return "negro"
        elif (color == "rojo"):
            return "rojo"
        else:
            return "blanco"

    def comprobarConsumo(Letra):
        if(Letra =="A"):
            return 100
        if(Letra =="B"):
            return 80
        if(Letra=="C"):
            return 60
        if(Letra =="D"):
            return 50
        if(Letra=="E"):
            return 30
        if(Letra=="F"):
            return 10