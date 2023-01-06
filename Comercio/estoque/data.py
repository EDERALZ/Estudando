print("Programa data")
dia = input("Informe o dia: ")

if dia <= "1" or dia <= "31":
    print("Está correto! ")
else:
    print("Dia está incorreto ")

mes = input("Informe o mês: ")
if mes <= "1" or mes <= "12":
    print("Está correto!")
else:
    print("Mês está incorreto")

ano = input("Informe o ano: ")
if ano <= "1" or ano <= "9999":
    print("Está correto! ")
else:
    print("Ano está incorreto")
