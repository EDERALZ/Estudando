import json
#leitura dos arquvios json
estoques:list = json.load(open("estoque.json"))
ed_estoque_id = input("Informe o id do produto que deseja alterar: ")
encontrado = (None)
for estoque_alterar in estoques:
    if ed_estoque_id == estoque_alterar['ID produto']:
        encontrado = estoque_alterar
if encontrado is None:
    print("Produto não encontrado ou informação errada")
else:
    #coleta os dados cadastrais
    id_produto = input("Informe o id do produto: ")
    quantidade_produto = input("Informe a quantidade do produto: ")
    val_produto = input("Validade do produto: ")
    cdd_produto = input("Centro de distribuicao: ")
    produto_id = (id_produto)
    produto_quantidade = (quantidade_produto)
    validade_p = str(val_produto)
    cdd_p = str(cdd_produto)
    estoques.remove(encontrado)
    estoques.append({'id: ':id_produto,"Quantidade: ":quantidade_produto,"Validade do produto: ":val_produto,"Centro de distribuicao: ":cdd_produto})

    #escrever informações dentro do json
    json.dump(estoques, open("estoque.json", "w"), indent=2)
    print("Informacoes alteradas com sucesso! ")