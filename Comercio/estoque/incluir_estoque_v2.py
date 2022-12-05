import json
#leitura do arquivo json de estoque
estoques:list = json.load(open("estoque.json"))
#leitura do arquivo json de produto
produtos:list = json.load(open("../produtos/produto.json"))

#mostrar na tela que está incluindo no estoque
print("Programa de incluir produto no estoque ")
#solicitar informação para usuario
procurar_informacao =  input("Informe o produto a ser encontrado: ")
print(procurar_informacao)

#novo: Verificar informação dentro do arquivo produto.json (id produto)
buscar = (None)
for produto_info in produtos:
    if procurar_informacao == produto_info['id']:
        buscar = produto_info
if buscar is None:
    print("Produto não encontrado")
else:
    print("Produto encontrado com sucesso: ")
    print("ID","    ", "Nome",   "  ", "quantidade")
    print(produto_info['id'],produto_info['Nome'].rjust(10), str(produto_info['Valor']).rjust(10))
#   poderá ter dois resultados; 1) produto existe e o programa funciona normal
#   2; caso não exista o programa irá mostrar uma mensagem "Produto não encontrado", sistema irá parar.
#gravar as informações dentro de variaveis
    #produto_id = input("Digite ID do produto que deseja incluir: ")
    quantidade_produto = input("Informe a quantidade do produto a ser incluido: ")
    val_produto = input("Informe a validade do produto incluido: ")
    centro_de_distribuicao = input("Informe o CDD do produto: ")
    #id_produto = str(produto_id)
    quant_produto = str(quantidade_produto)
    validade_produto = str(val_produto)
    cdd = str(centro_de_distribuicao)
    buscar = (None)
#adicionar informações no vetor
    produtos.append({"Quantidade": quantidade_produto, "Validade do produto": val_produto, "Centro de distribuicao":centro_de_distribuicao})
    estoques.append({"Quantidade": quantidade_produto, "Validade do produto": val_produto, "Centro de distribuicao":centro_de_distribuicao})
#escrever as informações dentro arquivo json
    json.dump(estoques, open("estoque.json", "w"), indent=2)
    json.dump(produtos, open("produto.json", "w"), indent=2)
#mostrar na tela que foi incluido no estoque
    print("Produto incluido com sucesso")