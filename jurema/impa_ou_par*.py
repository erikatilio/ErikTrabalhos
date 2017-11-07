numeros = input().split()
size = int(len(numeros))
if size > 5 and size < 0:
    while  size > 5 and size < 0:
        numeros = input().split()
        size = int(len(numeros))
else:
    vetor = []
    for g in numeros:
        if int(g) % 2 == 0:
            vetor.append("par")
        elif int(g) % 2 != 0:
            vetor.append("ímpa")
print((" ").join(vetor))