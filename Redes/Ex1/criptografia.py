MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, chave, mode):
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    dado = ''
    for c in data:
        index = alfabeto.find(c)
        if index == -1:
            dado += c
        else:
            cript_index = index + chave if mode == MODE_ENCRYPT else index - chave
            cript_index = cript_index % len(alfabeto)
            dado += alfabeto[cript_index:cript_index+1]
    return dado

###################################################
### MAIN FLOW
###################################################

chave = input("Informe o número de posições de deslocamento na cifra: ")

original = 'Esse é o meu primeiro algoritmo de criptografia de César'
print('Mensagem Original:', original)
criptografada = caesar(original, int(chave), MODE_ENCRYPT)
print('Mensagem Criptografada:', criptografada)
descriptografada = caesar(criptografada, int(chave), MODE_DECRYPT)
print('Mensagem Decriptografada:', descriptografada)