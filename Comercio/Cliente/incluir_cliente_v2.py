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
        "cep": cep,
    }
    
    return cadastro

def verificar_email(clientes ,cadastro):
    if cadastro["e_mail"].find("@") > -1:
        cep_valido = verificar_digito(cadastro['cep'])
        verificar_cep(clientes,cadastro, cep_valido)
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
    # if saida == True:
    #     "sim"
    # else:
    #     mensagem_cep()
    return saida


def verificar_cep(clientes,cadastro,cep_valido):
    if cep_valido == True:
        verificar_senha(cadastro)
        escrever_informacoes(clientes, cadastro)
        gravar_informacoes(clientes)
    else:
        mensagem_cep()


def mensagem_senha():
    print("Senha invalida, tente novamente")
    incluir_cliente_v2()

def verificar_senha(cadastro):
    contador_minuscula = 0
    contador_maiuscula = 0
    contador_digito = 0
    contador_simbolo = 0
    if (len(cadastro['Senha']) >= 6):
        for i in cadastro['Senha']:
            if (i.islower()):
                contador_minuscula += 1
            if (i.isupper()):
                contador_maiuscula += 1
            if (i.isdigit()):
                contador_digito += 1
            if (i == '@' or i == '$' or i == '_'):
                contador_simbolo += 1
    if (contador_minuscula >= 1 and contador_maiuscula >= 1 and contador_digito >= 1 and contador_simbolo >= 1
            and contador_minuscula + contador_maiuscula + contador_digito + contador_simbolo == len(cadastro['Senha'])):
        print("Senha valida")
    else:
        mensagem_senha()

def mensagem_cep():
    print("cep informado não existe, tente novamente")
    incluir_cliente_v2()

def mensagem_erro():
    print("Informação errada", "retornando ao início")
    incluir_cliente_v2()


def escrever_informacoes(clientes, cadastro):
    clientes.append({"id": cadastro['id'], "Nome": cadastro['Nome'], "Senha": cadastro['Senha'], "e_mail": cadastro['e_mail'], "cep": cadastro['cep']})


def gravar_informacoes(clientes):
    json.dump(clientes, open("cliente.json", "w" ), indent=2)
    print("Informação gravada com sucesso! ")

def main():
    cadastro = incluir_cliente_v2()
    clientes = load_json()
    verificar_email(clientes, cadastro)

main()


