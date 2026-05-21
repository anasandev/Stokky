from conexao import cursor

usuario = input("Usuário: ")
senha = input("Senha: ")

sql = "SELECT * FROM tb_usuario WHERE usu_email = %s AND usu_senha = %s"


valores = (usuario, senha)

cursor.execute(sql, valores)

resultado = cursor.fetchone()

if resultado:
    print("Login realizado!")
else:
    print("Usuário ou senha incorretos!")