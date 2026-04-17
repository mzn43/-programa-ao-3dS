# Ler o número de elementos
n = int(input("Digite a quantidade de números que deseja adicionar à lista: "))

# Criar a lista e ler os números
numeros = []
for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Ler o número a ser verificado
x = int(input("Digite o número que deseja verificar se está na lista: "))

# Verificar se x está na lista
if x in numeros:
    print(f"{x} está na lista.")
else:
    print(f"{x} não está na lista.")
