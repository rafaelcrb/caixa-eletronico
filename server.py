#Codigo Servidor
from socket import *
import os
HOST = '127.0.0.1'
PORTA = 50000

tcp = socket(AF_INET, SOCK_STREAM)
tcp.bind((HOST, PORTA))
tcp.listen(1)
print('Aguardando Login . . . ')

while True:
    conexao, endereco = tcp.accept()
    print('Conectado por', endereco)

    while True:
        matricula = conexao.recv(1024)
        print('Matricula: ', matricula.decode())
        senha = conexao.recv(1024)
        print('Senha: ', senha.decode())

        if (matricula.decode() == '12861333430' and senha.decode() == '123456'):
            mensagem = 'Logado'
            conexao.send(mensagem.encode())

            opcao = conexao.recv(1024)
            if (opcao.decode() == '4'):
                print('Finalizando a Conexão . . . ') 
                conexao.close()
                break

        else:
            mensagem = 'Falha'
            conexao.send(mensagem.encode())