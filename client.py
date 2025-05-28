#Codigo Cliente
from socket import *
import stdiomask
import os

HOST = '127.0.0.1'
PORTA = 50000

conexao = socket(AF_INET, SOCK_STREAM)
conexao.connect((HOST, PORTA))

while True:

    matricula = input('Digite Sua Matricula: ')
    senha = stdiomask.getpass (prompt='Senha: ', mask= '*')

    conexao.send(matricula.encode())
    conexao.send(senha.encode())

    resposta = conexao.recv(1024)
    print('Status . . . ', resposta.decode())

    saldo = 0
    opcao = 0
    enviar = '4'   

    while (opcao != 4):
        if (resposta.decode() == 'Logado'):
            os.system('cls')
            print('Login realizado com sucesso! ')
            print('===========================')
            print('     MENU:                 ')
            print('===========================')
            print('     [1] - Saldo     ')
            print('     [2] - Saque     ')
            print('     [3] - Deposito  ')
            print('     [4] - Sair      ')
            print('===========================')
            opcao = int(input('Digite uma Opção: '))

            if (opcao == 4 ):
                print('Saindo da Conta, Até Mais! ')
                print('===========================')
                conexao.send(enviar.encode())
                exit()
                                
            if (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
                print('Opção Inválida.')
                os.system('pause')
                continue
           
            #Saldo
            if (opcao == 1):
                print('===========================') 
                print ('Saldo Atual é R$', saldo)   
                print('                        ')
                
            #Saque
            elif (opcao == 2):
                print('===========================')
                saque = float(input('Digite o Valor que Deseja Sacar: '))
                print('===========================')
                if (saque <= saldo):
                    print('R$', saque, 'Foi Sacado.')
                    print('                        ')
                    saldo = saldo - saque
                else:
                    print('Saldo Insuficiente, Seu Saldo é R$', saldo)
                
            #Deposito
            elif (opcao == 3):
                print('===========================')
                deposito = float(input('Digite o valor que deseja depositar: '))
                print('===========================')
                print('R$', deposito, 'Foi Depositado.')
                print('                        ')
                saldo = saldo + deposito
                            
            os.system('pause')
            os.system('cls')

             
        else:
            print('Matricula ou senha incorreta, tente novamente! ')
            break
        