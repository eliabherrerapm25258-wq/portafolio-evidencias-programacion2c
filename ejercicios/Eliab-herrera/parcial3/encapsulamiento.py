class cuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def set_saldo(self):
        return self.__saldo
    
    def get_saldo(self, cantidad):
        return self.__saldo 
    
    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("fondo insuficiente")

    def main():
        cuenta = cuentaBancaria(5000)
        cuenta.set_saldo(-5000)
        print(cuenta.get_saldo())
        cuenta.mostrar_saldo()