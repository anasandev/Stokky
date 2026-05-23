from crud import *
import login
import relatorio


def menu_empresa():
    """Menu para gestão de empresas."""
    while True:
        print("\n===== GESTÃO DE EMPRESA =====")
        print("1 - Cadastrar empresa")
        print("2 - Listar empresas")
        print("3 - Consultar empresa específica")
        print("4 - Atualizar empresa")
        print("5 - Deletar empresa")
        print("6 - Voltar ao menu principal")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\n--- CADASTRO DE EMPRESA ---")
            emp_nome = input("Nome da empresa: ")
            emp_cnpj = input("CNPJ: ")
            emp_email = input("Email: ")
            emp_tel = input("Telefone: ")
            emp_cep = input("CEP: ")
            emp_rua = input("Rua: ")
            emp_numero = input("Número: ")
            emp_complemento = input("Complemento (deixe em branco se não houver): ")
            emp_bairro = input("Bairro: ")
            emp_cidade = input("Cidade: ")
            emp_estado = input("Estado (UF): ")
            emp_pais = input("País: ")
            emp_data_criacao = input("Data de criação (YYYY-MM-DD): ")

            try:
                cadastrar_empresa(emp_nome, emp_cnpj, emp_email, emp_tel, emp_cep, emp_rua,
                                  emp_numero, emp_complemento, emp_bairro, emp_cidade, emp_estado, emp_pais, emp_data_criacao)
                print("✓ Empresa cadastrada com sucesso!")
            except Exception as e:
                print(f"✗ Erro ao cadastrar empresa: {e}")

        elif opcao == "2":
            print("\n--- LISTAGEM DE EMPRESAS ---")
            empresas = listar_empresas()
            if empresas:
                print(f"\n{'ID':<5} | {'Nome':<30} | {'CNPJ':<15} | {'Email':<30} | {'Cidade':<20}")
                print("-" * 105)
                for empresa in empresas:
                    print(f"{empresa[0]:<5} | {empresa[1]:<30} | {empresa[2]:<15} | {empresa[3]:<30} | {empresa[4]:<20}")
            else:
                print("Nenhuma empresa cadastrada.")

        elif opcao == "3":
            emp_id = input("\nDigite o ID da empresa: ")
            empresa = obter_empresa_por_id(emp_id)
            if empresa:
                print("\n--- DADOS DA EMPRESA ---")
                print(f"ID: {empresa[0]}")
                print(f"Nome: {empresa[1]}")
                print(f"CNPJ: {empresa[2]}")
                print(f"Email: {empresa[3]}")
                print(f"Telefone: {empresa[4]}")
                print(f"CEP: {empresa[5]}")
                print(f"Rua: {empresa[6]}")
                print(f"Número: {empresa[7]}")
                print(f"Complemento: {empresa[8] or 'N/A'}")
                print(f"Bairro: {empresa[9]}")
                print(f"Cidade: {empresa[10]}")
                print(f"Estado: {empresa[11]}")
                print(f"País: {empresa[12]}")
                print(f"Data de Criação: {empresa[13]}")
            else:
                print("✗ Empresa não encontrada.")

        elif opcao == "4":
            emp_id = input("\nDigite o ID da empresa a atualizar: ")
            empresa = obter_empresa_por_id(emp_id)
            if empresa:
                print("\n--- ATUALIZAÇÃO DE EMPRESA ---")
                emp_nome = input(f"Nome ({empresa[1]}): ") or empresa[1]
                emp_cnpj = input(f"CNPJ ({empresa[2]}): ") or empresa[2]
                emp_email = input(f"Email ({empresa[3]}): ") or empresa[3]
                emp_tel = input(f"Telefone ({empresa[4]}): ") or empresa[4]
                emp_cep = input(f"CEP ({empresa[5]}): ") or empresa[5]
                emp_rua = input(f"Rua ({empresa[6]}): ") or empresa[6]
                emp_numero = input(f"Número ({empresa[7]}): ") or empresa[7]
                emp_complemento = input(f"Complemento ({empresa[8] or 'N/A'}): ") or empresa[8]
                emp_bairro = input(f"Bairro ({empresa[9]}): ") or empresa[9]
                emp_cidade = input(f"Cidade ({empresa[10]}): ") or empresa[10]
                emp_estado = input(f"Estado ({empresa[11]}): ") or empresa[11]
                emp_pais = input(f"País ({empresa[12]}): ") or empresa[12]

                try:
                    atualizar_empresa(emp_id, emp_nome, emp_cnpj, emp_email, emp_tel, emp_cep,
                                      emp_rua, emp_numero, emp_complemento, emp_bairro, emp_cidade, emp_estado, emp_pais)
                    print("✓ Empresa atualizada com sucesso!")
                except Exception as e:
                    print(f"✗ Erro ao atualizar empresa: {e}")
            else:
                print("✗ Empresa não encontrada.")

        elif opcao == "5":
            emp_id = input("\nDigite o ID da empresa a deletar: ")
            try:
                sucesso, mensagem = deletar_empresa(emp_id)
                if sucesso:
                    print(f"✓ {mensagem}")
                else:
                    print(f"✗ {mensagem}")
            except Exception as e:
                print(f"✗ Erro ao deletar empresa: {e}")

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")


def menu_produto():
    """Menu para gestão de produtos vinculados a uma empresa."""
    print("\n--- SELEÇÃO DE EMPRESA ---")
    empresas = listar_empresas()
    if not empresas:
        print("✗ Nenhuma empresa cadastrada. Cadastre uma empresa primeiro!")
        return

    print(f"\n{'ID':<5} | {'Nome':<30} | {'Cidade':<20}")
    print("-" * 60)
    for empresa in empresas:
        print(f"{empresa[0]:<5} | {empresa[1]:<30} | {empresa[4]:<20}")

    try:
        emp_id = input("\nEscolha o ID da empresa: ")
        empresa = obter_empresa_por_id(emp_id)
        if not empresa:
            print("✗ Empresa não encontrada!")
            return
    except Exception as e:
        print(f"✗ Erro: {e}")
        return

    while True:
        print(f"\n===== GESTÃO DE PRODUTOS - {empresa[1]} =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos da empresa")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Voltar ao menu principal")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\n--- CADASTRO DE PRODUTO ---")
            pro_nome = input("Nome do produto: ")
            pro_descricao = input("Descrição do produto: ")
            pro_marca = input("Marca do produto: ")
            pro_preco = input("Preço do produto: ").replace(",", ".")
            pro_data_validade = input("Data de validade (YYYY-MM-DD): ")

            try:
                cadastrar_produto(pro_nome, pro_descricao, pro_marca, pro_preco, pro_data_validade, emp_id)
                print("✓ Produto cadastrado com sucesso!")
            except Exception as e:
                print(f"✗ Erro ao cadastrar produto: {e}")

        elif opcao == "2":
            print(f"\n--- PRODUTOS DA EMPRESA: {empresa[1]} ---")
            produtos = listar_produtos()
            produtos_empresa = [p for p in produtos if p[6] == int(emp_id)]

            if produtos_empresa:
                print(f"\n{'ID':<5} | {'Nome':<25} | {'Marca':<15} | {'Preço':<12} | {'Validade':<12}")
                print("-" * 75)
                for produto in produtos_empresa:
                    print(f"{produto[0]:<5} | {produto[1]:<25} | {produto[3]:<15} | R$ {produto[4]:<10.2f} | {produto[5]:<12}")
            else:
                print("Nenhum produto cadastrado para esta empresa.")

        elif opcao == "3":
            pro_id = input("\nDigite o ID do produto a atualizar: ")
            try:
                pro_nome = input("Novo nome: ")
                pro_descricao = input("Nova descrição: ")
                pro_marca = input("Nova marca: ")
                pro_preco = input("Novo preço: ").replace(",", ".")
                pro_data_validade = input("Nova data de validade (YYYY-MM-DD): ")
                atualizar_produto(pro_id, pro_nome, pro_descricao, pro_marca, pro_preco, pro_data_validade, emp_id)
                print("✓ Produto atualizado com sucesso!")
            except Exception as e:
                print(f"✗ Erro ao atualizar produto: {e}")

        elif opcao == "4":
            pro_id = input("\nDigite o ID do produto a deletar: ")
            try:
                deletar_produto(pro_id)
                print("✓ Produto deletado com sucesso!")
            except Exception as e:
                print(f"✗ Erro ao deletar produto: {e}")

        elif opcao == "5":
            break

        else:
            print("Opção inválida!")


def menu_relatorios():
    """Menu para geração de relatórios."""
    while True:
        print("\n===== RELATÓRIOS =====")
        print("1 - Relatório de todas as empresas")
        print("2 - Relatório de produtos por empresa")
        print("3 - Relatório de estoque geral")
        print("4 - Voltar ao menu principal")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            try:
                resultados = relatorio.relatorio_empresas()
                print("\n--- RELATÓRIO DE EMPRESAS ---")
                print(f"{'ID':<5} | {'Nome':<25} | {'CNPJ':<15} | {'Produtos':<10} | {'Qtd Estoque':<12} | {'Valor Estoque':<15}")
                print("-" * 90)
                for empresa in resultados:
                    print(f"{empresa[0]:<5} | {empresa[1]:<25} | {empresa[2]:<15} | {empresa[5]:<10} | {empresa[6] or 0:<12} | R$ {empresa[7]:<13.2f}")
                
                salvar = input("\nDeseja salvar o relatório em arquivo? (s/n): ")
                if salvar.lower() == 's':
                    arquivo = relatorio.gerar_relatorio_empresas_em_arquivo()
                    print(f"✓ Relatório salvo em: {arquivo}")
            except Exception as e:
                print(f"✗ Erro ao gerar relatório: {e}")

        elif opcao == "2":
            try:
                empresas = listar_empresas()
                if not empresas:
                    print("✗ Nenhuma empresa cadastrada!")
                    continue

                print("\n--- SELEÇÃO DE EMPRESA ---")
                for empresa in empresas:
                    print(f"ID: {empresa[0]} - {empresa[1]}")

                emp_id = input("\nDigite o ID da empresa: ")
                empresa_info, produtos = relatorio.relatorio_produtos_por_empresa(emp_id)

                if not empresa_info:
                    print("✗ Empresa não encontrada!")
                    continue

                print(f"\n--- RELATÓRIO DE PRODUTOS: {empresa_info[0]} ---")
                if produtos:
                    print(f"\n{'ID':<5} | {'Nome':<20} | {'Marca':<15} | {'Preço':<12} | {'Qtd':<8} | {'Valor Total':<15}")
                    print("-" * 85)
                    for produto in produtos:
                        print(f"{produto[0]:<5} | {produto[1]:<20} | {produto[2]:<15} | R$ {produto[4]:<10.2f} | {produto[6]:<8} | R$ {produto[7]:<13.2f}")
                else:
                    print("Nenhum produto cadastrado para esta empresa.")

                salvar = input("\nDeseja salvar o relatório em arquivo? (s/n): ")
                if salvar.lower() == 's':
                    arquivo = relatorio.gerar_relatorio_produtos_empresa_em_arquivo(emp_id, f'relatorio_produtos_emp_{emp_id}.txt')
                    sucesso, msg = arquivo if isinstance(arquivo, tuple) else (True, arquivo)
                    print(f"✓ Relatório salvo em: {msg}")
            except Exception as e:
                print(f"✗ Erro ao gerar relatório: {e}")

        elif opcao == "3":
            try:
                resultados = relatorio.relatorio_estoque_geral()
                print("\n--- RELATÓRIO DE ESTOQUE GERAL ---")
                print(f"\n{'Empresa':<25} | {'Produto':<20} | {'Marca':<15} | {'Qtd':<6} | {'Preço':<12} | {'Valor Total':<15}")
                print("-" * 100)
                
                valor_total = 0
                for linha in resultados:
                    valor_total += linha[5] or 0
                    print(f"{str(linha[0]):<25} | {str(linha[1]):<20} | {str(linha[2]):<15} | {linha[3] or 0:<6} | R$ {linha[4]:<10.2f} | R$ {linha[5] or 0:<13.2f}")
                
                print("-" * 100)
                print(f"VALOR TOTAL DO ESTOQUE: R$ {valor_total:.2f}")

                salvar = input("\nDeseja salvar o relatório em arquivo? (s/n): ")
                if salvar.lower() == 's':
                    arquivo = relatorio.gerar_relatorio_estoque_em_arquivo()
                    print(f"✓ Relatório salvo em: {arquivo}")
            except Exception as e:
                print(f"✗ Erro ao gerar relatório: {e}")

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")


if login.fazer_login():

    while True:
        print("\n" + "=" * 50)
        print("===== SISTEMA DE GESTÃO DE ESTOQUE =====")
        print("=" * 50)
        print("1 - Gestão de Empresa")
        print("2 - Gestão de Produtos")
        print("3 - Relatórios")
        print("4 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            menu_empresa()
        elif opcao == "2":
            menu_produto()
        elif opcao == "3":
            menu_relatorios()
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")