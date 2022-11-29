import json
vendas:list = json.load(open("venda.json"))
#cliente irá digitar o nome do produto e será puxado o valor e o id do produto
print(vendas)
procurar_vendas = input("Insira o id da venda: ")
#fazer com que coloque o produto e o sistema puxe todas informações dele
buscar = (None)
#print(produtos)
for vendas_b in vendas:
    if procurar_vendas == vendas_b['id produto']:
        buscar = vendas_b

if buscar is None:
    print("Venda não encontrada")
else:
    print(buscar['id produto'], "venda encontrada")

json.dump(vendas, open("venda.json", "w"), indent=2)