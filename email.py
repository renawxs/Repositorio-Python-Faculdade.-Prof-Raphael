import re

def validar_email(email):
    padrao = r"@" and r"\."
    if re.search(padrao, email):
        print("Email valido!")
    else:
        print("Email invalido!")

email = input("Digite seu email: ")
validar_email(email)