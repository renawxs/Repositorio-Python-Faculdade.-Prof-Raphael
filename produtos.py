import json
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3599.90, "estoque": 15},
    {"id": 2, "nome": "Mouse", "preco": 129.90, "estoque": 42},
    {"id": 3, "nome": "Teclado", "preco": 239.90, "estoque": 30},
    {"id": 4, "nome": "Monitor", "preco": 1899.00, "estoque": 8},
    {"id": 5, "nome": "Headset", "preco": 399.90, "estoque": 25},
]
with open("produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
print("Arquivo produtos.json criado com sucesso!")