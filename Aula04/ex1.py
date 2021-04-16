import os
from time import sleep
opcao = 0
n = 10

def main(n):
    opcao = 0

    print('===================================================')
    print('MENU PRINCIPAL')
    print('===================================================')
    print('')
    print('1. Alterar o valor de N ( Atual = ',n,')')
    print('2. Gerar a lista usando o comando FOR')
    print('3. Gerar a lista usando a função MAP')
    print('4. Gerar a lista usando a função FILTER')
    print('5. Gerar a lista usando uma função geradora')
    print('6. Encerrar o programa')
    print('')
    opcao = int(input('Digite uma opção (de 1 a 6): '))

    clear()

    return opcao

def clear():
    os.system('cls')

def printLista(lista):
    if not list:
        print('A Lista está vazia!')
        return

    print('Lista: ', end='')

    print(lista)

    return

def alteraN (n):
    print('Valor de N ( Atual = ',n,')')
    n = int(input('Mudar para: '))

    return n

def listaFor(n):
    lista = []

    for n in range(1 , n + 1):
        if n % 2 != 0:
            lista.append(n)

    printLista(lista)

    return

def listaMap(n):
    m = list(map(lambda item:item * 2 - 1, range(1,n+1)))

    if n % 2 != 0:
        printLista(m[:int(n / 2) + 1])

    else:
        printLista(m[:int(n / 2)])

    return

def listaFilter(n):
    lista = list(filter(lambda item: item % 2 != 0, range(1,n+1)))

    printLista(lista)

    return

def listaFuncaoGeradora(n):

    for n in range(1 , n + 1):
        if n % 2 != 0:
            yield n

###################################################
### MAIN FLOW
###################################################

while (True):
    opcao = main(n)

    if opcao == 1:
        # ALTERAR O VALOR DE N
        n = alteraN (n)
        clear()

    elif opcao == 2:
        # GERAR LISTA COM FOR
        listaFor(n)
        sleep(3)
        clear()

    elif opcao == 3:
        # GERAR LISTA COM MAP
        listaMap(n)
        sleep(3)
        clear()

    elif opcao == 4:
        # GERAR LISTA COM FILTER
        listaFilter(n)
        sleep(3)
        clear()

    elif opcao == 5:
        # GERAR LISTA COM FUNÇÃO GERADORA
        listafuncaoGeradora = list(listaFuncaoGeradora(n))
        printLista(listafuncaoGeradora)
        sleep(3)
        clear()

    elif opcao == 6:
        # ENCERRAR PROGRAMA
        print('Encerrando a execução do programa...')
        sleep(2)
        clear()
        quit()

    else:
        # VALOR INVÁLIDO
        print('Digite um valor válido')
        sleep(2)
        clear()