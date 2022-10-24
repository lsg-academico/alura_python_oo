#from typing_extensions import Self
class Conta:
    
    #def __init__(self):
    #        print("Construindo objeto ... {}".format(self))
    #        self.numero=123
    #        self.titular="nico"
    #        self.saldo=55.0
    #        self.limit=1000.0
    
    
    #def cria_conta(numero, titular, saldo, limite):
        
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        
        #dois _ na frente do atributo, ele vira private
        
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))
        
    def deposita(self,valor):
        self.__saldo += valor
        
    def saca(self,valor):
        self.__saldo -= valor
        
 #   def transfere(self,valor,origem,destino):
 #       origem.saca(valor)
 #       destino.deposita(valor)
 
    def transfere(self,valor,origem,destino):
        self.saca(valor)
        destino.deposita(valor)
    
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    
    #numero
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self,numero):
        self.__numero=numero
    
    #titular
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular=titular
    
    #saldo
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo=saldo
    
    #limite
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self,limite):
        self.__limite=limite
        
        
