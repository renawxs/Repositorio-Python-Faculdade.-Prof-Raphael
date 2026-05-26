import json

arquivo = open("produtos.json", "r", encoding="utf-8")
produtos = json.load(arquivo)
arquivo.close()

total = 0

for p in produtos:
    valor = p["preco"] * p["estoque"]
    total = total + valor
    print(p["nome"], "- valor em estoque: R$", valor)

print("Total geral: R$", total)
