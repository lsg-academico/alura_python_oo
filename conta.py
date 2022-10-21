class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto... {}".format(self)) #mostra o endereço do objeto
        self.__numero = numero         #acessando o objeto
        self.__titular = titular       # esses __ indicam q os atributos são privados, não podendo ser mais acessados no console, apenas através dos métodos da classe
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)







# Funciona como ponteiros o negoço de referencia
# variavel = None   - faz com q a referencia pare de apontar para algo