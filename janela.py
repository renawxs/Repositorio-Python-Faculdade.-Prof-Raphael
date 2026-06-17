import tkinter as tk

def saudar():
    nome = campo.get()
    mensagem.config(text="Eai, " + nome + "!")

janela = tk.Tk()
janela.title("Bem-Vindo")

label = tk.Label(janela, text="Digite seu nome:")
label.pack()

campo = tk.Entry(janela)
campo.pack()

botao = tk.Button(janela, text="Clique aqui", command=saudar)
botao.pack()

mensagem = tk.Label(janela, text="")
mensagem.pack()

janela.mainloop()