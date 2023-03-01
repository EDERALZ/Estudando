import json

def informacoes_vendas():
    vendas:list = json.load(open("venda.json"))
    print(vendas)
    return vendas

def informacoes_produtos():
    produtos:list = json.load(open("../produtos/produto.json", "r"))
    print(produtos)
    return produtos

def informacoes_clientes():
    clientes: list = json.load(open("../Cliente/cliente.json", "r"))
    print(clientes)
    return clientes

def procurar_informacoes_produtos(produtos, cadastro):
    if cadastro['produto_id'] in produtos is True:
        print(cadastro['produto_id'])
    else:
        main()
def mensagem_erro_cliente():
    print("Cliente não encontrado, tente novamente")

def procurar_clientes(clientes, cadastro):
    buscar_cliente = None
    for cliente_existe in clientes:
        if cliente_existe['id'] == cadastro['identificacao']:
            buscar_cliente = cadastro
            print("Seu id, é: ", buscar_cliente['identificacao'])
            return buscar_cliente



def buscar_clientes_json(buscar_cliente,buscar_produto, vendas, cadastro):
    if buscar_cliente is None:
        mensagem_erro_cliente()
    else:
        identificador_cliente = cadastro['identificacao']
        produto_decisao(buscar_produto, vendas, cadastro)
        return identificador_cliente


def buscar_produto_identificador(produtos, cadastro):
    buscar_produto = None
    for produto_existe in produtos:
        if produto_existe['id'] == cadastro['produto']:
            buscar_produto = cadastro
            print("Produto encontrado: ", cadastro['produto'])
    return buscar_produto


def mensagem_erro_produto():
    print("Produto não encontrado")


def produto_decisao(buscar_produto, vendas, cadastro):
    if buscar_produto is None:
        mensagem_erro_produto()
    else:
        identificador_produto = cadastro['identificacao']
        escrever_informacoes(vendas, cadastro)
        gravar_info(vendas)
        return identificador_produto



def solicitar_dados():
    produto_id = input("Informe o produto: ")
    id = input("Digite o id do cliente: ")
    quantidade_produto = input("Informe a quantidade do produto: ")
    preco_produto = input("Informe o preço do produto: ")
    cadastro = {
        "produto": produto_id,
        "identificacao": id,
        "Quantidade_produto": quantidade_produto,
        "Preço Produto": preco_produto
    }
    return cadastro


def escrever_informacoes(vendas, cadastro):
    vendas.append(cadastro)

def gravar_info(vendas):
    json.dump(vendas, open("venda.json", "w" ),indent=2 )

def main():
    vendas = informacoes_vendas()
    produtos = informacoes_produtos()
    clientes = informacoes_clientes()
    cadastro = solicitar_dados()
    buscar_cliente = procurar_clientes(clientes, cadastro)
    buscar_produto = buscar_produto_identificador(produtos,cadastro)
    identificador_cliente = buscar_clientes_json(buscar_cliente,buscar_produto, vendas, cadastro)

main()