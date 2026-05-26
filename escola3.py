import sqlite3

conexao = sqlite3.connect("escola.db")

cursor = conexao.cursor()

cursor.execute("SELECT AVG(nota) FROM alunos")

media = cursor.fetchone()[0]

conexao.close()

print("Media das notas:", round(media, 2))