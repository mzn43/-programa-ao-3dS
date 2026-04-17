1 # Defiição implicita de uma tupla
2 tupla_implicita = (1, 2, 3, 4)
3
4 # Definição explícita de uma tupla
5
lista [5, 6, 7, 8]
6
tupla_explicita tüple(lista)
7
8
print("Tupla implicita:", tupla_implicita, "Tipo:", typ (tupla_implicita))
9
print("Tupla explicita:", tupla_explicita, " Tipo:", type(tupla_explicita))
# Cria uma tupla
empresas = ("Google", "Facebook", "Amazon") 
# Tentativa de alteração 
empresas[1] = "Samsung" 
frutas = ["maçã", "banana", "laranja"] frutas.append("uva")
print(frutas)
Saída esperada:
Python
['maça', 'banana', 'laranja', 'uva']
frutas = ["maçã", "banana", "laranja", "banana"]
frutas.remove("banana")
print(frutas)
Saída esperada:
['maçã', 'laranja', 'banana']
# Definição de uma tupla
frutas = ("maçã", "banana", "laranja", "uva")

# Encontra o índice do elemento "laranja" na tupla
indice_laranja = frutas.index("laranja")

print("O índice de 'laranja' é:", indice_laranja)
import functools
class Aluno:
def init_(self, nome, nota):
self.nome nome
self.nota nota
def
repr (self):
return f'{self.nome}: {self.nota}'
def comparar_alunos (a, b):
return (a.nota b.nota) (a.notab.nota)
[Aluno ('Ana', 88), Aluno ('Rafael', 92), Aluno ('Paulo', 78)] alunos
alunos ordenados sorted (alunos, key=functools.cmp_to_key(comparar_alunos))
print(alunos_ordenados)
