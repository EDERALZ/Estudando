validacao_data = input("informe a data: ")

validacao_data = [0,1]

def verificar_dia(dia_conferir):
    conferir_dia = True
    if dia_conferir < "1" or dia_conferir > "31":
        conferir_dia = False
        return conferir_dia

def verificar_mes(mes_ver):
    buscar_mes = True
    if mes_ver < "1" or mes_ver > "12":
        buscar_mes = False
        return buscar_mes

def verificar_ano(ano_ver):
    buscar_ano = True
    if ano_ver < "1" or ano_ver > "9999":
        buscar_ano = False
        return buscar_ano

def validacao_date(validacao_data):
    data_valida = True
    tamanho_texto = len(validacao_data)
    if tamanho_texto != 10:
        data_valida = False
        return data_valida
    posicao_dia = [0,1]
    for indice_dia in posicao_dia:
        resultado_dia = verificar_dia(validacao_data[indice_dia])
        if resultado_dia is False:
            data_valida = False
    posicao_mes = [3,4]
    for indice_mes in posicao_mes:
        resultado_mes = verificar_mes(validacao_data[indice_mes])
        if resultado_mes is False:
            data_valida = False
    posicao_ano = [6,7,8,9]
    for indice_ano in posicao_ano:
        resultado_ano = verificar_ano(validacao_data[indice_ano])
        if resultado_ano is False:
            data_valida = False
    if validacao_data[2] != "/":
        data_valida = False
    if validacao_data[5] != "/":
        data_valida = False
    return data_valida
    print("validacao data =", validacao_data)



