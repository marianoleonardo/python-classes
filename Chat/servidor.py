#!/usr/bin/python3

import socket
import sys


ipServidor = '127.0.0.1'
portaServidor = 1234


# ------------------------------------------------------------------------
# INICIA O SERVIDOR
# ------------------------------------------------------------------------

# prepara o socket do servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 'pugla' o socket na pilha de sockets do S.O.
sock.bind((ipServidor, portaServidor))

print("")
nick = str(input("Digite seu nickname: "))
print("")

# ------------------------------------------------------------------------
# AGUARDA CONEXÃO DO CLIENTE
# ------------------------------------------------------------------------

print('Aguardando conexão na porta', str(portaServidor) + '...', end=' ')
sys.stdout.flush()
sock.listen()

# ------------------------------------------------------------------------
# ACEITA CONEXÃO DE UM CLIENTE
# ------------------------------------------------------------------------

conn, host = sock.accept()
enderecoCliente, portaClient = host

print('-> conectado com cliente em', enderecoCliente + ':' + str(portaClient))

while True:
    print("")
    print("Aguardando mensagem do cliente...")
    print("")
    # ------------------------------------------------------------------------
    # RECEBE DADOS DO CLIENTE
    # ------------------------------------------------------------------------

    # recebe mensagem do cliente (em ascii)
    mensagemASC = conn.recv(1024)

    # converte mensagem recebida para string
    mensagem = mensagemASC.decode("utf-8")

    print(mensagem)
    print("")

    # ------------------------------------------------------------------------
    # ENVIA DADOS PARA O CLIENTE
    # ------------------------------------------------------------------------

    mensagem = str(input("Digite uma mensagem > "))

    mensagem = nick + ': ' + mensagem

    # converte a mensagem de resposta para ascii (o mesmo que: b'Pong')
    mensagemASC = mensagem.encode('ascii')

    # envia a resposta ao cliente (em ascii)
    conn.sendall(mensagemASC)

