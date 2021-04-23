from Disciplina import Disciplina

class Aluno():

    numAlunosMatriculados = 0

    def __init__(self, ra = 0, nome = 'Sem nome', idade = 0):
        self.ra = ra
        self.nome = nome
        self.idade = idade
        self.disciplinas = []
        Aluno.numAlunosMatriculados += 1

    def __del__(self):
        print('Aluno', self.nome ,'removido')

    def cadastrarDisciplina(self, nome, nota):
        self.disciplinas.append(Disciplina(nome, nota))

    def imprimirHistorico(self):
        print('===================================')
        print('             Histórico             ')
        print('===================================')
        print('RA: ', self.ra)
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
        print('Disciplinas: ')
        for i in self.disciplinas:
            print(' - Nome: ',i.nome,' Nota: ', i.nota)
        print('===================================')
        print('')

    def fazerAniversario(self): pass