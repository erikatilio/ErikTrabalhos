#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
#1 e um número inteiro informado pelo usuário.
#-----------------------------------------------------------------------------------------------------------------------


lim = int(input())
c = 3
div = 2

print("Numeros primos:")

if lim > 2:
    print("2")

while c<lim:

    if c % 2 == 0:
        c += 1

    else:

        if c == div:
            print(c)
            c += 1
            div = 2

        else:

            if c % div == 0:
                c += 1
                div = 2

            else:
                div += 1