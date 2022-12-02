import json
estoques:list = json.load(open("estoque.json"))
#cliente irá digitar o nome do produto e será puxado o valor e o id do produto
print(estoques)
estoque_encontrar = input("Insira o ID do produto ser encontrado: ")
#fazer com que coloque o produto e o sistema puxe todas informações dele
buscar = (None)
for estoque_b in estoques:
    if estoque_encontrar == estoque_b['id']:
        buscar = estoque_b

if buscar is None:
    print("Não está em estoque")
else:
    print(buscar['id'], "Produto encontrado")

json.dump(estoques, open("estoque.json", "w"), indent=2)