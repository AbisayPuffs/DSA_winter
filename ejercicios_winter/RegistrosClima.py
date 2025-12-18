class RegistroClimas:
    def __init__(self):
        self.climas = []

    def agregar_clima(self, temperatura):
        self.climas.append(temperatura)

    def mostrar_climas(self):
        total_elementos = len(self.climas)
        for indice in range(total_elementos):
            print(f"{indice + 1} {self.climas[indice]}")

    def contar_mayores_a(self, limite):
        climas_mayores = 0  # cuenta cuántos climas mayores hay 

        for clima in self.climas:
            if clima > limite:
                climas_mayores += 1
        return climas_mayores  # tiene que estar dentro del método para que se regrese, que esté dentro del for 


registro_verano = RegistroClimas()

registro_verano.agregar_clima(15)
registro_verano.agregar_clima(20)
registro_verano.agregar_clima(25)
registro_verano.agregar_clima(30)
# lista completa
registro_verano.mostrar_climas()

limite_dado = 18
cantidad_mayores = registro_verano.contar_mayores_a(limite_dado)

print(registro_verano.contar_mayores_a(22))