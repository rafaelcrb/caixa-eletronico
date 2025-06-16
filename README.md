# Caixa Eletrônico (Cliente-Servidor)

Um sistema básico de caixa eletrônico implementado em Python, utilizando uma arquitetura cliente-servidor para operações bancárias como consulta de saldo, depósito e saque.

## ✨ Funcionalidades

*   **Autenticação de Usuários**: Validação de matrícula e senha.
*   **Consulta de Saldo**: Permite verificar o saldo disponível na conta.
*   **Realização de Saques**: Permite sacar valores, com verificação de saldo.
*   **Realização de Depósitos**: Permite depositar valores na conta.
*   **Arquitetura Cliente-Servidor**: Comunicação via sockets para uma experiência interativa e segura.

## 🚀 Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Sockets**: Para comunicação de rede entre cliente e servidor.

## ⚙️ Instalação e Execução

Para rodar este projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   Python 3.x

### Passos

1.  Clone o repositório:
    ```bash
    git clone https://github.com/rafaelcrb/caixa-eletronico.git
    cd caixa-eletronico
    ```
2.  **Iniciar o Servidor** (em um terminal):
    ```bash
    python server.py
    ```
    O servidor indicará que está aguardando conexões.

3.  **Iniciar o Cliente** (em outro terminal):
    ```bash
    python client.py
    ```
    O cliente se conectará ao servidor e apresentará as opções de operação.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


