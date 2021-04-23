from Aluno import Aluno

class AlunoPosGrad(Aluno):

    def __init__(self, ra = 0, nome = 'Sem nome', idade = 0, orientador = 'Sem orientador', tese = 'Sem tese'):
        super().__init__(ra, nome, idade)

        self.orientador = orientador
        self.tese = tese

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
        print('Tese: ', self.tese)
        print('Orientador: ', self.orientador)
        print('===================================')
        print('')

    def fazerAniversario(self):
        self.idade += 1
        print('===================================')
        print('Parabéns', self.nome,'por completar',self.idade,'anos')
        print('===================================')
        print('')