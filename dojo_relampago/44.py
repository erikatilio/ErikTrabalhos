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


def media(matriz):
    matriz2 = []
    for x in range(len(matriz)):
        c = x
        i = 0
        while c > i:
            valor = matriz[i][c]
            matriz2.append(valor)
            i += 1
    produto = 1
    for t in range(len(matriz2)):
        produto *= matriz2[t]
    resul = produto
    return resul

def media2(matriz):
    media2 = []
    for x in range(len(media2)):
        c = x
        f = len(media2)
        i = x
        while f > i:
            valor = matriz[c][i]
            media2.append(valor)
            i += 1
    produto = 1
    for t in range(len(media2)):
        produto *= media2[t]
    resul = produto
    return resul


print(media(matriz(3,3)))
print(media2(matriz(3,3)))