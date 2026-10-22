# Sistema de Biblioteca

## Descrição

Sistema de gerenciamento de biblioteca desenvolvido em Python com Django.

O projeto permite cadastrar e administrar autores, livros e membros, além de controlar empréstimos e devoluções.

## Funcionalidades

* Cadastro e gerenciamento de autores, livros e membros pelo painel administrativo.
* Consulta e pesquisa de livros.
* Controle de empréstimos e devoluções.
* Controle de cópias disponíveis.
* Consulta dos empréstimos de cada membro.
* Identificação de empréstimos atrasados.
* Relatório de livros mais emprestados.

## Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML
* CSS

## Como executar o projeto

1. Instale o Python.

2. Crie e ative um ambiente virtual.

3. Instale as dependências:

   
   python -m pip install -r requirements.txt
   

4. Execute as migrações:

   
   python manage.py migrate
  

5. Inicie o servidor:

  
   python manage.py runserver
  

6. Acesse o sistema em `http://127.0.0.1:8000/`.

## Testes

Para executar os testes automatizados:


python manage.py test


## Autora

Projeto acadêmico desenvolvido como atividade prática de Django.
