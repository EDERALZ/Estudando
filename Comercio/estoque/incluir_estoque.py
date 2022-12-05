import json
estoques:list = json.load(open("estoque.json"))

print("Programa de incluir no estoque ")
id_produto = input("Informe o id do produto")
quantidade_produto = input("Quantidade do produto em estoque: ")
validade_produto = input("Informe a validade do produto: ")
centro_distribuicao = input("Digite o código cdd: ")

produto_id = str(id_produto)
produto_quantidade = str(quantidade_produto)
validade = str(validade_produto)
centro = str(centro_distribuicao)

estoques.append({"ID produto":produto_id,"Quantidade":produto_quantidade, "Validade":validade, "Centro de distribuicao": centro})

json.dump(estoques, open("estoque.json", "w" ), indent=2)
print("Estoque incluido com sucesso ")