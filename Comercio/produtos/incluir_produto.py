import json
#vai ler do arquivo e jogar na memória o vetor de produtos
produtos:list = json.load(open("produto.json"))

id_produto = input("Digite o ID do produto: ")
produtos_1 = input("Digite o nome do item: ")
valor_1 = input("Digite o preço do item: ")
imagem_1 = input("Coloque sua imagem")

produto_id = str(id_produto)
produtos_add = str(produtos_1)
valor_i = float(valor_1)
imagem = str(imagem_1)

produtos.append({"id":produto_id,"Nome":produtos_add, "Valor":valor_i, "Imagem": imagem})

#vai escrever o vetor de produtos dentro do arquivo
json.dump(produtos, open("produto.json", "w" ),
          indent=2 ) #indent é a quantidade de espaço que irá ficar ao formator o arquivo de destino na frente de cada linha