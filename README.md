
# Descrição

Cadastro de Pessoas com Interface Gráfica em Tkinter

Este projeto consiste em uma aplicação simples para cadastrar e gerenciar informações de pessoas, utilizando uma interface gráfica desenvolvida em Tkinter. A aplicação permite adicionar novos registros, remover entradas selecionadas e visualizar os dados em uma tabela.


## Bibliotecas Utilizadas

O projeto faz uso das seguintes bibliotecas:

tkinter: Fornece os elementos necessários para a criação da interface gráfica.

ttk (themedtk): Oferece widgets temáticos para melhorar o visual da interface.

pandas: Utilizada para manipulação e armazenamento dos dados em formato de tabela.

os: Usada para verificar a existência de arquivos, configurar o ícone da aplicação e manipular caminhos de arquivos.


## Preview

![App Screenshot](https://i.postimg.cc/FKRtYZzc/demo.png)


## Funcionamento do Código

#### Cadastro de Pessoas:

A função cadastrar é responsável por coletar os dados (nome, CPF, telefone) inseridos na interface.
Verifica se o arquivo 'cadastros.csv' existe. Se não existir, cria um novo.
Adiciona os dados à planilha CSV usando a biblioteca Pandas.
Limpa os campos de entrada após o cadastro.
Atualiza a tabela de cadastros.

#### Remoção de Entradas Selecionadas:

A função apagar_selecionado obtém os itens selecionados na tabela.
Lê o arquivo CSV existente com o Pandas.
Remove as entradas correspondentes aos itens selecionados.
Salva o DataFrame atualizado no arquivo CSV.
Atualiza a tabela após a remoção.

#### Atualização da Tabela:

A função atualizar_tabela verifica se o arquivo 'cadastros.csv' existe.
Limpa a tabela na interface.
Lê os dados do arquivo CSV e adiciona à tabela.

#### Interface Gráfica:

Configuração da janela principal com título, ícone, tamanho e tema.
Widgets incluem rótulos, campos de entrada, botões e uma tabela (TreeView) para exibir os dados.
A interface é visualmente aprimorada com o uso do ThemedStyle.

#### Loop Principal:

O código finaliza com o loop principal (root.mainloop()), que mantém a aplicação em execução.

Esse projeto é útil para criar e gerenciar um banco de dados simples de cadastros de pessoas com uma interface amigável.



## Autores

- [@rafadig](https://www.github.com/rafadig)

