lista = []
for g in range(100):
    x = int(input())
    lista.append(x)
a = int(max(lista))
b = lista.index(a)
print(a)
print(b+1)