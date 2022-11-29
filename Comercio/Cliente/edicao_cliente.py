import json
clientes:list = json.load(open("cliente.json"))
#fazer as informações de clientes serem excluidas
excliente_id = input("Informe o nome a ser alterado")
#coletar informações e excluir no json
encontrado = (None)
for cliente_e in clientes:
    if excliente_id == cliente_e['Nome']:
        encontrado = cliente_e

if encontrado is None:
    print("Cliente não encontrado ou informação errada")
else:
    clientes.remove(encontrado)
    print(encontrado['Nome'], "Excluido com sucesso")

cliente_id = input("Digite o id correto: ")
nome = input("Insira o nome correto do cliente: ")
senha = input("Informe a senha nova:")
e_mail = input("Digite seu e_mail: ")
endereco = input("Informe seu endereço: ")
id_cliente = str(cliente_id)
nome_cliente = str(nome)
senha_1 = str(senha)
e_mail_novo = str(e_mail)
endereco_novo = str(endereco)

clientes.append({"id":id_cliente,"Nome":nome_cliente, "Senha":senha_1, "E_mail":e_mail_novo, "Endereco":endereco_novo})

#escrever informações dentro do json
json.dump(clientes, open("cliente.json", "w"), indent=2)