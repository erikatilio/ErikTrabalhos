car = input()
lista = []
for i in car:
    lista.append(i)
size = int(len(lista))
c = 0
lista2 = []
while c < size:
    aux = lista[c]
    if lista.count(aux) >=2:
        lista2.append(aux)
    c += 1
i = 0
while c < len(lista2):
    m = lista2[c]
    n = lista.find(m)
    lista[n] = ""
    c += 1
print(lista)
#-----------------------------------------------------------------------------------------------------------------------

