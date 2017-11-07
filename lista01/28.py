# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles.O usuário deverá informar a quantidade de CDs e o valor para em cada um.
#-----------------------------------------------------------------------------------------------------------------------


cd = int(input("Quantos Cd's tem na sua coleção?: "))

while cd <=0:
    print("Informe uma quantidade positiva!")
    cd = int(input("Quantos Cd's tem na sua coleção?: "))

c = 0
sum = 0

while c < cd:
    sale = float(input("Qual o valor do CD?"))
    if sale < 0:
        print("Informe um valor de Cd positivo!")
    if sale > 0:
        sum = sum + sale
        c = c + 1
average = sum/cd

print("O valor total invetido na sua coleção é de = %.2f"%sum,"R$")
print("A média do preço de cada Cd é = %.2f"%average,"R$")