import json

def ler_json():
    return json.load(open("produto.json"))
produtos:list = ler_json()
def receber_nome():
    pegar_nome = input("Informe o nome do produto a ser alterado: ")
    return pegar_nome
pegar_nome = receber_nome()

def encontrar_nome():
    encontrado = (None)
    for produto_nome in produtos:
        if receber_nome == produto_nome['Nome']:
            encontrado = produto_nome
            return produto_nome
encontrado = encontrar_nome()

def memorizar_info():
    id_produto = input("Insira o id do produto novo: ")
    produto = input("Nome novo produto: ")
    valor_produto = input("Valor do produto: ")
    imagem_produto = input("Insira a imagem em formato de url: ")
    produto_id = (id_produto)
    produto_adicionar = (produto)
    produto_valor = (valor_produto)
    img_produto = (imagem_produto)
    produtos.remove(encontrado)
    produtos.append({"id":id_produto,"Nome":produto,"Valor":valor_produto,"Imagem":imagem_produto})

def alterar_informacao():
    json.dump(produtos, open("produto.json", "w"), indent=2)
    print("Dados alterados com sucesso")

def laco_produto():
    if encontrado is None:
        print("Produto não encontrado ou informação errada")
    else:
        memorizar_info()
        alterar_informacao()
laco_produto()