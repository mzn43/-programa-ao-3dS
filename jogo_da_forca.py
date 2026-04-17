palavra_secreta = "girafa"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]
tentativas = 6

# Desenho do boneco da forca, dividido em 6 partes
desenho_forca = [
    '''
     -----
     |   |
         |
         |
         |
         |
    =======
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    =======
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    =======
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    =======
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =======
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =======
    '''
]

# Função para mostrar o desenho da forca
def mostrar_forca(tentativas_restantes):
    print(desenho_forca[6 - tentativas_restantes])

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra_secreta:
        index = 0
        for letra in palavra_secreta:
            if palpite == letra:
                letras_acertadas[index] = letra
            index += 1
    else:
        tentativas -= 1
        print(f"Você tem {tentativas} tentativas restantes.")
        mostrar_forca(tentativas)  # Mostra a forca a cada erro
    
    print(" ".join(letras_acertadas))

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, você perdeu. A palavra era:", palavra_secreta)
