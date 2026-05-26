import re

def validar_senha(senha):
    if len(senha) < 8:
        print("Senha invalida! Precisa ter pelo menos 8 caracteres.")
    elif not re.search(r"[A-Z]", senha):
        print("Senha invalida! Precisa ter pelo menos uma letra maiuscula.")
    elif not re.search(r"[a-z]", senha):
        print("Senha invalida! Precisa ter pelo menos uma letra minuscula.")
    elif not re.search(r"[0-9]", senha):
        print("Senha invalida! Precisa ter pelo menos um numero.")
    elif not re.search(r"[!@#$%&*]", senha):
        print("Senha invalida! Precisa ter pelo menos um caractere especial (!@#$%&*).")
    else:
        print("Senha valida!")

senha = input("Digite sua senha: ")
validar_senha(senha)