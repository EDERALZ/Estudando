import json

def load_json():
    clientes:list = json.load(open("cliente.json"))
    return clientes


def incluir_cliente_v2():
    cliente_id = input("Digite seu id: ")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    e_mail = input("Informe seu e-mail: ")
    cep = input("Informe seu CEP: ")
    cadastro = {
        "id": cliente_id,
        "Nome": nome,
        "Senha": senha,
        "e_mail": e_mail,
        "endereco": cep,
    }
    
    return cadastro

def verificar_email(clientes ,cadastro):
    if cadastro["e_mail"].find("@") > -1:
        verificar_digito()
        escrever_informacoes(clientes, cadastro)
        gravar_informacoes(clientes)
    else:
        mensagem_erro()

def verificar_digito(entrada):
    saida = True
    try:
        if entrada[0] < "0" or entrada[0] > "9":
            saida = False
        if entrada[1] < "0" or entrada[1] > "9":
            saida = False
        if entrada[2] < "0" or entrada[2] > "9":
            saida = False
        if entrada[3] < "0" or entrada[3] > "9":
            saida = False
        if entrada[4] < "0" or entrada[4] > "9":
            saida = False
        if entrada[5] != "-":
            saida = False
        if entrada[6] < "0" or entrada[6] > "9":
            saida = False
        if entrada[7] < "0" or entrada[7] > "9":
            saida = False
        if entrada[8] < "0" or entrada[8] > "9":
            saida = False
    except IndexError:
        saida = False
    return saida


def mensagem_erro():
    print("Informação errada", "retornando ao início")
    incluir_cliente_v2()


def escrever_informacoes(clientes, cadastro):
    clientes.append({"id": cadastro['id'], "Nome": cadastro['Nome'], "Senha": cadastro['Senha'], "e_mail": cadastro['e_mail'], "cep": cadastro['cep']})


def gravar_informacoes(clientes):
    json.dump(clientes, open("cliente.json", "w" ), indent=2)

def main():
    cadastro = incluir_cliente_v2()
    clientes = load_json()
    saida = verificar_email(clientes, cadastro)

main()


