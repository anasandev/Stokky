# references https://www.youtube.com/watch?v=_q3j25ACmQ4

import mysql.connector

# conexão com banco
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="db_9dedos"
)

cursor = conexao.cursor()
print("Conectado com sucesso!")

cursor.execute("SHOW TABLES")

for tabela in cursor:
    print(tabela)