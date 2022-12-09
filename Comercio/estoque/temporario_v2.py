val_produto = input("Informe a validade do produto incluido: ")
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
data_valida = validacao_data(val_produto)
print("data_valida=" + str(data_valida))