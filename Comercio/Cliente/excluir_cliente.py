import json
clientes:list = json.load(open("cliente.json"))
#fazer as informações de clientes serem excluidas
excliente_id = input("Informe o ID à ser excluído: ")
#coletar informações e excluir no json
encontrado = (None)
for cliente_e in clientes:
    if excliente_id == cliente_e['id']:
        encontrado = cliente_e

if encontrado is None:
    print("Não encontrado")
else:
    clientes.remove(encontrado)
    print(encontrado['Nome'], "Excluido com sucesso")
#escrever informações dentro do json
json.dump(clientes, open("cliente.json", "w"), indent=2)