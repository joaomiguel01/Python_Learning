import tkinter as tk
from tkinter import messagebox

# Função para cadastrar o produto
def cadastrar_produto():
    cliente = entry_cliente.get()
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    categoria = entry_categoria.get()

    if cliente and produto and quantidade and categoria:
        # Aqui você poderia salvar em um banco de dados ou arquivo
        messagebox.showinfo("Cadastro", f"Produto '{produto}' cadastrado com sucesso!")
        
        # Limpa os campos após o cadastro
        entry_cliente.delete(0, tk.END)
        entry_produto.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos antes de cadastrar.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Produtos")
janela.geometry("400x300")

# Labels e campos de entrada
tk.Label(janela, text="Cliente:").pack(pady=5)
entry_cliente = tk.Entry(janela, width=40)
entry_cliente.pack()

tk.Label(janela, text="Produto:").pack(pady=5)
entry_produto = tk.Entry(janela, width=40)
entry_produto.pack()

tk.Label(janela, text="Quantidade:").pack(pady=5)
entry_quantidade = tk.Entry(janela, width=40)
entry_quantidade.pack()

tk.Label(janela, text="Categoria:").pack(pady=5)
entry_categoria = tk.Entry(janela, width=40)
entry_categoria.pack()

# Botão de cadastro
btn_cadastrar = tk.Button(janela, text="Cadastrar Produto", command=cadastrar_produto, bg="lightblue")
btn_cadastrar.pack(pady=20)

# Inicia o loop da janela
janela.mainloop()
