import tkinter as tk
from tkinter import messagebox
import sqlite3


# =========================
# BANCO DE DADOS
# =========================

def conectar_banco():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    conexao.commit()
    return conexao


# =========================
# FUNÇÕES
# =========================

def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Validação dos campos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Todos os campos devem ser preenchidos."
        )
        return

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()
        conexao.close()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente.\n\nErro: {erro}"
        )


def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


def visualizar_clientes():
    try:
        # Conecta ao banco
        conexao = conectar_banco()
        cursor = conexao.cursor()

        # Busca todos os clientes
        cursor.execute("""
            SELECT id, nome, email, telefone
            FROM clientes
            ORDER BY nome
        """)

        clientes = cursor.fetchall()
        conexao.close()

        # Cria uma nova janela
        janela_clientes = tk.Toplevel(janela)
        janela_clientes.title("Clientes Cadastrados")
        janela_clientes.geometry("700x400")
        janela_clientes.resizable(False, False)

        # Título da janela
        tk.Label(
            janela_clientes,
            text="Clientes Cadastrados",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Verifica se existem clientes
        if not clientes:
            tk.Label(
                janela_clientes,
                text="Nenhum cliente cadastrado.",
                font=("Arial", 12)
            ).pack(pady=30)

            return

        # Frame para a tabela
        frame_tabela = tk.Frame(janela_clientes)
        frame_tabela.pack(padx=10, pady=10)

        # Cabeçalhos
        tk.Label(
            frame_tabela,
            text="ID",
            font=("Arial", 10, "bold"),
            width=5,
            relief="solid"
        ).grid(row=0, column=0)

        tk.Label(
            frame_tabela,
            text="Nome",
            font=("Arial", 10, "bold"),
            width=25,
            relief="solid"
        ).grid(row=0, column=1)

        tk.Label(
            frame_tabela,
            text="E-mail",
            font=("Arial", 10, "bold"),
            width=30,
            relief="solid"
        ).grid(row=0, column=2)

        tk.Label(
            frame_tabela,
            text="Telefone",
            font=("Arial", 10, "bold"),
            width=18,
            relief="solid"
        ).grid(row=0, column=3)

        # Exibe os clientes
        for linha, cliente in enumerate(clientes, start=1):
            id_cliente, nome, email, telefone = cliente

            tk.Label(
                frame_tabela,
                text=id_cliente,
                width=5,
                relief="solid"
            ).grid(row=linha, column=0)

            tk.Label(
                frame_tabela,
                text=nome,
                width=25,
                anchor="w",
                relief="solid"
            ).grid(row=linha, column=1)

            tk.Label(
                frame_tabela,
                text=email,
                width=30,
                anchor="w",
                relief="solid"
            ).grid(row=linha, column=2)

            tk.Label(
                frame_tabela,
                text=telefone,
                width=18,
                anchor="w",
                relief="solid"
            ).grid(row=linha, column=3)

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível carregar os clientes.\n\nErro: {erro}"
        )


# =========================
# INTERFACE GRÁFICA
# =========================

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("450x350")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)

# Frame do formulário
frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=10)

# Nome
tk.Label(
    frame_formulario,
    text="Nome:",
    font=("Arial", 11)
).grid(row=0, column=0, padx=5, pady=8, sticky="e")

entrada_nome = tk.Entry(
    frame_formulario,
    width=30
)
entrada_nome.grid(row=0, column=1, padx=5, pady=8)

# E-mail
tk.Label(
    frame_formulario,
    text="E-mail:",
    font=("Arial", 11)
).grid(row=1, column=0, padx=5, pady=8, sticky="e")

entrada_email = tk.Entry(
    frame_formulario,
    width=30
)
entrada_email.grid(row=1, column=1, padx=5, pady=8)

# Telefone
tk.Label(
    frame_formulario,
    text="Telefone:",
    font=("Arial", 11)
).grid(row=2, column=0, padx=5, pady=8, sticky="e")

entrada_telefone = tk.Entry(
    frame_formulario,
    width=30
)
entrada_telefone.grid(row=2, column=1, padx=5, pady=8)


# =========================
# BOTÕES
# =========================

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

# Botão Salvar
botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    width=12,
    command=salvar_cliente,
    bg="#4CAF50",
    fg="white"
)
botao_salvar.grid(row=0, column=0, padx=5)

# Botão Limpar
botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    width=12,
    command=limpar_formulario
)
botao_limpar.grid(row=0, column=1, padx=5)

# Botão Visualizar Clientes
botao_visualizar = tk.Button(
    frame_botoes,
    text="Visualizar Clientes",
    width=20,
    command=visualizar_clientes,
    bg="#2196F3",
    fg="white"
)
botao_visualizar.grid(row=1, column=0, columnspan=2, pady=10)


# =========================
# INICIALIZAÇÃO
# =========================

conectar_banco().close()

entrada_nome.focus()

janela.mainloop()
