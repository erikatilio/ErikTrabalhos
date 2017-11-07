lista = []
c = 1
while c != 0:
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    if x > y:
        lista.append("Decrescente")
    elif y > x:
        lista.append("Crescente")
    elif x == y:
        c = 0
for g in lista:
    print(g)