# Meu Programa de Registro de Refeições

## Descrição

Este programa permite aos usuários registrar refeições feitas, editar, excluir, listar todas as refeições registradas e visualizar uma refeição específica. As informações das refeições são armazenadas em um banco de dados SQLite.

## Funcionalidades

- **Registrar uma refeição feita:** Os usuários podem registrar uma refeição feita fornecendo as seguintes informações:
  - Nome da refeição
  - Descrição da refeição
  - Data e hora da refeição
  - Se a refeição está dentro ou não da dieta

- **Editar uma refeição:** Os usuários têm a capacidade de editar todas as informações de uma refeição previamente registrada.

- **Excluir uma refeição:** Os usuários podem excluir uma refeição registrada do banco de dados.

- **Listar todas as refeições:** Os usuários podem ver uma lista de todas as refeições registradas.

- **Visualizar uma única refeição:** Os usuários podem visualizar detalhes específicos de uma refeição, incluindo nome, descrição, data e hora, e se está dentro ou não da dieta.

## Tecnologias Utilizadas

- Flask: Framework web em Python para criar o backend da aplicação.
- SQLAlchemy: Biblioteca para interagir com o banco de dados SQLite.
- SQLite: Banco de dados utilizado para armazenar as informações das refeições.

## Requisitos de Instalação

- Python 3.x
- Flask
- SQLAlchemy

## Instalação

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   
   Instale as dependências usando o pip:
   
   pip install -r requirements.txt
   
   Execute o aplicativo:
   
   python app.py
