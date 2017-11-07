# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#
# Atleta: Aparecido Parente
#
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04
#-----------------------------------------------------------------------------------------------------------------------

atleta = input("Nome do atleta: ")

c = 0
media = 0
nota_melhor = 0
nota_pior = 0

while c < 7:
    nota01 = float(input("Digite sua nota : "))
    nota02 = float(input("Digite sua nota : "))
    nota03 = float(input("Digite sua nota : "))
    nota04 = float(input("Digite sua nota : "))
    nota05 = float(input("Digite sua nota : "))
    nota06 = float(input("Digite sua nota : "))
    nota07 = float(input("Digite sua nota : "))

    if nota01 > nota02 and nota01 > nota03 and nota01 > nota04 and nota01 > nota05 and nota01 > nota06 and nota01 > nota07:
        nota_melhor = nota01
        print("Melhor nota: ",nota01)

    elif nota02 > nota01 and nota02 > nota03 and nota02 > nota04 and nota02 > nota05 and nota02 > nota06 and nota02 > nota07:
        nota_melhor = nota02
        print("Melhor nota: ",nota02)

    elif nota03 > nota01 and nota03 > nota02 and nota03 > nota04 and nota03 > nota05 and nota03 > nota06 and nota03 > nota07:
        nota_melhor = nota03
        print("Melhor nota: ",nota03)

    elif nota04 > nota01 and nota04 > nota02 and nota04 > nota03 and nota04 > nota05 and nota04 > nota06 and nota04 > nota07:
        nota_melhor = nota04
        print("Melhor nota: ",nota04)

    elif nota05 > nota01 and nota05 > nota02 and nota05 > nota03 and nota05 > nota04 and nota05 > nota06 and nota05 > nota07:
        nota_melhor = nota05
        print("Melhor nota: ",nota05)

    elif nota06 > nota01 and nota06 > nota02 and nota06 > nota03 and nota06 > nota04 and nota06 > nota05 and nota06 > nota07:
        nota_melhor = nota06
        print("Melhor nota: ",nota06)

    elif nota07 > nota01 and nota07 > nota02 and nota07 > nota03 and nota07 > nota04 and nota07 > nota05 and nota07 > nota06:
        nota_melhor = nota07
        print("Melhor nota: ",nota07)

    if nota01 < nota02 and nota01 < nota03 and nota01 < nota04 and nota01 < nota05 and nota01 < nota06 and nota01 < nota07:
        nota_pior = nota01
        print("Pior nota: ", nota01)

    elif nota02 < nota01 and nota02 < nota03 and nota02 < nota04 and nota02 < nota05 and nota02 < nota06 and nota02 < nota07:
        nota_pior = nota02
        print("Pior nota: ", nota02)

    elif nota03 < nota01 and nota03 < nota02 and nota03 < nota04 and nota03 < nota05 and nota03 < nota06 and nota03 < nota07:
        nota_pior = nota03
        print("Pior nota: ", nota03)

    elif nota04 > nota01 and nota04 > nota02 and nota04 > nota03 and nota04 > nota05 and nota04 > nota06 and nota04 > nota07:
        nota_melhor = nota04
        print("Melhor nota: ", nota04)

    elif nota05 > nota01 and nota05 > nota02 and nota05 > nota03 and nota05 > nota04 and nota05 > nota06 and nota05 > nota07:
        nota_melhor = nota05
        print("Melhor nota: ", nota05)

    elif nota06 > nota01 and nota06 > nota02 and nota06 > nota03 and nota06 > nota04 and nota06 > nota05 and nota06 > nota07:
        nota_melhor = nota06
        print("Melhor nota: ", nota06)

    elif nota07 > nota01 and nota07 > nota02 and nota07 > nota03 and nota07 > nota04 and nota07 > nota05 and nota07 > nota06:
        nota_melhor = nota07
        print("Melhor nota: ", nota07)