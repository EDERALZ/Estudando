import json
def informar_entrada():
  resultado = input("informe qual é a entrada: ")
  return resultado



def verificar_problemas(entrada):
  if entrada == "0":
    return "erro: entrada não pode ser zero"
  else:
    return None
def gravar_mudancas(entrada):
  vetor = json.load(open("banco_de_dados.json"))

  vetor.append(entrada)

  json.dump(vetor, open("banco_de_dados.json", "w"))
def programa_principal():
  entrada = informar_entrada()
  problema = verificar_problemas(entrada)
  if problema is not None:
    print(problema)
    return
  else:
    gravar_mudancas(entrada)
    print("cadastrado com sucesso")
    return
programa_principal()

#pensar no sistema de incluir estoque


