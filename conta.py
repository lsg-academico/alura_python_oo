class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def verExtrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    #def testarInadimplencia(self, cliente):
        

#from data import Data
#conta = Conta(123, "Lucas", 0.0, 1000.0)
#conta2 = Conta(321, "Maryana", 0.0, 1000.0)
