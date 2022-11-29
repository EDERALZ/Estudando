import json
vendas:list = json.load(open("venda.json"))
#fazer as informações de clientes serem excluidas
ex_venda = input("Informe o ID da venda a ser excluído")
#coletar informações e excluir no json
encontrado = (None)
for vendas_e in vendas:
    if ex_venda == vendas_e['id produto']:
        encontrado = vendas_e

if encontrado is None:
    print("Venda não encontrada")
else:
    vendas.remove(encontrado)
    print(encontrado['id produto'], "Excluido com sucesso")
#escrever informações dentro do json
json.dump(vendas, open("venda.json", "w"), indent=2)