class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto... {}".format(self)) #mostra o endereço do objeto
        self.__numero = numero         #acessando o objeto
        self.__titular = titular       # esses __ indicam q os atributos são privados, não podendo ser mais acessados no console, apenas através dos métodos da classe
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):        #get retorna um valor
        return self.__limite 

    @limite.setter
    def limite(self, limite):
        self.__limite = limite       #set altera um valor

    @staticmethod  #metodo estatico da classe
    def codigo_banco():
        return "001"

    @staticmethod 
    def codigos_bancos():
        return {'BB' : '001', 'caixa' : '104',  'Bradesco': '237'}
 





#print("\033[H\033[J", end="")
# conta = Conta(123, "Rodrigo", 455.0, 1000.0)
# conta2 = Conta(236,"sezar",600.0,1000.0)
# Funciona como ponteiros o negoço de referencia
# variavel = None   - faz com q a referencia pare de apontar para algo