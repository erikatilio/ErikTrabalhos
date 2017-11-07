#Faça um programa que leia 5 números e informe o maior número.
#-----------------------------------------------------------------------------------------------------------------------
print("Informe 5 números para imprimir o maior deles")

number1 = float(input("Digite um número: "))
number2 = float(input("Digite um número: "))
number3 = float(input("Digite um número: "))
number4 = float(input("Digite um número: "))
number5 = float(input("Digite um número: "))

if number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
    while number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
        print("o maior número é o: ", number1)
        break

if number2 > number1 and number2 > number3 and number2 > number4 and number2 > number5:
    while number2 > number1 and number2 > number3 and number2 > number4 and number2 > number5:
        print("o maior número é o: ", number2)
        break

if number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5:
    while number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5:
        print("o maior número é o: ", number3)
        break

if number4 > number1 and number4 > number2 and number4 > number3 and number4 > number5:
    while number4 > number1 and number4 > number2 and number4 > number3 and number4 > number5:
        print("o maior número é o: ", number4)
        break

if number5 > number1 and number5 > number2 and number5 > number3 and number5 > number4:
    while number5 > number1 and number5 > number2 and number5 > number3 and number5 > number4:
        print("o maior número é o: ", number5)
        break

else:
    if number1 == number2 == number3 == number4 == number5:
        print("operação invalida! números iguais")
