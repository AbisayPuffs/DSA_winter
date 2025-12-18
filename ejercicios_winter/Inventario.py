class Inventario:
 
    def __init__(self):
        self.productos={}

    def agregar_producto(self,codigo, precio):
        if codigo not in self.productos: 
            self.productos[codigo] = precio

    def mostrar_productos(self):
       for codigo in self.productos:
           print(f'{codigo} $ {self.productos[codigo]}.00')

    def consultar_precio(self, codigo ): 
       if codigo in self.productos: 
           print(f'{codigo} $ {self.productos[codigo]}.00') 
kfe = Inventario()
kfe.agregar_producto('coca', 15)
kfe.agregar_producto('cheetos', 18)
kfe.agregar_producto('caguama',47)
kfe.mostrar_productos() 

kfe.consultar_precio('cheetos')