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

print(media(matriz(3,3)))
