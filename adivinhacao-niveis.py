import random

print("=====================================")
print("      JOGO DE ADIVINHAÇÃO - NÍVEIS    ")
print("=====================================")
print()

print("Escolha o nível de dificuldade:")
print("  [1] Fácil    (número entre 1 e 10)")
print("  [2] Médio    (número entre 1 e 50)")
print("  [3] Difícil  (número entre 1 e 100)")
print()

while True:
    escolha = input("Digite 1, 2 ou 3: ").strip()
    
    if escolha in ['1', '2', '3']:
        break
    print("Opção inválida! Digite 1, 2 ou 3.")

# Definindo o intervalo com base na dificuldade
if escolha == '1':
    nivel = "Fácil"
    minimo, maximo = 1, 10
elif escolha == '2':
    nivel = "Médio"
    minimo, maximo = 1, 50
else:
    nivel = "Difícil"
    minimo, maximo = 1, 100

# Gera o número secreto
secreto = random.randint(minimo, maximo)
tentativas = 0
max_tentativas = 8 if nivel == "Fácil" else 6 if nivel == "Médio" else 5

print(f"\nNível selecionado: {nivel}")
print(f"Vou pensar em um número entre {minimo} e {maximo}...")
print(f"Você tem até {max_tentativas} tentativas.\n")

while tentativas < max_tentativas:
    try:
        palpite = int(input(f"Tentativa {tentativas+1}/{max_tentativas} → Seu palpite: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        continue

    tentativas += 1

    if palpite == secreto:
        print("\n" + "═" * 40)
        print(f"  PARABÉNS! Você acertou em {tentativas} tentativa(s)!  ")
        print("═" * 40)
        break
    
    elif palpite < secreto:
        print("O número secreto é MAIOR ↓")
    else:
        print("O número secreto é MENOR ↑")
    
    if tentativas < max_tentativas:
        print(f"Restam {max_tentativas - tentativas} tentativa(s)\n")
    else:
        print("\n" + "═" * 40)
        print(f"  GAME OVER! O número era {secreto}")
        print("═" * 40)

print("\nFim de jogo. Obrigado por jogar!")
