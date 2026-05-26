def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    
        total_linhas = len(linhas)
        total_palavras = sum(len(linha.split()) for linha in linhas)
    
        print(f"Total de linhas: {total_linhas}")
        print(f"Total de palavras: {total_palavras}")
    
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
    
ler_arquivo("meu belo nome.txt")