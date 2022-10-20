from wsgiref.validate import validator


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto... {}".format(self)) #mostra o endereço do objeto
        self.numero = numero         #acessando o objeto
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


