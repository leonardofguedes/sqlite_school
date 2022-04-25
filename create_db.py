import sqlite3

Escola = sqlite3.connect('Dados_Escola.db') #variavel criadora do banco de dados
Cursor = Escola.cursor()
"""
Cursor.execute(
   'CREATE TABLE Alunos ( Nome text, Id int, CPF int, Turma int)'
)
"""