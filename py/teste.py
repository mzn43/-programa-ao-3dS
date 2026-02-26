def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

print("Calculadora simples")
print("Operações disponíveis: +, -, *, /")

while True:
    operacao = input("Digite a operação (+, -, *, /) ou 'sair' para encerrar: ")
    if operacao == "sair":
        print("Encerrando a calculadora.")
        break
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        continue

    if operacao == "+":
        print("Resultado:", soma(num1, num2))
    elif operacao == "-":
        print("Resultado:", subtracao(num1, num2))
    elif operacao == "*":
        print("Resultado:", multiplicacao(num1, num2))
    elif operacao == "/":
        print("Resultado:", divisao(num1, num2))
    else:
        print("Operação inválida.")
