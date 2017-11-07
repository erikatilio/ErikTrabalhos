def matriz(x,y):
    matriz = []
    for i in range(y):
        linha = []
        for j in range(y):
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)
    for b in matriz:
        print(b)
    return matriz

def menor(matriz):
    menor = []
    for x in range(1,len(matriz)):
        f = len(matriz)
        d = f - x
        i = x
        valor = matriz[i][d:f]
        menor.append(valor)
    menor_valor = min(menor)
    return menor_valor

print(menor(matriz(4,4)))
