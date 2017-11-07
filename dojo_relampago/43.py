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
    media = []
    for g in range(len(matriz)):
        c = g
        for u in range(0,c):
            valor = matriz[c][u]
            media.append(valor)
    soma = 0
    for t in range(len(media)):
        soma += media[t]
    media = soma/ len(media)
    return media

def media2(matriz):
    media2 = []
    for x in range(1,len(matriz)):
        f = len(matriz)
        d = f - x
        i = x
        while d != f:
            valor = matriz[i][d]
            media2.append(valor)
            d += 1
    soma = 0
    for t in range(len(media2)):
        soma += media2[t]
    media_sec = soma/ len(media2)
    return media_sec

print(media(matriz(3,3)))
print(media2(matriz(3,3)))