numeros = input().split()
size = int(len(numeros))
if size > 20 and size < 0:
    while size > 20 and size < 0:
        numeros = input().split()
        size = int(len(numeros))
else:
    menor = min(numeros)
    posicao = numeros.index(menor)
    print(menor, (posicao+1))