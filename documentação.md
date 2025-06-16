# Documentação Técnica - Caixa Eletrônico (Cliente-Servidor)

## 1. Visão Geral

Este projeto implementa um sistema básico de caixa eletrônico utilizando uma arquitetura cliente-servidor. O `server.py` atua como o backend que gerencia as operações bancárias (saque, depósito, consulta de saldo), enquanto o `client.py` fornece a interface para o usuário interagir com o sistema.

## 2. Estrutura do Projeto

A estrutura do projeto é simples e direta, consistindo em dois arquivos principais:

```
caixa-eletronico/
├── client.py                   # Código do cliente (interface do usuário)
├── server.py                   # Código do servidor (lógica de negócio e banco de dados)
└── README.md                   # Arquivo de documentação do projeto
```

## 3. Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Sockets**: Para comunicação entre o cliente e o servidor.

## 4. Funcionalidades Principais

### Servidor (`server.py`)

*   Gerencia contas de usuários (armazenamento em memória ou arquivo simples).
*   Processa requisições de saque, depósito e consulta de saldo.
*   Valida transações (saldo suficiente, valores válidos).
*   Comunica-se com o cliente via sockets.

### Cliente (`client.py`)

*   Fornece uma interface de linha de comando para o usuário.
*   Permite ao usuário realizar operações de saque, depósito e consulta de saldo.
*   Envia requisições ao servidor e exibe as respostas.

## 5. Fluxo de Operação

1.  O `server.py` é iniciado e fica aguardando conexões de clientes.
2.  O `client.py` é iniciado e tenta se conectar ao servidor.
3.  Após a conexão, o cliente envia requisições ao servidor (ex: 


saque, depósito, consulta).
4.  O servidor processa a requisição, atualiza o estado (saldo) e envia uma resposta de volta ao cliente.
5.  O cliente exibe a resposta ao usuário.

## 6. Configuração e Execução

Para configurar e executar o projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   Python 3.x

### Instalação

Não há dependências externas complexas. Basta clonar o repositório:

```bash
git clone https://github.com/rafaelcrb/caixa-eletronico.git
cd caixa-eletronico
```

### Execução

1.  **Iniciar o Servidor** (em um terminal):
    ```bash
    python server.py
    ```
    O servidor indicará que está aguardando conexões.

2.  **Iniciar o Cliente** (em outro terminal):
    ```bash
    python client.py
    ```
    O cliente se conectará ao servidor e apresentará as opções de operação.

## 7. Considerações de Desenvolvimento

*   Este é um projeto simplificado para demonstrar a comunicação cliente-servidor via sockets.
*   O armazenamento de dados (contas e saldos) é feito de forma básica, provavelmente em memória ou em um arquivo simples, e não é persistente entre as execuções do servidor.
*   Não há tratamento robusto de erros ou segurança de rede implementados neste exemplo.
*   Pode ser expandido para incluir autenticação de usuário, persistência de dados em banco de dados, e tratamento de múltiplas conexões de clientes.

