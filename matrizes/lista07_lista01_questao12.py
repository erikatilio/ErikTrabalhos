#12) Entrar com valores inteiros para um matriz A4x4 e para uma matriz B4x4. Gerar e
#imprimir a SOMA (A+B).
#-----------------------------------------------------------------------------------------------------------------------

import random

linhas = 4
colunas = 4
matriz = []

for g in range(linhas):
    linha = []
    for e in range(colunas):
        x = random.randint(1,10)
        linha.append(x)
    matriz.append(linha)

print("Matriz A:")
for x in range(0,4):
    print(matriz[x])

matriz2 = []
for t in range(linhas):
    linha2 = []
    for k in range(colunas):
        u = random.randint(1,10)
        linha2.append(u)
    matriz2.append(linha2)

print("Matriz B:")
for m in range(0,4):
    print(matriz2[m])
soma = []
for d in range(0,4):
    c = d
    somado = []
    for w in range(int(len(matriz))):
        z = int(matriz[c][w])
        b = int(matriz2[c][w])
        f = z + b
        somado.append(f)
    soma.append(somado)
print("Soma:")
for a in range(0,4):
    print(soma[a])