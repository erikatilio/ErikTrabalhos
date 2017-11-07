notas = []
erro = []
c = 0
while c != 2:
    n = float(input())
    if 0 < n <= 10:
        notas.append(n)
        c += 1
    else:
        erro.append("nota invalida")
soma = 0
for g in notas:
    soma += g
media = soma/2
for e in erro:
    print(e)
print("media = %.2f"%media)