import json

def ler_json():
    return json.load(open("cliente.json"))
clientes:list = ler_json()
def pegar_id():
    guardar_id = input("Informe o id será alterado: ")
    return guardar_id
guardar_id = pegar_id()

def encontrar_id():
    encontrado = (None)
    for id_usuario in clientes:
        if guardar_id == id_usuario['id']:
            encontrado = id_usuario
            return id_usuario
encontrado = encontrar_id()

def memorizar_info():
    nome = input("Insira o nome correto do cliente: ")
    senha = input("Informe a senha nova:")
    e_mail = input("Digite seu e_mail: ")
    endereco = input("Informe seu endereço: ")
    id_usuario = (guardar_id)
    nome_cliente = str(nome)
    senha_1 = str(senha)
    e_mail_novo = str(e_mail)
    endereco_novo = str(endereco)
    #irá remover e adicionar
    clientes.remove(encontrado)
    clientes.append({"id":guardar_id,"Nome":nome_cliente,
                     "Senha":senha_1, "E_mail":e_mail_novo, "Endereco":endereco_novo})

def alterar_info():
    json.dump(clientes, open("cliente.json", "w"), indent=2)
    print("Dados alterados com sucesso")

def laco_info():
    if encontrado is None:
        print("Cliente não encontrado ou informação errada")
    else:
        memorizar_info()
        alterar_info()
laco_info()