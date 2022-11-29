import json
vendas:list = json.load(open("venda.json"))

print("id produto    id cliente   Quantidade do produto     preco do produto       dia e hora da compra")
for item_vendas in vendas:
    print("", str(item_vendas['id produto']).ljust(10), "",item_vendas['id cliente'].ljust(10), "", item_vendas['Quantidade do produto'].ljust(5), "", item_vendas['Preco do produto'].ljust(5), "", str(item_vendas['Dia e hora da compra'].rjust(5)))