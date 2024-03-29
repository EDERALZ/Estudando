import json

def informar_pesquisa(pesquisar_centro):
    print(pesquisar_centro)
    print("Busca realizada com sucesso!")
    print("Retornando ao início")
    principal()


def load_pesquisar_centro(pesquisar_centro):
    edicao: list = json.load(open("centro_distribuicao.json"))
    pesquisar_cep = verificar_procura(pesquisar_centro, edicao)
    verificar_pesquisa(pesquisar_cep)
    return edicao

def verificar_procura(pesquisar_centro,edicao):
    for pesquisar_cep in edicao:
        if pesquisar_cep['cep'] == pesquisar_centro['cep']:
            encontrar_cep = pesquisar_centro
            return pesquisar_cep

def mensagem_erro_pesquisa():
    print("Busca não encontrada, retornando ao início")
    principal()

def verificar_pesquisa(pesquisar_cep):
    if pesquisar_cep is None:
        mensagem_erro_pesquisa()
    else:
        informar_pesquisa(pesquisar_cep)


def verificar_pesquisar_centro():
    print("Você entou na pesquisa Centro de Distribuição")
    solicitar_cep = input("Digite o CEP que deseja buscar")
    pesquisar_cep = solicitar_cep
    pesquisar_centro = {
        "cep": pesquisar_cep
    }
    load_pesquisar_centro(pesquisar_centro)



def pesquisar_centro_distribuicao(opcao):
    if opcao == "5":
        verificar_pesquisar_centro()
    else:
        principal(opcao)
def saida_opcao_4():
    print("ID não encontrado")
    principal()

def load_opcao_4():
    edicao: list = json.load(open("centro_distribuicao.json"))
    return edicao

def encontrar_id_4(excluir_inf, edicao):
    for id_encontrado in edicao:
        if id_encontrado['id'] == excluir_inf['id']:
            encontrar_id = excluir_inf
            return id_encontrado
def opcao_4_remover(encontrar_id, edicao):
    edicao.remove(encontrar_id)

def dump_opcao_4(edicao):
    json.dump(edicao, open("centro_distribuicao.json", "w"), indent=2)
    print("Excluído com sucesso! ")


def arquivo_opcao_4(encontrar_id):
    edicao = load_opcao_4()
    encontrar_id = encontrar_id_4(encontrar_id, edicao)
    if encontrar_id is None:
        saida_opcao_4()
    else:
        opcao_4_remover(encontrar_id, edicao)
        dump_opcao_4(edicao)
        #principal()

def excluir_entrada_centro():
    print("Você entrou em Excluir Centro de Distribuição ")
    entrada_id = input("Informe o ID que deseja excluir: ")
    print(entrada_id)
    excluir_inf = {
        "id": entrada_id
    }

    arquivo_opcao_4(excluir_inf)
def excluir_centro_distribuicao(opcao):
    if opcao == "4":
        excluir_entrada_centro()
    else:
        pesquisar_centro_distribuicao(opcao)


# def arquivo_editar_centro_distribuicao(cadastro, edicao):


def verificar_imposto_mensagem():
    print("O valor do imposto deve ser entre 0 a 100. ")
    principal()


def edicao_append(cadastro):
    #editar_CEP = input("Informar o CEP a ser alterado: ")
    #editar_imposto_estadual = input("Informar o Imposto Estadual novo: ")
    #editar_imposto_municipal = input("Informar o Imposto Municipal novo: ")
    #editar_imposto_federal = input("Informar o Imposto Federal novo: ")
    edicao.append({"cep": cadastro, "editar_imposto_estadual":
        cadastro, "editar_imposto_municipal": cadastro,
                   "editar_imposto_federal": cadastro})
    print("Informações alteradas com sucesso! ")


def encontrar_informacao_json(cadastro, edicao):
    encontrado = (None)
    for edicao_id in edicao:
        if edicao_id['id'] == cadastro['id']:
            encontrado = cadastro
            return cadastro


def edicao_remover(encontrado):
    edicao.remove(encontrado)


def editar_dump_json(edicao):
    json.dump(edicao, open("centro_distribuicao.json", "w"), indent=2)
    print("Informações alteradas com sucesso ")


def edicao_load_json():
    edicao: list = json.load(open("centro_distribuicao.json"))
    return edicao

def nao_encontrado_centro_distribuicao():
    print("Não encontrado, tente novamente. ")

def arquivo_editar_json(cadastro):
    edicao = json_load()
    encontrado = encontrar_informacao_json(cadastro, edicao)
    if encontrado is None:
        nao_encontrado_centro_distribuicao()
    else:
        edicao_remover(cadastro)
        edicao_append(cadastro)
        dump_json(edicao)
        principal()


def verificar_imposto_efederal(cadastro):
    editar_imposto_municipal = cadastro['imposto_municipal']
    if editar_imposto_municipal >= 0 and editar_imposto_municipal <= 100:
        arquivo_editar_json(cadastro)
    else:
        verificar_imposto_mensagem()


def verificar_imposto_emunicipal(cadastro):
    editar_imposto_municipal = cadastro['imposto_municipal']
    if editar_imposto_municipal >= 0 and editar_imposto_municipal <= 100:
        verificar_imposto_efederal(cadastro)
    else:
        verificar_imposto_mensagem()


def verificar_imposto_eedicao(cadastro):
    editar_imposto_estadual = cadastro['imposto_estadual']
    if editar_imposto_estadual >= 0 and editar_imposto_estadual <= 100:
        verificar_imposto_emunicipal(cadastro)
    else:
        verificar_imposto_mensagem()


def editar_opcao_centro():
    editar_id = input("Informar o ID: ")
    editar_CEP = input("Informar o CEP: ")
    editar_imposto_estadual = int(input("Informar o Imposto Estadual: "))
    editar_imposto_municipal = int(input("Informar o Imposto Municipal: "))
    editar_imposto_federal = int(input("Informar o Imposto Federal: "))
    cadastro = {
        "id": editar_id,
        "cep": editar_CEP,
        "imposto_estadual": editar_imposto_estadual,
        "imposto_municipal": editar_imposto_municipal,
        "imposto_federal": editar_imposto_federal
    }
    verificar_imposto_eedicao(cadastro)


def opcao_editar_centro(opcao):
    if opcao == "3":
        editar_opcao_centro()
    else:
        excluir_centro_distribuicao(opcao)


def informar_imposto_errado():
    print("O valor do imposto deve ser entre 0 a 100. ")
    principal()


def json_load():
    edicao: list = json.load(open("centro_distribuicao.json"))
    return edicao


def edicao_append_json(cadastro, edicao):
    arquivo_id = cadastro['id']
    arquivo_cep = cadastro['cep']
    arquivo_imposto_estadual = cadastro['imposto_estadual']
    arquivo_imposto_municipal = cadastro['imposto_municipal']
    arquivo_imposto_federal = cadastro['imposto_federal']
    edicao.append({"id": arquivo_id, "cep": arquivo_cep, "imposto_estadual": arquivo_imposto_estadual,
                   "imposto_municipal": arquivo_imposto_municipal,
                   "imposto_federal": arquivo_imposto_federal})


def dump_json(edicao):
    json.dump(edicao, open("centro_distribuicao.json", "w"), indent=2)
    print("Adicionado com sucesso! ")


def arquivo_json(cadastro):
    edicao = json_load()
    edicao_append_json(cadastro, edicao)
    dump_json(edicao)
    principal()


def verificar_imposto_federal(cadastro):
    imposto_federal = cadastro['imposto_federal']
    if imposto_federal >= 0 and imposto_federal <= 100:
        arquivo_json(cadastro)
    else:
        informar_imposto_errado()


def verificar_imposto_municipal(cadastro):
    imposto_municipal = cadastro['imposto_municipal']
    if imposto_municipal >= 0 and imposto_municipal <= 100:
        verificar_imposto_federal(cadastro)
    else:
        informar_imposto_errado()


def verificar_imposto_estadual(cadastro):
    imposto_estadual = cadastro['imposto_estadual']
    if imposto_estadual >= 0 and imposto_estadual <= 100:
        verificar_imposto_municipal(cadastro)
    else:
        informar_imposto_errado()


def incluir_novo_centro_distribuicao():
    id = input("Informe novo ID: ")
    cep = input("Informe novo CEP: ")
    imposto_estadual = float(input("Informe imposto estadual: "))
    imposto_municipal = float(input("Informe imposto Municipal: "))
    imposto_federal = float(input('Informe o imposto Federal: '))
    cadastro = {
        "id": id,
        "cep": cep,
        "imposto_estadual": imposto_estadual,
        "imposto_municipal": imposto_municipal,
        "imposto_federal": imposto_federal
    }
    return cadastro


def verificar_opcao_novo_centro(opcao):
    if opcao == "2":
        cadastro = incluir_novo_centro_distribuicao()
        verificar_imposto_estadual(cadastro)
    else:
        opcao_editar_centro(opcao)


def sair_sistema():
    print("Obrigado por usar nosso sistema ")


def verificar_opcao_sair(opcao):
    pass
    if opcao == "1":
        sair_sistema()
    else:
        verificar_opcao_novo_centro(opcao)


def ler_opcao_menu():
    pass
    opcao = input("Digite opção desejada: ")
    return opcao


def exibir_menu():
    print("1 - Sair do sistema")
    print("2 - Incluir novo Centro de Distribuição")
    print("3 - Editar Centro de Distribuição")
    print("4 - Excluir Centro de Distribuição")
    print("5 - Pesquisar Centro de Distribuição pelo CEP")


def mostrar_mensagem():
    print("Programa de centro de distribuição")


def principal():
    mostrar_mensagem()
    exibir_menu()
    opcao = ler_opcao_menu()
    verificar_opcao_sair(opcao)


principal()
