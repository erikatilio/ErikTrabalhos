#1) Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva os
#elementos da diagonal principal.
#-----------------------------------------------------------------------------------------------------------------------

import random

linhas = 10
colunas = 10
matriz = []
for g in range(linhas):
    linha = []
    for e in range(colunas):
        x = random.randint(1,100)
        linha.append(x)
    matriz.append(linha)
for x in range(0,10):
    print(matriz[x])
for e in range(0,10):
    print(matriz[e][e])
