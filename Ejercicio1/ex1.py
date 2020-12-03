import random
from Persona import *

p1 = None
p2 = None
p3 = None

def generaDni():
	dniNumero = random.randrange(00000000,99999999)
	dniNumeroString = str(dniNumero).zfill(8)
	letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
	letra = letras[dniNumero%23]
	dni = dniNumeroString+letra
	return dni

def pesoIMC(peso):
    if(peso<20):
        print("Tiene infrapeso")
    elif(peso>20 and peso<25):
        print("Esta en el peso ideal")
    else:
        print("Tiene sobrepeso")

def sexo(sexo):
    if(sexo=="H"):
        return "H"
    elif(sexo=="M"):
        return "M"
    else:
        return "M"

def edad(edad):
    a = True
    if(edad>18):
        return a
    else:
        a= False
        return a


nombre1 = input("Introduce el nombre   ")
edad1 = int(input("Introduce la edad   "))
sexo1 = input("Introduce el sexo   ")
peso1 =float( input("Introduce el peso   "))
altura1 =float (  input("Introduce la altura  "))
alt1 = altura1 * altura1
pesoa1 = peso1/alt1


p1=Persona()
p1.setNombre(nombre1)
p1.setEdad(edad1)
p1.setAltura(altura1)
p1.setPeso(peso1)
p1.setSexo(sexo(sexo1))
dni1 = generaDni()
p1.setDNI(dni1)

pesoIMC(pesoa1)
b = edad(edad1)
if(b==True):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

print("Nombre: ",p1.getNombre()," Edad: ",p1.getEdad()," DNI: ",p1.getDNI()," Sexo: ",p1.getSexo()," Peso: ",p1.getPeso(), " Altura : ",p1.getAltura())


nombre2 = input("Introduce el nombre   ")
edad2 = int(input("Introduce la edad   "))
sexo2 = input("Introduce el sexo   ")
peso2 =120
altura2 =1.50
alt2 = altura2 * altura2
pesoa2 = peso2/alt2
dni2 = generaDni()

p2=Persona()
p2.setNombre(nombre2)
p2.setEdad(edad2)
p2.setAltura(altura2)
p2.setPeso(peso2)
p2.setSexo(sexo(sexo2))
p2.setDNI(dni2)

pesoIMC(pesoa2)
c = edad(edad2)
if(c==True):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

print("Nombre: ",p2.getNombre()," Edad: ",p2.getEdad()," DNI: ",p2.getDNI()," Sexo: ",p2.getSexo()," Peso: ",p2.getPeso(), " Altura : ",p2.getAltura())


nombre3 = input("Introduce el nombre   ")
edad3 = int(input("Introduce la edad   "))
sexo3 = input("Introduce el sexo   ")
peso3 =float( input("Introduce el peso   "))
altura3 =float (  input("Introduce la altura  "))
alt3 = altura3 * altura3
pesoa3 = peso3/alt3
dni3 = generaDni()

p3=Persona()
p3.setNombre(nombre2)
p3.setEdad(edad2)
p3.setAltura(altura2)
p3.setPeso(peso2)
p3.setSexo(sexo(sexo2))
p3.setDNI(dni3)

pesoIMC(pesoa3)
d = edad(edad3)
if(d==True):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

print("Nombre: ",p3.getNombre()," Edad: ",p3.getEdad()," DNI: ",p3.getDNI()," Sexo: ",p3.getSexo()," Peso: ",p3.getPeso(), " Altura : ",p3.getAltura())
