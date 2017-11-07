numeros = input().split()
size = int(len(numeros))
if size < 20 and size > 20:
    while size < 20 and size > 20:
        numeros = input().split()
        size = int(len(numeros))
else:
    soma = 0
    for g in numeros:
        soma += int(g)
    print(soma)