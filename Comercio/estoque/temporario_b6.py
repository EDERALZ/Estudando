validacao_data = input("informe a data: ")
data_dia = int(validacao_data[0] + (validacao_data[1]))
tamanho_data = validacao_data
tamanho_data != 10
if data_dia >= 1 and data_dia <= 31:
    print("Está correto")
    data_mes = int(validacao_data[3] + (validacao_data[4]))
    if data_mes >= 1 and data_mes <= 12:
        print("Está correto o mes")
        data_ano = int(validacao_data[6] + (validacao_data[7] + (validacao_data[8] + (validacao_data[9]))))
        if data_ano >= 1 and data_ano <= 9999:
            print("Está correto")
        else:
            print("O ano está incorreto")
    else:
        print("Está incorreto o mes")
else:
    print("Está incorreto")