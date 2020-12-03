class Serie:
    def __init__(self, titulo="", nTemp=3, entregado=False, genero="", creador=""):
        self.titulo = titulo
        self.nTemp = nTemp
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    def entregar(self, s):
        self.entregado = True


class Videojuego:
    def __init__(self, titulo="", horasEstimadas=10, entregado=False, genero="", comp=""):
        self.titulo = titulo
        self.horasEstimadas = horasEstimadas
        self.entregado = entregado
        self.genero = genero
        self.comp = comp

    def entregarVideojuego(self, v):
        self.entregado = True


serie1 = Serie("Breaking Bad", 5, False, "Thriller", "Vince Gillian")
serie2 = Serie("Vikingos", 4, True, "Accion", "Michael Hirst")
serie3 = Serie("Juego de Tronos", 5, True, "Ciencia Ficcion", "George RR Martin")
serie4 = Serie("Me llamo Earl", 7, True, "Comedia", "Greg Garcia")
serie5 = Serie("Black Mirror", 5, True, "Ciencia Ficcion", "Charlie Brooker")

vj1 = Videojuego("Call Of Duty", 1800, False, "Shooter", "Activision")
vj2 = Videojuego("Minecraft", 5600, True, "RPG", "Microsoft/Mojang")
vj3 = Videojuego("Need For Speed", 3000, True, "Carreras", "EA")
vj4 = Videojuego("Assasins Creed", 1000, True, "Accion", "Activision")
vj5 = Videojuego("GTA", 5000, False, "RPG/Accion", "Rockstar Games")

# Entregamos serie
serie1.entregar(serie1)
print(serie1.entregado)

lista_series = [serie1, serie2, serie3, serie4, serie5]
lista_juegos = [vj1, vj2, vj3, vj4, vj5]

# Entregamos videojuego
vj1.entregarVideojuego(vj1)
print(vj1.entregado)

contSeries = 0
contVideojuego = 0

maxHorasJuego = 0
maxTempSeries = 0
vjMax = vj1
serieMax = serie1

for i in lista_series:
    if i.entregado == True:
        contSeries += 1

    if i.nTemp > maxTempSeries:
        maxTempSeries = i.nTemp
        serieMax = i

for i in lista_juegos:
    if i.entregado == True:
        contVideojuego += 1

    if i.horasEstimadas > maxHorasJuego:
        maxHorasJuego = i.horasEstimadas
        vjMax = i

print("Series entregadas: ", contSeries)
print("Juegos entregadas: ", contVideojuego)
print("Serie con mas temp:", serieMax.titulo)
print("Videojuego con mas horas:", vjMax.titulo)