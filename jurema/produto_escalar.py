numeros = input().split()
size = int(len(numeros))
escala = int(numeros[0])
for g in numeros[1:]:
    resultado = int(g)*int(escala)
    print(resultado,end=" ")