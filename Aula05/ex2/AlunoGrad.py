from Aluno import Aluno

class AlunoGrad(Aluno):

    def __init__(self, ra = 0, nome = 'Sem nome', idade = 0):
        super().__init__(ra, nome, idade)

        self.media = 0

    def calcularMedia(self):
        total = 0

        for item in self.disciplinas:
            total += item.nota

        self.media = total / len(self.disciplinas)

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
        print('Média: ', round(self.media, 1))
        print('===================================')
        print('')

    def fazerAniversario(self):
        self.idade += 1
        print('===================================')
        print('Parabéns', self.nome,'por completar',self.idade,'anos')
        print('===================================')
        print('')

