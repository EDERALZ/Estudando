import json
#le arquivo json com as informações que está dentro
def ler_arquivo_json():
    return json.load(open("estoque.json"))
estoque:list = ler_arquivo_json()

def digitar_estoque():
    estoque_e =  input("Insira o id do produto a ser encontrado: ")
    return estoque_e
produto_encontrar = digitar_estoque()
#fazer com que coloque o produto e o sistema puxe todas informações dele
def buscar_produto():
    buscar = (None)
    for estoque_p in estoque:
        if produto_encontrar == estoque_p['ID produto']:
            buscar = estoque_p
    return buscar
buscar = buscar_produto()
#será feito a verificação do produto
def id_encontrar():
    id_produto = None
    if buscar is None:
        id_produto = ("ID do produto não encontrado")
    else:
        id_produto = (buscar['ID produto'] + " " + "Produto encontrado")
    return id_produto
id_produto = id_encontrar()
print(id_produto)
#escreve nos arquivos
def escreve_arquivo():
    json.dump(estoque, open("estoque.json", "w"), indent=2)
escreve_arquivo()