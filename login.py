from conexao import get_connection
import pwinput


def fazer_login():
    usuario = input("Email: ")
    senha = pwinput.pwinput(prompt='Senha: ', mask='*') #pwipwi :3

    conexao = get_connection()
    cursor = conexao.cursor()

    sql = "SELECT usu_id, usu_nome FROM tb_usuario WHERE usu_email = %s AND usu_senha = %s"
    valores = (usuario, senha)

    cursor.execute(sql, valores)
    resultado = cursor.fetchone()

    cursor.close( )
    conexao.close()

    if resultado:
        usu_id = resultado[0]
        usu_nome = resultado[1]
        print(f"Login realizado! Bem-vindo, {usu_nome}!")
        return usu_id

    print("Usuário ou senha incorretos!")
    return None