from model import  Filme, Serie

filme = Filme('vingadores - guerra infinita', 2018, 160)
filme.dar_like()
print(f'Nome: {filme.nome} - Ano: {filme.ano} '
      f'Duração: {filme.duracao} - Likes: {filme.likes}')

serie = Serie('nao sei', 2018, 2)
serie.nome = 'atlanta - um teste'
serie.dar_like()
serie.dar_like()
print(f'Nome: {serie.nome} - Ano: {serie.ano} '
      f'Duração: {serie.temporadas} - Likes: {serie.likes}')