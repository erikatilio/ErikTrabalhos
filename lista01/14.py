#Faça um programa que peça 10 números inteiros,
#calcule e mostre a quantidade de números pares e a quantidade de números impares.
#-----------------------------------------------------------------------------------------------------------------------

c = 0
sum_par = 0
sum_impa = 0

while c < 10:
    number = int(input("Digite um número inteiro: "))
    if number%2 == 0:
        sum_par = sum_par + 1
    if number%2 != 0:
        sum_impa = sum_impa + 1
    c = c + 1

print("A quantidade de números pares é =",sum_par)
print("A quantidade de números impares é =",sum_impa)