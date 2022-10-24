class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #se trata de uma propriedade
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()     #transforma toda primeira letra em maiuscula

    @nome.setter 
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome