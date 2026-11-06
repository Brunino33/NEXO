from database import conexao
from produtos import (
    cadastrar_produto,
    listar_produtos,
    consultar_estoque,
    atualizar_produto,
    deletar_produto
)
from fornecedores import (
    cadastrar_fornecedor,
    listar_fornecedores,
    consultar_fornecedor,
    atualizar_fornecedor,
    deletar_fornecedor
) 


while True:
    print("\n===============================")
    print("             NEXO")
    print("   Sistema de Gestão Comercial")
    print("===============================")
    print("[1] Cadastrar Produto")
    print("[2] Listar Produtos")
    print("[3] Consultar Estoque")
    print("[4] Atualizar Produto")
    print("[5] Deletar Produto")

    print("\n========== FORNECEDORES ==========")

    print("[6] Cadastrar Fornecedor")
    print("[7] Listar Fornecedores")
    print("[8] Consultar Fornecedor")
    print("[9] Atualizar Fornecedor")
    print("[10] Deletar Fornecedor")
    print("\n[11] Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        consultar_estoque()

    elif opcao == "4":
        atualizar_produto()

    elif opcao == "5":
        deletar_produto()

    elif opcao == "6":
        cadastrar_fornecedor()

    elif opcao == "7":
        listar_fornecedores()

    elif opcao == "8":
        consultar_fornecedor()

    elif opcao == "9":
        atualizar_fornecedor()

    elif opcao == "10":
        deletar_fornecedor()

    elif opcao == "11":
        print("Encerrando o Nexo. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

conexao.close()




                  

                                         