class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def getNumero(self):
        return self.__numero
    
    def getTitular(self):
        return self.__titular
    
    def getSaldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    def setNumero(self, numero):
        self.__numero = numero
    
    def setTitular(self, titular):
        self.__titular = titular
    
    #def setSaldo(self, saldo):
    #    self.__saldo = saldo

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
        

#from conta import Conta
#conta = Conta(123, "Lucas", 0.0, 1000.0)
#conta2 = Conta(321, "Maryana", 0.0, 1000.0)
