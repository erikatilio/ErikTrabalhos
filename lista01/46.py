#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
#atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
#informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular
#a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não
#são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
#conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
#
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#
#Melhor salto:  6.5 m
#Pior salto: 5.3 m
#Média dos demais saltos: 5.9 m
#
#Resultado final:
#Rodrigo Curvêllo: 5.9 m
#-----------------------------------------------------------------------------------------------------------------------
athlete = input("Atleta: ")

c = 1
higher = 0
lower = 0

while len(athlete) != 0 or athlete == 0:
    while c != 0:
        jump1 = float(input("Primeiro Salto: "))
        jump2 = float(input("Segundo Salto: "))
        jump3 = float(input("Terceiro Salto: "))
        jump4 = float(input("Quarto Salto: "))
        jump5 = float(input("Quinto salto: "))

        print("Primeiro Salto: ",jump1,"m")
        print("Segundo Salto: ",jump2,"m")
        print("Terceiro Salto: ",jump3,"m")
        print("Quarto Salto: ",jump4,"m")
        print("Quinto Salto: ",jump5,"m")
        print(" ")

        if jump1 > jump2 and jump1 > jump3 and jump1 > jump4 and jump1 > jump5:
            higher = jump1
            print("Melhor salto: ", higher,"m")

        elif jump2 > jump1 and jump2 > jump3 and jump2 > jump4 and jump2 > jump5:
            higher = jump2
            print("Melhor salto: ", higher,"m")

        elif jump3 > jump1 and jump3 > jump2 and jump3 > jump4 and jump3 > jump5:
            higher = jump3
            print("Melhor salto: ", higher,"m")

        elif jump4 > jump1 and jump4 > jump2 and jump4 > jump3 and jump4 > jump5:
            higher = jump4
            print("Melhor salto: ", higher,"m")

        elif jump5 > jump1 and jump5 > jump2 and jump5 > jump3 and jump5 > jump4:
            higher = jump5
            print("Melhor salto: ", higher,"m")

        if jump1 < jump2 and jump1 < jump3 and jump1 < jump4 and jump1 < jump5:
            lower = jump1
            print("Pior salto: ", lower,"m")

        elif jump2 < jump1 and jump2 < jump3 and jump2 < jump4 and jump2 < jump5:
            lower = jump2
            print("Pior salto: ", lower,"m")

        elif jump3 < jump1 and jump3 < jump2 and jump3 < jump4 and jump3 < jump5:
            lower = jump3
            print("Pior salto: ", lower,"m")

        elif jump4 < jump1 and jump4 < jump2 and jump4 < jump3 and jump4 < jump5:
            lower = jump4
            print("Pior salto: ", lower,"m")

        elif jump5 < jump1 and jump5 < jump2 and jump5 < jump3 and jump5 < jump4:
            lower = jump5
            print("Pior salto: ", lower,"m")


        media = (jump1 + jump2 + jump3 + jump4 + jump5 - higher - lower) / 3
        print("A média dos demais saltos: %.1f"%media,"m")
        print(" ")
        print("Resultado final:")
        print(athlete,": %.1f"%media,"m")
        print("----"*100)
        break
    athlete = input("Atleta: ")