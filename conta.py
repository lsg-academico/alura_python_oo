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
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite