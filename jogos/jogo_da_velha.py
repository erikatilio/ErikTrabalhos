from funcoes import *

print("Jogo da velha")

#formulando o jogo
jogo = [[ 0 ,0, 0 ],[ 0 ,0, 0 ],[ 0 ,0, 0 ]]
for y in jogo:
    print(y)

#entrada do jogo
acabou = 0
aux = vitoria(jogo)
while acabou < 9 or aux != 0:
    if aux == 1:
        break

    jogada = input("Informe sua jogada: ").split()
    linha = int(jogada[0])
    coluna = int(jogada[1])

    if jogo[linha][coluna] == 0:
        jogo[linha][coluna] = 1
        print("Sua jogada:")
        for y in jogo:
            print(y)
        aux = vitoria(jogo)
        acabou += 1
        if aux == 1:
            break
        print("PC jogada:")
        jogada_aleatoria(jogo)
        aux = vitoria(jogo)
        if aux == 1:
            break
        acabou += 1
    else:
        while jogo[linha][coluna] == 1 or jogo[linha][coluna] == 2:
            print("Jogada errada!")
            jogada = input("Informe sua jogada novamente: ").split()
            linha = int(jogada[0])
            coluna = int(jogada[1])

        if jogo[linha][coluna] == 0:
            jogo[linha][coluna] = 1
            print("Sua jogada:")
            for y in jogo:
                print(y)
            aux = vitoria(jogo)
            acabou += 1
            if aux == 1:
                break
            print("PC jogada:")
            jogada_aleatoria(jogo)
            aux = vitoria(jogo)
            if aux == 1:
                break
            acabou += 1
    print("--------------------")

if aux == 0:
    print("Empate!")
else:
    print("Fim de jogo")