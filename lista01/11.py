#Altere o programa anterior para mostrar no final a soma dos números.
#-----------------------------------------------------------------------------------------------------------------------
sum = 0

number1 = int(input("Digite um numero inteiro: "))
number2 = int(input("Digite outro numero inteiro: "))

if number1 < number2:
    while number1 < number2:
        number1 = number1 + 1
        if number1 < number2:
            print(number1)
            sum = sum + number1

elif number2 < number1:
    while number2 < number1:
        number2 = number2 + 1
        if number2 < number1:
            print(number2)
            sum = sum + number2

print(sum)