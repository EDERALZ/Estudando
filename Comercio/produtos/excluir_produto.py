import json
produtos:list = json.load(open("produto.json"))
#fazer as informações de clientes serem excluidas
ex_produto = input("Informe o nome do produto a ser excluido")
#coletar informações e excluir no json
encontrado = (None)
for produtos_e in produtos:
    if ex_produto == produtos_e['Nome']:
        encontrado = produtos_e

if encontrado is None:
    print("Venda não encontrada")
else:
    produtos.remove(encontrado)
    print(encontrado['Nome'], "Excluido com sucesso")
#escrever informações dentro do json
json.dump(produtos, open("produto.json", "w"), indent=2)