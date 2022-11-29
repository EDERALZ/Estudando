import datetime
import json
vendas:list = json.load(open("venda.json"))

produto_id = input("Informe o ID do produto: ")
cliente_id = input("Informe seu ID: ")
quantidade_produto = input("Digite a quantidade que deseja: ")
preco_produto = input("Digite o preço do produto: ")
data_hora = str(datetime.datetime.now())

id_produto = str(produto_id)
id_cliente = str(cliente_id)
quantidade = str(quantidade_produto)
preco = str(preco_produto)
hora_data = str(data_hora)

vendas.append({"id produto": produto_id, "id cliente": cliente_id, "Quantidade do produto":quantidade_produto,
               "Preco do produto": preco_produto, "Dia e hora da compra": hora_data})

json.dump(vendas, open("venda.json", "w" ),indent=2 )