from Aluno import Aluno
from AlunoGrad import AlunoGrad
from AlunoPosGrad import AlunoPosGrad

aluno1 = AlunoGrad(102214, 'Leonardo H Mariano', 21)

aluno1.cadastrarDisciplina('Estrutura de dados', 9.5)
aluno1.cadastrarDisciplina('Banco de dados', 8.5)
aluno1.cadastrarDisciplina('Paradigmas de programação', 10)

aluno1.calcularMedia()

aluno2 = AlunoPosGrad(5425, 'Fabiano Berardo', 40, 'Diego Negretto', 'Os impactos da IA na sociedade')

aluno2.cadastrarDisciplina('Estrutura de dados', 9.5)
aluno2.cadastrarDisciplina('Banco de dados', 8.5)
aluno2.cadastrarDisciplina('Paradigmas de programação', 10)
aluno2.cadastrarDisciplina('IA', 10)
aluno2.cadastrarDisciplina('IoT', 8)

listaAlunos = [aluno1, aluno2]

for i in listaAlunos:
    i.imprimirHistorico()
    i.fazerAniversario()

print('===================================')
print('Total de alunos:', Aluno.numAlunosMatriculados)
print('===================================')