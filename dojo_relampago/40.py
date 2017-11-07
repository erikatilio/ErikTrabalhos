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

def soma(matriz):
    matriz2 = []
    for x in range(len(matriz)):
        c = x
        i = 0
        while c > i:
            valor = matriz[i][c]
            matriz2.append(valor)
            i += 1
    soma = 0
    for y in range(len(matriz2)):
        soma += matriz2[y]
    return soma

print(soma(matriz(3,3)))