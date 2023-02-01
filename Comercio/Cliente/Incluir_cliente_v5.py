import json

def load_json():
    clientes: list = json.load(open("cliente.json"))
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


def verificar_email(clientes, cadastro):
    if cadastro["e_mail"].find("@") > -1:
        cep_valido = verificar_digito(cadastro['cep'])
        verificar_cep(clientes, cadastro, cep_valido)
    else:
        mensagem_erro()


def validate_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, str(cpf)))
    if len(cpf) != 11 or any(cpf[i] != cpf[0] for i in range(1, 11)):
        return False
    prod = [int(cpf[i]) * (len(cpf) - i) for i in range(10)]
    sm = sum(prod)
    digit1 = 11 - sm % 11 if sm % 11 > 1 else 0
    prod = [int(cpf[i]) * (len(cpf) - i) for i in range(10, 11)]
    sm = sum(prod) + digit1 * 2
    digit2 = 11 - sm % 11 if sm % 11 > 1 else 0
    return cpf[-2:] == f'{digit1}{digit2}'


def verificar_cpf():
    pass


def validate_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, str(cnpj)))
    if len(cnpj) != 14 or any(cnpj[i] != cnpj[0] for i in range(1, 14)):
        return False
    prod = [int(cnpj[i]) * (len(cnpj) - i) for i in range(12, -1, -1)]
    sm = sum(prod[:12])
    digit1 = 11 - sm % 11 if sm % 11 > 1 else 0
    prod = [int(cnpj[i]) * (len(cnpj) - i) for i in range(13, -1, -1)]
    sm = sum(prod[:13]) + digit1 * 2
    digit2 = 11 - sm % 11 if sm % 11 > 1 else 0
    return cnpj[-2:] == f'{digit1}{digit2}'

def verificar_cnpj():
    pass

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


def verificar_cep(clientes, cadastro, cep_valido):
    if cep_valido == True:
        verificar_senha(clientes, cadastro)
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
    contador = 0
    if (len(cadastro['Senha']) >= 6):
        for i in cadastro['Senha']:
            if (i.islower()):
                contador_minuscula += 1
            if (i.isupper()):
                contador_maiuscula += 1
            if (i.isdigit()):
                contador_digito += 1
            if (i == '@' or i == '$' or i == '!'):
                contador_simbolo += 1
    #preencher o contador geral baseado nos contadores das letras
    if contador_minuscula >= 1:
        contador += 1
    if contador_maiuscula >= 1:
        contador += 1
    if contador_simbolo >= 1:
        contador += 1
    if contador_digito >= 1:
        contador += 1

    if contador >= 2:
        verificar_pessoa(cadastro)
    else:
        mensagem_senha()

def verificar_pessoa(clientes, cadastro):
    pessoa = input("Você é uma pessoa 'fisica' ou 'juridica'?")
    pessoa = pessoa.lower()
    cadastro['Pessoa'] = pessoa
    if pessoa == 'fisica':
        guardar_cpf = input("Informe seu cpf: ")
        cadastro['CPF'] = guardar_cpf
        escrever_informacoes(clientes, cadastro)
        gravar_informacoes(clientes)
    elif pessoa == 'juridica':
        guardar_cpnj = input("Informe seu cnpj: ")
        cadastro['CNPJ'] = guardar_cpnj
        escrever_informacoes(clientes, cadastro)
        gravar_informacoes(clientes)
    else:
        mensagem_erro_pessoa()

def verificar_cpf():
    pass


def verificar_cnpj():
    pass

def mensagem_digito_erro():
    print("Informação errada ou incompleta")

def mensagem_erro_pessoa():
    print("Você não escolheu pessoa fisica e nem juridica")



def mensagem_cep():
    print("cep informado não existe, tente novamente")
    incluir_cliente_v2()


def mensagem_erro():
    print("Informação errada", "retornando ao início")
    incluir_cliente_v2()


def escrever_informacoes(clientes, cadastro):
    clientes.append(cadastro)

def gravar_informacoes(clientes):
    json.dump(clientes, open("cliente.json", "w"), indent=2)
    print("Informação gravada com sucesso! ")


def main():
    cadastro = incluir_cliente_v2()
    clientes = load_json()
    verificar_email(clientes, cadastro)


main()


