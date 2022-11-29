import json
estoques:list = json.load(open("estoque.json"))

print("id     Nome   Senha     e_mail    endereco")
for estoque_listar in estoques:
    print("", estoque_listar['ID produto'].ljust(5), "", estoque_listar['Quantidade'].ljust(5), "", estoque_listar['Validade'].ljust(10), "", estoque_listar['Centro de distribuicao'].ljust(10))