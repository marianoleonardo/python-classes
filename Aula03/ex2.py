disciplina1 = {'disciplina': 'Algoritmos', 'sigla': 'ALG', 'periodo': 1, 'nota': 5.3}
disciplina2 = {'disciplina': 'Logica Computacional', 'sigla': 'LC', 'periodo': 1, 'nota': 6.7}
disciplina3 = {'disciplina': 'Linguagem de Programacao I', 'sigla': 'LP', 'periodo': 2, 'nota': 7.0}

disciplinas = [disciplina1, disciplina2, disciplina3]

aluno = "Leonardo"

# Descomentar linha 8 para testar lista vazia
# disciplinas = 0

def concat(disciplinas, aluno):
    media = 0.0
    if not disciplinas:
        print('A Lista de disciplinas esta vazia!')
        return

    nomeConcat = aluno + " - SI"

    for x in disciplinas:
        media = (media + x['nota'])

    media /= len(disciplinas)

    lista = [nomeConcat, media]

    return lista

lista = concat(disciplinas, aluno)

print('===================================================')
print('MEDIA DO ALUNO')
print('===================================================')
print('')
print('Aluno:', lista[0])
print('Media:', round(lista[1], 1))