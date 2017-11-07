#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
#por quais número ele é divisível.
#-----------------------------------------------------------------------------------------------------------------------


number = int(input("Informe um numero: "))
divisibles = []

aux = number - 1
cont = 0

while aux > 1 :
    if (number % aux) == 0 :
        cont += 1
        divisibles.append(aux)
    aux -= 1

if cont == 0 :
    print("O valor eh primo !")
else :
    print("O valor nao eh primo !")
    print("Divisores de %d: " % number)
    print(divisibles)