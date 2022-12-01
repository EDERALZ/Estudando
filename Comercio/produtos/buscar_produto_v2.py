import json
#leitura do arquivo json
def ler_arquivo_json():
    return json.load(open("produto.json"))
produtos:list = ler_arquivo_json()

#cliente irá digitar o nome do produto e será puxado o valor e o id do produto
def digitar_nome():
    produto_e =  input("Insira o produto a ser encontrado: ")
    return produto_e
produto_encontrar = digitar_nome()
#fazer com que coloque o produto e o sistema puxe todas informações dele
def buscar_produto():
    buscar = (None)
    for produto_b in produtos:
        if produto_encontrar == produto_b['Nome']:
            buscar = produto_b
    return buscar
buscar = buscar_produto()
#será feito a verificação do produto
def produto_encontrar():
    mostrar_produto = None
    if buscar is None:
        mostrar_produto = ("Produto não encontrado")
    else:
        mostrar_produto = (buscar['Nome'] + " " + "Produto encontrado")
    return mostrar_produto
mostrar_produto = produto_encontrar()
print(mostrar_produto)
#escreve nos arquivos
def escreve_arquivo():
    json.dump(produtos, open("produto.json", "w"), indent=2)
escreve_arquivo()