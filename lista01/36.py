#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
#não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
#usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7
#
#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#-----------------------------------------------------------------------------------------------------------------------

number = int(input("Montar a tabuada de: "))
start = int(input("Começar por: "))
finsh = int(input("Terminar em: "))

while start > finsh:
    print("O valor final é maior que o inicial: ")
    start = int(input("Começar por: "))
    finsh = int(input("Terminar em: "))

print("Vou montar a tabuada de",number,"começando em",start,"e terminando em",finsh,":")

while start <= finsh:
    result = number*start
    print(number,"X",start,"=",result)
    start += 1