import json
def leitura_json():
    return json.load(open("cliente.json"))
clientes: list = leitura_json()

cliente_encontrar = input("Insira o nome do cliente: ")
buscar = (None)
for cliente_b in clientes:
    if cliente_encontrar == cliente_b['Nome']:
        buscar = cliente_b

if buscar is None:
    print("Cliente não encontrado")
else:
    print("Cliente encontrado:", "Seu id é:", cliente_b['id'])

json.dump(clientes, open("cliente.json", "w"), indent=2)
