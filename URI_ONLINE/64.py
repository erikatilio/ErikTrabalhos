positivos = []
for g in range(6):
    numero = input()
    if float(numero) > 0:
        positivos.append(numero)
soma = 0
for e in positivos:
    soma += float(e)
media = soma/int(len(positivos))
print(int(len(positivos)), "valores positivos")
print("%.1f"%media)