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

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores guerra infinita', 2018, 160)
vingadores.curtir()
print(f"- Nome: {vingadores.nome}\n- Temporadas: {vingadores.ano}\n- Likes: {vingadores.curtidas}\n")

friends = Serie('friends', 1994, 10)
friends.curtir()
print(f"- Nome: {friends.nome}\n- Temporadas: {friends.temporadas}\n- Likes: {friends.curtidas}")
