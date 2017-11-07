#4) Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e imprima a
#soma dos elementos que estão acima da diagonal principal:
#-----------------------------------------------------------------------------------------------------------------------

import random

linhas = 10
colunas = 10
matriz = []
for g in range(linhas):
    linha = []
    for e in range(colunas):
        x = random.randint(1,10)
        linha.append(x)
    matriz.append(linha)
print("Matriz:")
for x in range(0,10):
    print(matriz[x])
print("Acima da diagonal principal:")
soma = []
for t in range(0,10):
    print(matriz[t][t+1:])
    v = matriz[t][t+1:]
    soma.append(v)
soma2 = 0

for u in range(0,10):
    p = u
    for h in range(int(len(soma[p]))):
        soma2 += int(soma[p][h])
print("A soma:")
print(soma2)