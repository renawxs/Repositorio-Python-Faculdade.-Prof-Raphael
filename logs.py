def analisar_log(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    
        erros = conteudo.count("ERROR")
        avisos = conteudo.count("WARNING")
    
        print(f"Análise do arquivo: {nome_arquivo}")
        print(f"ERROR encontrado: {erros} vez(es)")
        print(f"WARNING encontrado: {avisos} vez(es)")
    
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
    
analisar_log("sistema.log")