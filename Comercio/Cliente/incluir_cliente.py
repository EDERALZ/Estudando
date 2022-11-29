import json
clientes:list = json.load(open("cliente.json"))
#Fazer o cliente/usuário preencher suas informações
cliente_id = input("Digite seu id: ")
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
e_mail = input("Informe seu e-mail: ")
endereco = input("Informe seu endereço: ")
#Convertendo as informacoes em string
id_cliente = str(cliente_id)
nome_cliente = str(nome)
senha_cliente = str(senha)
caixa = str(e_mail)
endereco_1 = str(endereco)
#Pegando as informações e incluindo no json
clientes.append({"id":id_cliente,"Nome":nome_cliente, "Senha":senha_cliente, "E_mail":caixa, "Endereco":endereco_1})
#Colocando as informações dentro do arquivo json
json.dump(clientes, open("cliente.json", "w" ), indent=2)