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
    
