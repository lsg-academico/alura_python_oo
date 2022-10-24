class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigoBanco = "001"
        
    @property    
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def verExtrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor
    
    def __podeSacar(self, valorParaSacar):
        valorDisponivelParaSacar = self.__saldo + self.__limite
        return valorParaSacar <= valorDisponivelParaSacar

    def sacar(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite, pobrinho")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @staticmethod
    def codigoBanco():
        return "001"

    @staticmethod
    def codigosBanco():
        return {"BB": "001", "Caixa": "104", "Bradesco": "273"}
    
    #def testarInadimplencia(self, cliente):
        

#from conta import Conta
#conta = Conta(123, "Lucas", 0.0, 1000.0)
#conta2 = Conta(321, "Maryana", 0.0, 1000.0)
