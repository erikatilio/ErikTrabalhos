#13) Entrar com valores para duas matrizes inteiras de ordem cinco. Gerar e imprimir a
#matriz diferença.
#-----------------------------------------------------------------------------------------------------------------------

import random

linhas = 5
colunas = 5
matriz = []

for g in range(linhas):
    linha = []
    for e in range(colunas):
        x = random.randint(1,10)
        linha.append(x)
    matriz.append(linha)

print("Matriz A:")
for x in range(0,5):
    print(matriz[x])

matriz2 = []
for t in range(linhas):
    linha2 = []
    for k in range(colunas):
        u = random.randint(1,10)
        linha2.append(u)
    matriz2.append(linha2)

print("Matriz B:")
for m in range(0,5):
    print(matriz2[m])
diferença = []
for d in range(0,5):
    c = d
    dif = []
    for w in range(int(len(matriz))):
        z = int(matriz[c][w])
        b = int(matriz2[c][w])
        f = z - b
        dif.append(f)
    diferença.append(dif)
print("Diferença:")
for a in range(0,4):
    print(diferença[a])