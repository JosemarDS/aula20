import sqlite3 
import tkinter as tk


conexao = sqlite3.connect('meu_banco_de_dados.db')

cursor = conexao.cursor()
# Criar uma Tabela
cursor.execute('''
         CREATE TABLE IF NOT EXISTS pessoas (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nome TEXT NOT NULL,
         idade INTERGER NOT NULL,
         cidade TEXT NOT NULLpip )           
''')

# INSERIR DADOS NA TABELA
nome = 'Paula'
idade = 30
cidade = 'São Paulo'
cursor.execute('''
    INSERT INTO pessoas (nome, idade, cidade)
    VALUES (?, ?, ?)
''', (nome, idade, cidade) 
    )
# Confirmar a Transação
conexao.commit()

#Consultar dados da Tabela
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

# Mostar dados consultados
for pessoa in pessoas:
    print(f'''ID: {pessoa[0]}, Nome: {pessoa[1]}, idade: {pessoa[2]}, Cidade: {pessoa[3]}''')

# Fechar Conexão
conexao.close()
   