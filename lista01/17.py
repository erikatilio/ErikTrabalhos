#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
#-----------------------------------------------------------------------------------------------------------------------

prod = int(input("digite um número: "))

number = prod
fat = 1

while number > 0:
    fat = fat*number
    number = number - 1

print("O fatorial de",prod,"!=",fat)