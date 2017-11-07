#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50
#-----------------------------------------------------------------------------------------------------------------------

number = int(input("Qual número você deseja ver a tabuada?: "))

c = 1

while c < 11:
    result = number*c
    print(number,"X",c,"=",result)
    c = c + 1
