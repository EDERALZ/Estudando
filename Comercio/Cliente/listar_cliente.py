import json
clientes:list = json.load(open("cliente.json"))

print("id     Nome   Senha     e_mail    endereco")
for clientes_listar in clientes:
    print("", clientes_listar['id'].ljust(5), "", clientes_listar['Nome'].ljust(5), "", clientes_listar['Senha'].ljust(10), "", clientes_listar['E_mail'].ljust(10), "", str(clientes_listar['Endereco'].rjust(20)))