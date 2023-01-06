import json
estoques:list = json.load(open("estoque.json"))
produtos:list = json.load(open("../produtos/produto.json"))
print("Programa de incluir produto no estoque ")
procurar_informacao =  input("Informe o produto a ser encontrado: ")
print(procurar_informacao)
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
    #gravar as informações dentro de variaveis
    quantidade_produto = input("Informe a quantidade do produto a ser incluido: ")
    val_produto = input("Informe a validade do produto incluido: ")
    data_dia = int(val_produto[0] + (val_produto[1]))
    if data_dia >= 1 and data_dia <= 31:
        print("Está correto")
        data_mes = int(val_produto[3] + (val_produto[4]))
        if data_mes >= 1 and data_mes <= 12:
            print("Está correto o mes")
            data_ano = int(val_produto[6] + (val_produto[7] + (val_produto[8] + (val_produto[9]))))
            if data_ano >= 1 and data_ano <= 9999:
                print("Está correto")
            else:
                print("O ano está incorreto")
        else:
            print("Está incorreto o mes")
    else:
        print("Está incorreto")
        centro_de_distribuicao = input("Informe o CDD do produto: ")
        quant_produto = str(quantidade_produto)
        validade_produto = str(val_produto)
        cdd = str(centro_de_distribuicao)
        buscar = (None)
        produtos.append({"Quantidade": quantidade_produto, "Validade do produto": val_produto,
                         "Centro de distribuicao": centro_de_distribuicao})
        estoques.append({"Quantidade": quantidade_produto, "Validade do produto": val_produto,
                         "Centro de distribuicao": centro_de_distribuicao})
        json.dump(estoques, open("estoque.json", "w"), indent=2)
        print("Produto incluido com sucesso")
