# caixa-eletronico
Sistema de Caixa Eletronico Basico em Python

Descrição: Desenvolvi um Sistema de Caixa Eletrônico utilizando a arquitetura cliente-servidor em Python. Este sistema permite aos usuários realizarem operações bancárias básicas como consultar saldo, fazer depósitos e saques. O sistema é dividido em duas partes principais: o cliente, que interage com o usuário final, e o servidor, que autentica os usuários e gerencia as transações.
Principais Funcionalidades:
•	Autenticação de Usuários: O servidor autentica os usuários com base em uma matrícula e senha.
•	Consulta de Saldo: Permite que os usuários consultem o saldo disponível em suas contas.
•	Realização de Saques: Permite que os usuários façam saques, verificando se há saldo suficiente.
•	Realização de Depósitos: Permite que os usuários façam depósitos em suas contas.
•	Arquitetura Cliente-Servidor: O sistema é dividido em duas partes que se comunicam via socket, proporcionando uma experiência interativa e segura.
Desenvolvimento:
1.	Cliente:
o	Autenticação:
	O cliente solicita a matrícula e senha do usuário.
	As informações são enviadas ao servidor para autenticação.
o	Menu de Operações:
	Após a autenticação bem-sucedida, o cliente apresenta um menu com as opções de Saldo, Saque, Depósito e Sair.
o	Operações Bancárias:
	A opção Saldo exibe o saldo atual do usuário.
	A opção Saque permite que o usuário saque um valor, desde que haja saldo suficiente.
	A opção Depósito permite que o usuário deposite um valor na conta.
o	Encerramento:
	A opção Sair encerra a sessão do usuário e a conexão com o servidor.
2.	Servidor:
•	Autenticação:
o	O servidor recebe a matrícula e senha do cliente e verifica se as credenciais são válidas.
•	Gerenciamento de Sessões:
o	Se as credenciais forem válidas, o servidor envia uma mensagem de sucesso ao cliente e aguarda novas solicitações.
•	Encerramento:
o	O servidor encerra a conexão se o cliente optar por sair.

Conclusão: O Sistema de Caixa Eletrônico desenvolvido em Python com arquitetura cliente-servidor demonstra habilidades na criação de aplicações interativas e seguras. Utilizando sockets para a comunicação entre cliente e servidor, o projeto oferece uma solução prática para operações bancárias básicas, garantindo a autenticidade e segurança das transações.
Código:
O código completo do projeto está disponível no meu repositório GitHub, onde você pode explorar cada classe e entender a estrutura e funcionamento da aplicação.
https://github.com/rafaelcrb/caixa-eletronico.git
