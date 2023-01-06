from datetime import date

informacao_data = input("Informe a data: ")
data_atual  = date.today()
data_escrita = data_atual.strftime('%d/%m/%Y')
print(informacao_data)
