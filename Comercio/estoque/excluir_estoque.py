import json
estoques:list = json.load(open("estoque.json"))
#fazer as informações de clientes serem excluidas
ex_estoque = input("Informe o id do produto a ser excluido")
#coletar informações e excluir no json
encontrado = (None)
for estoque_e in estoques:
    if ex_estoque == estoque_e['ID produto']:
        encontrado = estoque_e

if encontrado is None:
    print("Não achou no estoque")
else:
    estoques.remove(encontrado)
    print(encontrado['ID produto'], "Excluido com sucesso")
#escrever informações dentro do json
json.dump(estoques, open("estoque.json", "w"), indent=2)