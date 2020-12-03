from Electrodoomesticos import *
from Lavadora import *
from Television import *

e1 = Electrodomesticos(precio=100,color="blanco",consumo_energetico="F",peso=5)
e2 = Electrodomesticos(precio = 150,color="blanco",consumo_energetico="F",peso=15)
e3 = Electrodomesticos(precio=200,color="azul",consumo_energetico="A",peso=20)
l1 = Lavadora(carga=5)
l2 = Lavadora(carga=5)
l2.precio=140
l2.peso= 16
l2.color="blanco"
l3 = Lavadora(carga=10)
l3.precio=130
l3.peso=34
l3.consumo_energetico="B"
l3.carga=10
l3.color="negro"
t1 = Television(20,False,consumo_energetico="F",peso=5)
t1.setColor("blanco")

t2 = Television(20,False,peso=20,consumo_energetico="F")
t2.setColor("blanco")
t3 = Television(32,True,consumo_energetico="C",peso=22)

t3.precio=300

t3.color="negro"
t4 = Television(27,False,consumo_energetico="F",peso=21)
t4.precio=400
t4.color="azul"

array = [e1,e2,e3,l1,l2,l3,t1,t2,t3,t4]

precioT =0
precioE =0
precioL=0
d=0
for  i in array:

    if d<3:
        d = d+1
        print("Precio ",i.getPrecio()," Color: ",i.getColor()," Consumo energético ", i.getConsumo(), " Peso: ",i.getPeso())
        precioE = precioE + i.getPrecio()
    elif(d>2 and d<6):
        d= d+1
        precioL = precioL + i.getPrecio()
        print("Precio ", i.getPrecio(), " Color: ", i.getColor(), " Consumo energético ", i.getConsumo(), " Peso: ",i.getPeso(), " Carga: ",i.getCarga())
    elif(d>5):
        print("Precio ", i.getPrecio(), " Color: ", i.getColor(), " Consumo energético ", i.getConsumo(), " Peso: ",i.getPeso(), " Resolucion: ",i.getResolucion(), " Sintonizado: ",i.getSintonizador())
        precioT =precioT + i.getPrecio()


print("ELECTRODOMESTICOS: ",precioE)
print("LAVADORAS: ",precioL)
print("TELEVISORES: ",precioT)
total = precioL + precioT +precioE
print("TOTAL: ",total)