pares = []
impares = []
positivos = []
negativos = []
for g in range(5):
    x = int(input())
    if x % 2 == 0:
        pares.append(x)
        if x > 0:
            positivos.append(x)
        elif x < 0:
            negativos.append(x)
    elif x % 2 != 0:
        impares.append(x)
        if x > 0:
            positivos.append(x)
        elif x < 0:
            negativos.append(x)

print(int(len(pares)), "valor(es) par(es)")
print(int(len(impares)), "valor(es) impar(es)")
print(int(len(positivos)), "valor(es) positivo(s)")
print(int(len(negativos)), "valor(es) negativo(s)")