class Cliente:
    
    def __init__(self, nome):
        self.nome = nome
        
    def getNome(self):
        return self.nome.title()
    
    def setNome(self, nome):
        self.nome = nome