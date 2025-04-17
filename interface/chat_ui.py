import tkinter as tk
from tkinter import simpledialog

def iniciar_interface(jarvis):
    def enviar():
        pergunta = entrada.get()
        if pergunta.startswith("ensinar:"):
            partes = pergunta[8:].split("->")
            if len(partes) == 2:
                jarvis.ensinar(partes[0].strip(), partes[1].strip())
                resposta = "Entendi, acabei de aprender isso."
            else:
                resposta = "Formato inválido. Use: ensinar: pergunta -> resposta"
        else:
            resposta = jarvis.responder(pergunta)

        chat.insert(tk.END, f"Você: {pergunta}\n", "user")
        chat.insert(tk.END, f"JARVIS: {resposta}\n", "jarvis")
        entrada.delete(0, tk.END)

    janela = tk.Tk()
    janela.title("JARVIS")

    janela.configure(bg='black')
    janela.geometry("600x500")

    chat = tk.Text(janela, bg="black", fg="lime", font=("Consolas", 12))
    chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    chat.tag_config("user", foreground="cyan")
    chat.tag_config("jarvis", foreground="lime")

    entrada = tk.Entry(janela, bg="gray20", fg="white", font=("Consolas", 12))
    entrada.pack(padx=10, pady=10, fill=tk.X)
    entrada.bind("<Return>", lambda event: enviar())

    botao = tk.Button(janela, text="Enviar", command=enviar, bg="gray30", fg="white")
    botao.pack(pady=5)

    janela.mainloop()
