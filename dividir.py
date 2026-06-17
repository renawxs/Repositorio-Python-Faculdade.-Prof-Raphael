def dividir():
    try:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro! Nao e possivel dividir por zero.")
    except ValueError:
        print("Erro! Digite apenas numeros.")

dividir()