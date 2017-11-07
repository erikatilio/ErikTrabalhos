#Altere o programa de cálculo do fatorial,
#permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos
#e menores que 16.
#-----------------------------------------------------------------------------------------------------------------------

quant = int(input("Informe quantas vezes pretende rodar o fatorial: "))

c = 0

while c < quant:
    prod = int(input("Digite um número entre 0 e 16: "))

    if prod <= 16 and prod > 0:
        number = prod
        fat = 1

        while number > 0:
            fat = fat*number
            number = number - 1

        print("O fatorial de",prod,"!=",fat)

    else:
        print("O número informado não está entre 0 e 16!")
    c = c + 1