import json
#le arquivo json com as informações que está dentro
def ler_arquivo_json():
    return json.load(open("venda.json"))
vendas:list = ler_arquivo_json()

def digitar_id():
    vendas_e =  input("Insira o id da venda: ")
    return vendas_e
vendas_encontrar = digitar_id()
#fazer com que coloque o produto e o sistema puxe todas informações dele
def vendas_produto():
    buscar = (None)
    for vendas_p in vendas:
        if vendas_encontrar == vendas_p['id produto']:
            buscar = vendas_p
    return buscar
buscar = vendas_produto()
#será feito a verificação do produto
def id_encontrar():
    id_venda = None
    if buscar is None:
        id_venda = ("ID da venda nao encontrado")
    else:
        id_venda = (buscar['id produto'] + " " + "Produto encontrado")
    return id_venda
id_venda = id_encontrar()
print(id_venda)
#escreve nos arquivos
def escreve_arquivo():
    json.dump(vendas, open("venda.json", "w"), indent=2)
escreve_arquivo()