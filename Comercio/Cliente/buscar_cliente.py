import json
clientes:list = json.load(open("cliente.json"))
#cliente irá digitar o nome do produto e será puxado o valor e o id do produto
print(clientes)
cliente_encontrar = input("Insira o nome do cliente: ")
#fazer com que coloque o produto e o sistema puxe todas informações dele
buscar = (None)
#print(produtos)
for cliente_b in clientes:
    if cliente_encontrar == cliente_b['Nome']:
        buscar = cliente_b

if buscar is None:
    print("Cliente não encontrado")
else:
    print(buscar['Nome'], "Cliente encontrado")

json.dump(clientes, open("cliente.json", "w"), indent=2)



#criar um laco para dizer se tem ou não o produto