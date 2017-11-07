#3) Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
#somente os elementos acima da diagonal principal.
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
print("Matriz:")
for x in range(0,10):
    print(matriz[x])
print("Acima da diagonal principal:")
for t in range(0,10):
    print(matriz[t][t+1:])