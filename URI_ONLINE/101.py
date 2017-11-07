no = input().split()
m = int(no[0])
n = int(no[1])
if n > m:
    soma = 0
    lista = []
    for g in range(m,n):
        soma += int(g)
        lista.append(g)
    a = (" ").join(lista)
    print(str(a),"Sum=",soma)
elif m > n:
    soma = 0
    lista = []
    for e in range(n,m):
        soma += int(e)
        lista.append(e)
    b = (" ").join(lista)
    print(str(b),"Sum=",soma)