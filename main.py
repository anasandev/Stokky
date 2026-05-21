from crud import *
import login

if login.fazer_login():

    while True:

        print("\n===== SISTEMA =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            atualizar_produto()

        elif opcao == "4":
            deletar_produto()

        elif opcao == "5":
            break