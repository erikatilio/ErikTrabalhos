numeros = input().split()
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])

if a >= b + c:
    print("NAO FORMA TRIANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or a == c or b == c:
        print("TRIANGULO ISOCELES")
if a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or a == c or b == c:
        print("TRIANGULO ISOCELES")
if a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or a == c or b == c:
        print("TRIANGULO ISOCELES")
if a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or a == c or b == c:
        print("TRIANGULO ISOCELES")