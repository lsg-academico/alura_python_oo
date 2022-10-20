
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto... {}".format(self)) #mostra o endereço do objeto
        self.numero = numero         #acessando o objeto
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


