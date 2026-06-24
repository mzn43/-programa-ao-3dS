class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"


# Entrada de dados do usuário
titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
paginas = int(input("Digite a quantidade de páginas: "))

# Criação do objeto Livro
livro = Livro(titulo, autor, paginas)

# Exibição usando o método __str__()
print(livro)
