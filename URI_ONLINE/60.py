positivos = []
for g in range(6):
    numero = input()
    if float(numero) > 0:
        positivos.append(numero)
print(int(len(positivos)), "valores positivos")