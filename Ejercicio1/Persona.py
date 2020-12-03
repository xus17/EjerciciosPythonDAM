class Persona:
    nombre=""
    edad=0
    DNI=""
    sexo=""
    peso=0.0
    altura=0.0

    def _init_(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDNI(self):
        return self.DNI

    def getSexo(self):
        return self.sexo

    def getPeso(self):
        return self.peso

    def getAltura(self):
        return self.altura

    def setNombre(self,nuevoNombre):
        self.nombre = nuevoNombre

    def setEdad(self,nuevaEdad):
        self.edad = nuevaEdad

    def setDNI(self,nuevoDNI):
        self.DNI = nuevoDNI

    def setSexo(self,nuevoSexo):
        self.sexo = nuevoSexo

    def setPeso(self,nuevoPeso):
        self.peso = nuevoPeso

    def setAltura(self,nuevaAltura):
        self.altura = nuevaAltura
