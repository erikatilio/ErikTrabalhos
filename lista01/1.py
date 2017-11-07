#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
#-----------------------------------------------------------------------------------------------------------------------

grade = float(input("Informe uma nota entre 0 e 10: "))

while grade < 0 or grade > 10:
    grade = float(input("Número errado, Digite novamente: "))
print("Valor válido")
