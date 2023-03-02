class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self) -> str:
        return f"{vingadores._nome} - {vingadores.ano} - {vingadores.duracao} - {vingadores._likes}" 
  
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f"{atlanta._nome} - {atlanta.ano} - {atlanta.temporadas} - {atlanta._likes}"

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)


#     detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
#     print(f"{programa._nome} - {programa.ano} - {detalhes} - {programa._likes}")