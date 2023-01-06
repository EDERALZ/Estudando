import json
def editar_centro():
    edicao:list = json.load(open("Centro.json"))
    centro_id = input("Informe o ID do Centro de distribuição: ")
    usuario_id = input("Informe seu ID: ")
    centro_cep = input("Digite o cep do Centro de distribuição: ")
    editar = {
        "centro_id": centro_id,
        "usuario ID": usuario_id,
        "Centro CEP": centro_cep
    }
    editar_centro(editar)

    edicao.append({"ID centro": centro_id, "Usuario id": usuario_id, "CEP centro":centro_cep})

    json.dump(edicao, open("Centro.json", "w" ),indent=2 )
editar_centro()