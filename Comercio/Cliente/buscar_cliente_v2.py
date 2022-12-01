import json
#ele le os arquivos do json
def buscar_clientes_json():
    return json.load(open("cliente.json"))
clientes:list = buscar_clientes_json()

#buscar informacao do cliente com o id
excliente_id = input("Informe o id que deseja alterar")
#coletar informações e excluir no json
encontrado = (None)
for cliente_e in clientes:
    if excliente_id == cliente_e['id']:
        encontrado = cliente_e
#laço de repetição para remover
if encontrado is None:
    print("Cliente não encontrado ou informação errada")
else:
    #coleta os dados cadastrais
    nome = input("Insira o nome correto do cliente: ")
    senha = input("Informe a senha nova:")
    e_mail = input("Digite seu e_mail: ")
    endereco = input("Informe seu endereço: ")
    cliente_id = (excliente_id)
    nome_cliente = str(nome)
    senha_1 = str(senha)
    e_mail_novo = str(e_mail)
    endereco_novo = str(endereco)
    #irá remover e adicionar
    clientes.remove(encontrado)
    clientes.append({"id":excliente_id,"Nome":nome_cliente, "Senha":senha_1, "E_mail":e_mail_novo, "Endereco":endereco_novo})

    #escrever informações dentro do json
    json.dump(clientes, open("cliente.json", "w"), indent=2)
    print("Dados alterados com sucesso")