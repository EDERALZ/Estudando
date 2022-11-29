import json
produtos:list = json.load(open("produto.json"))

print("id    Nome    Valor")
for item_compra in produtos:
    print("", item_compra['id'].ljust(5), "",item_compra['Nome'].ljust(15), "", str("%.2f"%item_compra['Valor']).rjust(5))