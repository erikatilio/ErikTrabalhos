numeros = input()
size = int(len(numeros))
if numeros.isdigit():
    if int(numeros[0]) == 0 and int(numeros[size - 1]) == 0:
        for g in numeros[1:][:-1][::-1]:
            print(g, end="")
    elif int(numeros[0]) == 0:
        for g in numeros[1:][::-1]:
            print(g,end="")
    elif int(numeros[size-1]) == 0:
        for g in numeros[:-1][::-1]:
            print(g,end="")
    else:
        for g in numeros[::-1]:
            print(g,end="")
else:
    print("erro")