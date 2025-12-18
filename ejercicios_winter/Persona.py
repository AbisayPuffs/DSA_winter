class Persona:

    def __init__ (self, nombre, edad):
        self.nombre= nombre
        self.edad= edad

    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} anios")

    
    def  es_mayor(self):
        return self.edad >= 18
        
pers1 = Persona("Juan L", 28)
pers2 = Persona("Mario R", 15)

pers1.saludar()
pers2.saludar()

print(pers1.es_mayor())       
print(pers2.es_mayor())

print(pers2.nombre)