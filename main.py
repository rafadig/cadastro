import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import pandas as pd
import os

# Função para cadastrar uma nova pessoa
def cadastrar():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    telefone = telefone_entry.get()

    # Verificar se o arquivo já existe
    arquivo_existe = os.path.exists('cadastros.csv')

    # Adicionar os dados à planilha
    with open('cadastros.csv', mode='a', newline='') as arquivo:
        header = not arquivo_existe
        df = pd.DataFrame({'Nome': [nome], 'CPF': [cpf], 'Telefone': [telefone]})
        df.to_csv(arquivo, header=header, index=False)

    # Limpar os campos após o cadastro
    nome_entry.delete(0, 'end')
    cpf_entry.delete(0, 'end')
    telefone_entry.delete(0, 'end')

    # Atualizar a tabela de cadastros
    atualizar_tabela()

# Função para apagar a entrada selecionada na tabela
def apagar_selecionado():
    # Obter os itens selecionados na tabela
    selecionados = tabela.selection()
    
    if selecionados:
        # Atualizar o arquivo CSV removendo as entradas correspondentes
        df = pd.read_csv('cadastros.csv')

        # Converter os IDs de seleção para índices do DataFrame
        indices = [int(tabela.index(selecao)) for selecao in selecionados]
        
        # Filtrar os índices para garantir que estão presentes no DataFrame
        indices = [indice for indice in indices if indice in df.index]

        # Remover as entradas do DataFrame
        df = df.drop(indices)

        # Salvar o DataFrame atualizado no arquivo CSV
        df.to_csv('cadastros.csv', index=False)

        # Atualizar a tabela após a remoção
        atualizar_tabela()

# Função para atualizar a tabela de cadastros
def atualizar_tabela():
    # Verificar se o arquivo já existe
    if os.path.exists('cadastros.csv'):
        # Limpar a tabela
        for row in tabela.get_children():
            tabela.delete(row)

        # Ler a planilha
        df = pd.read_csv('cadastros.csv')

        # Adicionar os dados à tabela
        for index, row in df.iterrows():
            tabela.insert('', 'end', values=(row['Nome'], row['CPF'], row['Telefone']))

# Configuração da interface gráfica
root = tk.Tk()
root.title('Cadastro de Pessoas')

# Defina o caminho para o seu próprio ícone (substitua 'seu_icone.ico' pelo caminho do seu ícone)
icone_path = 'C:\\Users\\Rafael\\Desktop\\Cadastros Gabinete do Cidadão\\logo.ico'

# Verifique se o arquivo do ícone existe antes de tentar configurá-lo
if os.path.exists(icone_path):
    root.iconbitmap(icone_path)

# Obter as dimensões da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Calcular as coordenadas para centralizar a janela
x = (largura_tela - 800) // 2
y = (altura_tela - 400) // 2  # Altura da janela reduzida

# Definir a geometria da janela
root.geometry(f'800x400+{x}+{y}')

# Tema para melhorar o visual
style = ThemedStyle(root)
style.set_theme('arc')  # Escolha o tema desejado

# Widgets
nome_label = ttk.Label(root, text='Nome:')
nome_entry = ttk.Entry(root)

cpf_label = ttk.Label(root, text='CPF:')
cpf_entry = ttk.Entry(root)

telefone_label = ttk.Label(root, text='Telefone:')
telefone_entry = ttk.Entry(root)

cadastrar_button = ttk.Button(root, text='Cadastrar', command=cadastrar)
apagar_button = ttk.Button(root, text='Apagar Selecionado', command=apagar_selecionado)

# Tabela de cadastros
tabela = ttk.Treeview(root, columns=('Nome', 'CPF', 'Telefone'), show='headings', height=10)
tabela.column('Nome', width=200, anchor='center')
tabela.heading('Nome', text='Nome')
tabela.column('CPF', width=150, anchor='center')
tabela.heading('CPF', text='CPF')
tabela.column('Telefone', width=150, anchor='center')
tabela.heading('Telefone', text='Telefone')

# Layout
nome_label.grid(row=0, column=0, pady=10, padx=10, sticky='e')
nome_entry.grid(row=0, column=1, pady=10, padx=10, sticky='w')

cpf_label.grid(row=1, column=0, pady=10, padx=10, sticky='e')
cpf_entry.grid(row=1, column=1, pady=10, padx=10, sticky='w')

telefone_label.grid(row=2, column=0, pady=10, padx=10, sticky='e')
telefone_entry.grid(row=2, column=1, pady=10, padx=10, sticky='w')

cadastrar_button.grid(row=3, column=0, pady=10, padx=10)
apagar_button.grid(row=3, column=1, pady=10, padx=10)

tabela.grid(row=0, column=2, rowspan=4, pady=10, padx=10, sticky='nsew')  # Movida para a coluna 2

# Atualizar a tabela ao iniciar
atualizar_tabela()

# Configurar pesos na grade para tornar a tabela redimensionável
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(4, weight=1)

# Iniciar o loop principal
root.mainloop()
