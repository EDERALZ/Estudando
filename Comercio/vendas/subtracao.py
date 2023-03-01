import json

estoque: list = json.load(open("../estoque/estoque.json", "r"))

produto_desejado = input("Digite o id do produto que deseja comprar: ")
quantidade_desejada = int(input("Digite a quantidade que deseja comprar: "))
cadastro = None
for item in estoque:
    if item['ID produto'] == produto_desejado:
        cadastro = item
        break

if cadastro is None:
    print("Desculpe, o produto não foi encontrado.")
else:
    quantidade_em_estoque = cadastro['Quantidade']
    if quantidade_desejada > quantidade_em_estoque:
        print("Desculpe, não há estoque suficiente.")
    else:
        nova_quantidade = quantidade_em_estoque - quantidade_desejada
        cadastro['Quantidade'] = nova_quantidade
        print("Compra realizada com sucesso. Quantidade do produto em estoque:", nova_quantidade)

        #json.dump(estoque, open('../estoque/estoque.json', 'w'), indent=2)