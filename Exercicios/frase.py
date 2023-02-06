import json

frases = []

while True:
    text = input("Digite uma frase: ")
    if text in frases:
        print("O texto que você digitou é repetido. ")
        break
    else:
        print("O texto que você digitou é novo")
        frases.append(text)

        with open("frases.json", "w") as file:
            json.dump(frases, file)