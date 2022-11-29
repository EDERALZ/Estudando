import json
produtos:list = json.load(open("produto.json"))
#cliente irá digitar o nome do produto e será puxado o valor e o id do produto
print(produtos)
produto_encontrar = input("Insira o produto a ser encontrado: ")
#fazer com que coloque o produto e o sistema puxe todas informações dele
buscar = (None)
#print(produtos)
for produto_b in produtos:
    if produto_encontrar == produto_b['Nome']:
        buscar = produto_b

if buscar is None:
    print("Produto não encontrado")
else:
    print(buscar['Nome'], "Produto encontrado")

json.dump(produtos, open("produto.json", "w"), indent=2)