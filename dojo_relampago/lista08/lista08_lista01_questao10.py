#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#
# 10.Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os
# dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
#-----------------------------------------------------------------------------------------------------------------------

import random

def JogaDadosCraps():
    jogada = random.randint(2, 12)
    return jogada

quantidadeJogadas = 1
acabou = False
ponto = 0

while (not acabou):
    jogada = JogaDadosCraps()
    print("Jogada %d: %d"% (quantidadeJogadas, jogada))
    if (quantidadeJogadas == 1):
        if (jogada == 2) or (jogada == 3) or (jogada == 12):
            print("Craps! Voce Perdeu!")
            acabou = True
        elif (jogada == 7) or (jogada == 11):
            print("Voce Ganhou!")
            acabou = True
        else:
            ponto = jogada
            print("Seu ponto eh %d"% ponto)
    else:
        if (jogada == 7):
            print("'Voce Perdeu!")
            acabou = True
        elif (jogada == ponto):
            print("Voce Ganhou!")
            acabou = True
    quantidadeJogadas += 1