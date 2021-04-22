class Disciplina():
    def __init__(self, nome='Disciplina 1', sigla='DC1', nota=1.0):
        self.nome = nome
        self.sigla = sigla
        self.nota = nota

    def __del__(self):
        print('Disciplina',self.nome,'removida')

    def imprimirDados(self):
        print('Nome:', self.nome)
        print('Sigla:', self.sigla)
        print('Nota:', self.nota)

disciplina1 = Disciplina()

disciplina2 = Disciplina('Disciplina 2', 'DC2', 2.0)

disciplina3 = Disciplina()
disciplina3.nome = 'Disciplina 3'
disciplina3.sigla = 'DC3'
disciplina3.nota = 3.0

disciplina1.imprimirDados()
disciplina2.imprimirDados()
disciplina3.imprimirDados()

del disciplina1
del disciplina2
del disciplina3