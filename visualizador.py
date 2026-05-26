import tkinter as tk

def calcular(operacao):
    numero1 = float(campo1.get())
    numero2 = float(campo2.get())

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            label_resultado.config(text="Erro! Nao pode dividir por zero!")
            return
        resultado = numero1 / numero2

    label_resultado.config(text="Resultado: " + str(resultado))

janela = tk.Tk()
janela.title("Calculadora")

tk.Label(janela, text="Digite o primeiro numero:").pack()
campo1 = tk.Entry(janela)
campo1.pack()

tk.Label(janela, text="Digite o segundo numero:").pack()
campo2 = tk.Entry(janela)
campo2.pack()

tk.Button(janela, text="+", command=lambda: calcular("+")).pack()
tk.Button(janela, text="-", command=lambda: calcular("-")).pack()
tk.Button(janela, text="*", command=lambda: calcular("*")).pack()
tk.Button(janela, text="/", command=lambda: calcular("/")).pack()

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

janela.mainloop()