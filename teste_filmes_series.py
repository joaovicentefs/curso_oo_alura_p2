from model import Filme, Serie

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atltanta = Serie('nao sei', 2018, 2)
atltanta.nome = 'atlanta - um teste'
atltanta.dar_like()
atltanta.dar_like()
print(f'Nome: {atltanta.nome} - Ano: {atltanta.ano} '
      f'Duração: {atltanta.temporadas} - Likes: {atltanta.likes}')

#Aula do modulo 3, aula 2, polimorfismo

filmes_e_series = [vingadores, atltanta]
for programa in filmes_e_series:
      detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
      print(f'{programa.nome} - {detalhes} D - {programa.likes}')
