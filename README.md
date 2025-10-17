# Eco-nomia

Este é o projeto de conclusão da disciplina de Algoritmos e Programação de Computadores (APC), do curso de computação da Universidade de Brasília (UnB).
Visando reduzir o consumo elétrico e de água dos grandes datacenters que processam os inputs de inteligências Artificiais, este projeto tem como objetivo desenvolver um software para reduzir o total de tokens enviados para os grandes modelos de IA processarem e consequentemente reduzir o consumo elétrico e de água. O software utiliza um modelo de IA menor e local, para recriar o input, reduzindo o total de tokens. Após isso, ambos os inputs são submetidos para um grande modelo de IA, para que o usuário possa comparar as respostas produzidas e é realizado o cálculo de tokens submetidos, bem como o provável consumo gerado pelos servidores, através de dados médios.


## Instruções para inicializar o projeto

1. Instalação e configuração do git

    1. Baixe e instale o git através do link: https://git-scm.com/downloads
    2. Configuração do git:
        ```bash
        git config user.name 'Seu Nome'
        git config user.email 'seu_email@email.com'
        ```
    3. Clone o projeto para o seu computador
        1. abra o terminal
        2. abra a pasta onde o projeto ficará
        ```bash
        cd caminho/para/pasta
        ```
        3. faça o clone do projeto
        ```bash
        git clone https://github.com/psifabiohenrique/eco_nomia.git
        ```
    4. Escolha a ramificação que irá trabalhar
        + master:
            A versão mais estável do projeto, versão que será a final
            ```bash
            git checkout master
            ```
        + develop:
            A versão de desenvolvimento, ela irá agrupar todas as atualizações, até que possam ser enviadas para a versão master
            ```bash
            git checkout develop
            ```
        + feat/meu_recurso
            A versão com o novo recurso que você está trabalhando, você deverá criar esse ramo para contribuir com o projeto.
            ```bash
            git checkout feat/meu_recurso
            ```
            ou
            ```bash
            git checkout -b feat/meu_recurso
            ```

2. Configurando o projeto

    1. Crie um ambiente virtual
    ```bash
    python -m venv .venv
    ```
    2. Entre no ambiente virtual
    ``` bash
    .venv/scripts/activate # no windows
    source .venv/bin/activate # no linux/mac
    ```
    3. Instale as dependências do projeto
    ``` bash
    pip install -r requirements.txt
    ```
