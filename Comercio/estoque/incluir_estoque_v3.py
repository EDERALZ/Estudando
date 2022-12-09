import json
estoques:list = json.load(open("estoque.json"))
#leitura do arquivo json de produto
produtos:list = json.load(open("../produtos/produto.json"))
#mostrar na tela que está incluindo no estoque
print("Programa de incluir produto no estoque ")
def verificar_letra(letra_digito):
    resultado = True
    if letra_digito < "0" or letra_digito > "9":
        resultado = False
    return resultado

def validacao_data(val_produto):
    data_valida = True
    tamanho_texto = len(val_produto)
    if tamanho_texto != 10:
        data_valida = False
        return data_valida
    posicao_letra = [0,1,3,4,6,7,8,9]
    for indice_letra in posicao_letra:
        resultado_letra = verificar_letra(val_produto[indice_letra])
        if resultado_letra is False:
            data_valida = False
    if val_produto[2] != "/":
        data_valida = False
    if val_produto[5] != "/":
        data_valida = False
    return data_valida
#solicitar informação para usuario
procurar_informacao =  input("Informe o produto a ser encontrado: ")
print(procurar_informacao)
#Verificar informação dentro do arquivo produto.json (id produto)
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
    # Transformar em uma validação correta de data: 31/01/2022
    #olhar se há 10 letras
    # e olhar se todas letras são números e que tenha "/" em lugares certos
    data_valida =validacao_data(val_produto)
    #print("data_valida=" + str(data_valida))

    #continuar lendo o resto das informações
    centro_de_distribuicao = input("Informe o CDD do produto: ")
    quant_produto = str(quantidade_produto)
    validade_produto = str(val_produto)
    cdd = str(centro_de_distribuicao)
    buscar = (None)
    #adicionar informações no vetor
    produtos.append({"Quantidade": quantidade_produto, "Validade do produto": val_produto, "Centro de distribuicao":centro_de_distribuicao})
    estoques.append({"Quantidade": quantidade_produto, "Validade do produto": val_produto, "Centro de distribuicao":centro_de_distribuicao})
    #escrever as informações dentro arquivo json
    json.dump(estoques, open("estoque.json", "w"), indent=2)
    #mostrar na tela que foi incluido no estoque
    print("Produto incluido com sucesso")