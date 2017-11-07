#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
#Não utilize a função de potência da linguagem.
#-----------------------------------------------------------------------------------------------------------------------

base = int(input("Informe um número como base: "))
exponent = int(input("Informe um número como expoente: "))

result = 1
c = 0

while c < exponent:
    result = result*base
    c = c + 1

print(base,"^",exponent,"=",result)