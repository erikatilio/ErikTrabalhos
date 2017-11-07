#Faça um programa que leia 5 números e informe a soma e a média dos números.
#-----------------------------------------------------------------------------------------------------------------------

i = 0
sum = 0

while i < 5:
    number = float(input("digite um numero: "))
    sum = sum + number
    i = i + 1

average = sum / i

print("soma dos numeros digitados =", sum)
print("media dos numeros digitados =", average)
