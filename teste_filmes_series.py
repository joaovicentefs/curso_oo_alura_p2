from model import Filme, Serie, Playlist

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta - um teste', 2018, 2)
the_office = Serie('The Office', 2005, 9)
titanic = Filme('titanic', 1996, 210)
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
titanic.dar_like()
the_office.dar_like()
the_office.dar_like()
the_office.dar_like()
the_office.dar_like()
the_office.dar_like()

filmes_e_series = [vingadores, atlanta, titanic, the_office]
playlist_fds = Playlist('fim de semana', filmes_e_series)

print(f'Tamnanho da Playlist: {len(playlist_fds)}')

for programa in playlist_fds:
      # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
      # print(f'{programa.nome} - {detalhes} D - {programa.likes}')
      print(programa)