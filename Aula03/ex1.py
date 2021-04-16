disciplina1 = {'disciplina': 'Algoritmos', 'sigla': 'ALG', 'periodo': 1, 'nota': 5.3}
disciplina2 = {'disciplina': 'Logica Computacional', 'sigla': 'LC', 'periodo': 1, 'nota': 6.7}
disciplina3 = {'disciplina': 'Linguagem de Programacao I', 'sigla': 'LP', 'periodo': 2, 'nota': 7.0}

disciplinas = [disciplina1, disciplina2, disciplina3]

# Descomentar linha 8 para testar lista vazia
# disciplinas = 0

def historico(disciplinas):
    if not disciplinas:
        print('A Lista de disciplinas esta vazia!')
        return

    print('===================================================')
    print('HISTORICO DO ALUNO')
    print('===================================================')
    print('')
    print('---------------------------------------------------')

    for x in disciplinas:
        print('Disciplina:', x['disciplina'])
        print('Sigla:', x['sigla'])
        print('Período:', x['periodo'])
        print('Nota:', x['nota'])

        print('---------------------------------------------------')

historico(disciplinas)