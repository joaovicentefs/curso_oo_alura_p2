class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando Cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas no fórum')

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

jose = Junior()
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()
# jose.busca_cursos_do_mes() <- Erro, pois o objeto Jose não tem acesso ao atributo da Classe, apenas o Pleno

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

# MRO (Method Resolution Order) -> Algoritmo do Python para saber qual o método deverá usar no nosso caso ficaria assim:
# Pleno > Alura > Funcionario > Caelum > Funcionário -> mas tem duplicata, não é uma 'good head'
# Good head é quando não tem nenhum classe abaixo que eu não possa usar.
# Então ficaria assim:
# Pleno > Alura > Caelum > Funcionário -> Removemos a duplicidade e mantamos o Caelum que é o Good head