from database import conexao, cursor

def cadastrar_fornecedor():
    nome = input("Digite o nome do fornecedor: ").strip()
    cnpj = input("Digite o CNPJ do fornecedor: ").strip()
    telefone = input("Digite o telefone do fornecedor: ").strip()
    email = input("Digite o email do fornecedor: ").strip()
    endereco = input("Digite o endereço do fornecedor: ").strip()

    cursor.execute("""
        INSERT INTO fornecedores (nome, cnpj, telefone, email, endereco)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, cnpj, telefone, email, endereco))

    conexao.commit()

    print(f"Fornecedor {nome} cadastrado com sucesso!")

def listar_fornecedores():
    cursor.execute("SELECT * FROM fornecedores")
    fornecedores = cursor.fetchall()

    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return

    print("\n========== LISTA DE FORNECEDORES ==========")

    for fornecedor in fornecedores:
        print(f"ID: {fornecedor[0]}")
        print(f"Nome: {fornecedor[1]}")
        print(f"CNPJ: {fornecedor[2]}") 
        print(f"Telefone: {fornecedor[3]}")
        print(f"Email: {fornecedor[4]}")
        print(f"Endereço: {fornecedor[5]}")
        print("--------------------------------")

def consultar_fornecedor():
    cnpj = input("Digite o CNPJ do fornecedor que deseja consultar: ").strip()

    cursor.execute("SELECT * FROM fornecedores WHERE cnpj = ?", (cnpj,))
    fornecedor = cursor.fetchone()

    if fornecedor:
        print("\n========== DADOS DO FORNECEDOR ==========")
        print(f"ID: {fornecedor[0]}")
        print(f"Nome: {fornecedor[1]}")
        print(f"CNPJ: {fornecedor[2]}")
        print(f"Telefone: {fornecedor[3]}")
        print(f"Email: {fornecedor[4]}")
        print(f"Endereço: {fornecedor[5]}")
    else:
        print("Fornecedor não encontrado.")

def atualizar_fornecedor():
    cnpj = input("Digite o CNPJ do fornecedor que deseja atualizar: ").strip()
    cursor.execute(
        "SELECT * FROM fornecedores WHERE cnpj = ?", 
        (cnpj,)
    )

    fornecedor = cursor.fetchone()

    if fornecedor:
        print(f"Fornecedor encontrado: {fornecedor[1]}")

    novo_nome = input("Novo nome (pressione Enter para manter o atual): ").strip()
    if novo_nome == "":
        novo_nome = fornecedor[1]

    novo_telefone = input("Novo telefone (pressione Enter para manter o atual): ").strip()
    if novo_telefone == "":
        novo_telefone = fornecedor[3]

    novo_email = input("Novo email (pressione Enter para manter o atual): ").strip()
    if novo_email == "":
        novo_email = fornecedor[4]

    novo_endereco = input("Novo endereço (pressione Enter para manter o atual): ").strip()
    if novo_endereco == "":
        novo_endereco = fornecedor[5]

        cursor.execute("""
        UPDATE fornecedores
        SET nome = ?, telefone = ?, email = ?, endereco = ?
        WHERE cnpj = ?
        """, (novo_nome, novo_telefone, novo_email, novo_endereco, cnpj))

        conexao.commit()

        print("Fornecedor atualizado com sucesso!")
    
    else:
        print("Fornecedor não encontrado.")

def deletar_fornecedor():
    cnpj = input("Digite o CNPJ do fornecedor que deseja deletar: ").strip()

    cursor.execute(
        "SELECT * FROM fornecedores WHERE cnpj = ?", 
        (cnpj,)
    )

    fornecedor = cursor.fetchone()

    if fornecedor:
        print(f"Fornecedor encontrado: {fornecedor[1]}")
        confirmacao = input("Tem certeza que deseja deletar este fornecedor? (s/n): ").strip().lower()
        if confirmacao == "s":
            cursor.execute(
                "DELETE FROM fornecedores WHERE cnpj = ?",
            (cnpj,)
        )

            conexao.commit()
            print("Fornecedor deletado com sucesso!")
        else:
            print("Fornecedor não encontrado.")
    else:
        print("Fornecedor não encontrado.")


