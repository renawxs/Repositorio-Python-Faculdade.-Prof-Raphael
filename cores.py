import tkinter as tk

def mudar_cor():
    cor = cor_escolhida.get()
    janela.config(bg=cor)

janela = tk.Tk()
janela.title("Seletor de Cores")
janela.geometry("300x200")

cor_escolhida = tk.StringVar()

tk.Label(janela, text="Escolha uma cor:").pack(pady=10)

tk.Radiobutton(janela, text="Vermelho", variable=cor_escolhida, value="red", command=mudar_cor).pack(pady=5)
tk.Radiobutton(janela, text="Verde", variable=cor_escolhida, value="green", command=mudar_cor).pack(pady=5)
tk.Radiobutton(janela, text="Azul", variable=cor_escolhida, value="blue", command=mudar_cor).pack(pady=5)

janela.mainloop()