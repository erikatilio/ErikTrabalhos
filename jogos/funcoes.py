import random

def jogada_aleatoria(jogo):
    for x in range(1):
        i = random.randint(0,2)
        j = random.randint(0,2)
    if jogo[i][j] == 0:
        jogo[i][j] = 2
        for y in jogo:
            print(y)
    else:
         while jogo[i][j] == 1 or jogo[i][j] == 2:
             for x in range(1):
                 i = random.randint(0, 2)
                 j = random.randint(0, 2)
         if jogo[i][j] == 0:
             jogo[i][j] = 2
             for y in jogo:
                 print(y)

def vitoria(jogo):
    ver = 0
    # vertical possibilidades de vencer
    if jogo[0][0] == jogo[1][0] == jogo[2][0] and jogo[0][0] != 0 and jogo[1][0] != 0 and jogo[2][0] != 0:
        vencedor = jogo[0][0]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    if jogo[0][1] == jogo[1][1] == jogo[2][1] and jogo[0][1] != 0 and jogo[1][1] != 0 and jogo[2][1] != 0:
        vencedor = jogo[0][1]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    if jogo[0][2] == jogo[1][2] == jogo[2][2] and jogo[0][2] != 0 and jogo[1][2] != 0 and jogo[2][2] != 0:
        vencedor = jogo[0][2]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    # horizontal possibilidades de vencer
    if jogo[0][0] == jogo[0][1] == jogo[0][2] and jogo[0][0] != 0 and jogo[0][1] != 0 and jogo[0][2] != 0:
        vencedor = jogo[0][0]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    if jogo[1][0] == jogo[1][1] == jogo[1][2] and jogo[1][0] != 0 and jogo[1][1] != 0 and jogo[1][2] != 0:
        vencedor = jogo[1][0]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    if jogo[2][0] == jogo[2][1] == jogo[2][2] and jogo[2][0] != 0 and jogo[2][1] != 0 and jogo[2][2] != 0:
        vencedor = jogo[2][0]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    # diagonais possibilidades de vencer
    if jogo[0][0] == jogo[1][1] == jogo[2][2] and jogo[0][0] != 0 and jogo[1][1] != 0 and jogo[2][2] != 0:
        vencedor = jogo[0][0]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    if jogo[0][2] == jogo[1][1] == jogo[2][0] and jogo[0][2] != 0 and jogo[1][1] != 0 and jogo[0][2] != 0:
        vencedor = jogo[0][2]
        print("O jogador", vencedor, "venceu!")
        ver = 1
    return ver