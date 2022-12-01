import json
#leitura do arquivo
def leitura_cliente():
    return json.load(open("cliente.json"))
clientes: list = leitura_cliente()
#fazer as informações de clientes serem excluidas
def pedir_id():
    excliente_id = input("Informe o id que deseja alterar")
    return excliente_id
excliente_id = pedir_id()
#coletar informações e excluir no json
def excluir_id():
    encontrado = (None)
    for cliente_e in clientes:
        if excliente_id == cliente_e['id']:
            encontrado = cliente_e
    return cliente_e
encontrado = excluir_id()
#laço de repetição para remover
def remover_info():
    nome = input("Insira o nome correto do cliente: ")
    senha = input("Informe a senha nova:")
    e_mail = input("Digite seu e_mail: ")
    endereco = input("Informe seu endereço: ")
    cliente_id = (excliente_id)
    nome_cliente = str(nome)
    senha_1 = str(senha)
    e_mail_novo = str(e_mail)
    endereco_novo = str(endereco)
    clientes.remove(encontrado)
    clientes.append({
        "id": excliente_id, "Nome": nome_cliente,
        "Senha": senha_1, "E_mail": e_mail_novo, "Endereco": endereco_novo})
def escrever_json():
    json.dump(clientes, open("cliente.json", "w"), indent=2)
    print("Dados alterados com sucesso")

def cliente_informacao():
    if encontrado is None:
        print("Cliente não encontrado ou informação errada")
    else:
        #irá remover e adicionar
        remover_info()

        #escrever informações dentro do json
        escrever_json()