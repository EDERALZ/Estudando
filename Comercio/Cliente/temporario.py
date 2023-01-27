a, b, c, d = 0, 0, 0, 0
senha = input("Digite uma senha: ")

if (len(senha) >= 6):
    for i in senha:
        if (i.islower()):
            a += 1
        if (i.isupper()):
            b += 1
        if (i.isdigit() or i.isnumeric()):
            c += 1
        if(i == '@' or i == '$' or i == '_'):
            d += 1

if (a >= 1 and b >= 1 and c >= 1 and d >= 1 and a+b+c+d == len(senha)):
    print("Senha valida")
else:
    print("Senha invalida")