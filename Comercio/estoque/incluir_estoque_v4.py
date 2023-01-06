#na hora de validar a data, terá que olhar o dia data ele é um número
#de 1 a 31, o mês um numero de 1 a 12
#e o ano numero de 1 a 9999
import json
estoques:list = json.load(open("estoque.json"))
produtos:list = json.load(open("../produtos/produto.json"))
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
    data_valida = validacao_data(val_produto)
    if data_valida is False:
        print("Informação incorreta, retornando ao início")

    else:
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




#passo 1: receber a entrada, que o usuário irá informar
#passo 2: processamento
#passo 3 : saída; final do programa
