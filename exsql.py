import sqlite3

conexao = sqlite3.connect("escola.db")

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER, nome TEXT, nota REAL)")

cursor.execute("INSERT INTO alunos VALUES (1, 'João', 8.5)")
cursor.execute("INSERT INTO alunos VALUES (2, 'Maria', 9.0)")
cursor.execute("INSERT INTO alunos VALUES (3, 'Pedro', 7.3)")

conexao.commit()
conexao.close()

print("Banco de dados criado e alunos inseridos com sucesso!")