from database import conexao, cursor

def cadastrar_produto():
    nome = input("Digite o nome do produto: ").strip()

    if nome == "":
        print("Erro: O nome do produto não pode ficar vazio.")
        return

    try:
        preco = float(input("Digite o preço do produto: ").replace(",", "."))

        if preco <= 0:
            print("Erro: O preço do produto deve ser maior que zero!")
            return
    except ValueError:
        print("Erro: O preço do produto deve ser um número válido.")
        return

    try:
        quantidade = int(input("Digite a quantidade do produto: "))

        if quantidade < 0:
            print("Erro: A quantidade do produto não pode ser negativa!")
            return
    except ValueError:
        print("Erro: A quantidade deve ser um número inteiro válido.")
        return

    cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (?, ?, ?)
        """, (nome, preco, quantidade))

    conexao.commit()
    print(f"Produto {nome} cadastrado com sucesso!")

def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n========== LISTA DE PRODUTOS ==========")

    for produto in produtos:
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Preço: R$ {produto[2]:.2f}".replace(".", ","))
        print(f"Quantidade: {produto[3]}")
        print("--------------------------------")

def consultar_estoque():
    cursor.execute("SELECT nome, quantidade FROM produtos")
    produtos = cursor.fetchall()

    print("\n========== ESTOQUE ==========")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        nome = produto[0]
        quantidade = produto[1]
    

        if quantidade < 5:
            print(f"ALERTA: Estoque baixo para {nome}!")
        elif quantidade <= 15:
            print(f"AVISO: Estoque moderado para {nome}.")
        elif quantidade < 30:
            print(f"Estoque quase acabando para {nome}.")
        else:
            print(f"Estoque suficiente para {nome}.")
    

def atualizar_produto():
    try:
        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
    except ValueError:
        print("Erro: Digite um ID válido.")
        return

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()

    if produto:
        print(f"Produto encontrado: {produto[1]}")
        novo_nome = input(
            "Digite o novo nome do produto (ou pressione Enter para manter o atual): "
        ).strip()

        if novo_nome == "":
            novo_nome = produto[1]
        
        novo_preco = input(
            "Digite o novo preço do produto (ou pressione Enter para manter o atual): "
        ).strip()
        
        if novo_preco == "":
            novo_preco = produto[2]
        else:
            try:
                novo_preco = float(novo_preco.replace(",", "."))

                if novo_preco <= 0:
                    print("Erro: O preço do produto deve ser maior que zero!")
                    return
            except ValueError:
                print("Erro: O preço do produto deve ser um número válido.")
                return
        
        nova_quantidade = input(
            "Digite a nova quantidade do produto (ou pressione Enter para manter o atual): "
        ).strip()

        if nova_quantidade == "":
            nova_quantidade = produto[3]
        else:
            try:
                nova_quantidade = int(nova_quantidade)
                
                if nova_quantidade < 0:
                    print("Erro: A quantidade do produto não pode ser negativa!")
                    return
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro válido.")
                return

        cursor.execute("""
            UPDATE produtos
            SET nome = ?, preco = ?, quantidade = ?
            WHERE id = ?
        """, (novo_nome, novo_preco, nova_quantidade, id_produto))   
        
        conexao.commit()
        
        print(f"Produto {novo_nome} atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def deletar_produto():
    try:
        id_produto = int(input("Digite o ID do produto que deseja deletar: "))
    except ValueError:
        print("Erro: Digite um ID válido.")
        return

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()

    if produto:
        confirmacao = input(
            f"Tem certeza que deseja deletar o produto {produto[1]}? (s/n): "
        ).strip().lower()

        if confirmacao == "s":
            cursor.execute(
                "DELETE FROM produtos WHERE id = ?", (id_produto,)
            )
            conexao.commit()
            print(f"Produto {produto[1]} deletado com sucesso!")
        else:
            print("Exclusão cancelada.")
    else:
        print("Produto não encontrado.")
