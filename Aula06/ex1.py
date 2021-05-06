import sys

class Aluno():

    def __init__(self, ra = 0, nome = 'Sem nome'):
        try:
            raCheck(ra)
        except RANotValidError as r:
            print('----------------------------------------------')
            print(r)
            print('O valor do RA deve estar entre 800000 e 999999')
            print('----------------------------------------------')
            exit()
        else:
            self.ra = ra

        self.nome = nome

class RANotValidError(Exception):
    def __str__(self):
        return '⚠ ERRO: RA não é válido ⚠'

def raCheck (ra):
    if ra < 800000 or ra > 999999:
        raise RANotValidError()
    return

###################################################
### MAIN FLOW
###################################################

if len(sys.argv) == 1:
    arquivo = input("Informe o nome do arquivo: ")
else:
    arquivo = sys.argv[1]

try:
    f = open(arquivo, 'rt')
except IOError as io:
    print('----------------------------------------------')
    print('⚠ ERRO AO LER ARQUIVO INFORMADO ⚠')
    print(io)
    print('----------------------------------------------')
    exit()

informacoes = f.readlines()

print('')
print('Criando primeiro aluno...')
print('')
aluno = Aluno(int(informacoes[0].strip()), informacoes[1])

print('RA:',aluno.ra)
print('NOME:',aluno.nome)

print('Criando aluno com RA inválido...')
print('')
alunoExeption = Aluno(int(informacoes[2].strip()), informacoes[3])

print('RA:',alunoExeption.ra)
print('NOME:',alunoExeption.nome)

f.close()