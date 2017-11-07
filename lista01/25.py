#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
#varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem,
#adulta ou idosa, conforme a média calculada.
#-----------------------------------------------------------------------------------------------------------------------

people = int(input("Quantas pessoas tem na turma?: "))

c = 0
sum = 0

while c < people:
    age = int(input("Informe sua idade: "))
    sum = sum + age
    c = c + 1
average = sum/ c

if average <= 25:
    print("A turma é jovem")
if 26 <= average <= 60:
    print("A turma é adulta")
if average > 60:
    print("A turma é idosa")
