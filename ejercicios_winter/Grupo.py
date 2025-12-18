class Grupo:
    def __init__(self, nombre_grupo):
        self.nombre_grupo=nombre_grupo
        self.calificaciones=[]

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def mostrar_calificacion(self):
        num_elementos= len(self.calificaciones) 

        for elemento in range (num_elementos):
            print (f"{elemento+1} {self.calificaciones[elemento]}") 
            
    def obtener_calificacion (self, indice):
        print(f"Indice: {indice} calificacion: {self.calificaciones[indice-1]}") 
        
grupo1 = Grupo("TIC's 3A")
grupo1.agregar_calificacion(8)
grupo1.agregar_calificacion(10)
grupo1.agregar_calificacion(7)
grupo1.agregar_calificacion(6)

grupo1.mostrar_calificacion()
input= int (("Dame el valor del indice: "))
grupo1.obtener_calificacion(indice)