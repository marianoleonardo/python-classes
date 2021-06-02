#!/usr/bin/env python3

##########################################################################
### CLIENTE.PY
##########################################################################

import socket


ipServidor = '127.0.0.1'
portaServidor = 1234


# ------------------------------------------------------------------------
# INICIA O CLIENTE
# ------------------------------------------------------------------------

# cria o socket do cliente para se conectar ao servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("")
nick = str(input("Digite seu nickname: "))
print("")

# ------------------------------------------------------------------------
# CONEXÃO COM O SERVIDOR
# ------------------------------------------------------------------------

print('Tentando conexão...', end=' ')
sock.connect((ipServidor, portaServidor))
print('-> conectado com', ipServidor + ':' + str(portaServidor))
print("")

# ------------------------------------------------------------------------
# ENVIA DADOS PARA O SERVIDOR
# ------------------------------------------------------------------------

while True:
    mensagem = str(input("Digite uma mensagem > "))

    mensagem = nick + ': ' + mensagem

    # converte mensagem para ascii (o mesmo que: b'Ping')
    mensagemASC = mensagem.encode('ascii')

    # envia mensagem ao servidor (em ascii)
    sock.sendall(mensagemASC)

    print("")
    print("Aguardando resposta do servidor...")
    print("")

    # ------------------------------------------------------------------------
    # RECEBE RESPOSTA DO SERVIDOR
    # ------------------------------------------------------------------------

    # recebe resposta do servidor (em ascii)
    respostaASC = sock.recv(1024)

    # converte mensagem para string
    resposta = respostaASC.decode("utf-8")

    print(resposta)
    print("")