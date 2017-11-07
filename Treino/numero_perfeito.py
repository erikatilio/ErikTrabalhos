def per(n):
    cont = 1
    soma = 0
    while cont < n:
        if n % cont == 0:
            soma += cont
            cont += 1
        else:
            cont += 1
    if soma == n:
        print(n,"eh perfeito")
    else:
        print(n,"nao eh prefeito")

vezes = int(input())
numeros = []
for g in range(vezes):
    number = int(input())
    numeros.append(number)
for e in numeros:
    per(e)