#Faça um programa que calcule o mostre a média aritmética de N notas.
#-----------------------------------------------------------------------------------------------------------------------

number = int(input("digite um numero de notas que serão avaliadas: "))

c = 0
sum = 0

while c < number:
    grade = int(input("digite a nota: "))
    sum = sum + grade
    c = c + 1
average = sum / c

print("Média igual a:", average)