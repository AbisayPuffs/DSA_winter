class CuentaBancaria():
    def __init__(self, nom_titular, sal_inicial): 
        self.nom_titular = Titular
        self.sal_inicial = Saldo_Inicial

  
    def mostrar_info(self):
        print(f"El titular es: {self.nom_titular}su saldo es de {self.sal_inicial}")
    
    def depositar (self, cantidad): 
        self.sal_inicial= self.sal_inicial + cantidad
        print(f"el saldo es de: {self.sal_inicial}")

    def retirar(self, cantidad):
        if self.sal_inicial < cantidad:
            print ("No cuentas con el saldo suficiente")
            
        else:
            self.sal_inicial= self.sal_inicial- cantidad
            print("Si puedes retirar")

pers1= CuentaBancaria('a',100)
pers2= CuentaBancaria('b', 100)

pers1.depositar(500)
pers1.retirar(100)
pers1.mostrar_info


pers2.depositar(1000)
pers2.retirar(2000)
pers2.mostrar_info