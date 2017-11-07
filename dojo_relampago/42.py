def matriz():
    x = int(input("Linhas:"))
    y = int(input("Colunas:"))
    matriz = []
    for i in range(x):
        linha = []
        for j in range(y):
            linha.append(int(input()))
        matriz.append(linha)

    return matriz

def imprimir_matrizes(matriz):
    for i in matriz:
        print(i)


def menor(matriz):
    c = 1
    soma = 0
    numbers = []
    menor = 0
    while c < len(matriz):
        for x in range(len(matriz)):
            numbers += matriz[x][:-c]
            c += 1
    for x in range(len(numbers)):
        soma += numbers[x]

    return min(numbers)


print(menor(matriz()))