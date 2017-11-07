palavra = input()
lista = []
for i in palavra:
    lista.append(i)

if ("").join(lista[::-1]) == ("").join(lista):
    print("True")
else:
    print("False")