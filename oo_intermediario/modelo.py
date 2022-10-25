class Programa:
    
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtidas = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def curtidas(self):
        return self._curtidas

    @curtidas.setter
    def curtidas(self, curtidas):
        self._curtidas = curtidas

    def curtir(self):
        self.curtidas += 1
    
    def imprimir(self):
        print(f"- Nome: {vingadores.nome}\n- Duracao: {vingadores.duracao}\n- Likes: {vingadores.curtidas}\n")

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def imprimir(self):
        print(f"- Nome: {self._nome}\n- Temporadas: {self.duracao}\n- Likes: {self.curtidas}\n")
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def imprimir(self):
        print(f"- Nome: {self._nome}\n- Duracao: {self.temporadas}\n- Likes: {self.curtidas}\n")

vingadores = Filme('vingadores guerra infinita', 2018, 160)
vingadores.curtir()

friends = Serie('friends', 1994, 10)
friends.curtir()

filmesSerires = [vingadores, friends]

for programa in filmesSerires:
    programa.imprimir()
    