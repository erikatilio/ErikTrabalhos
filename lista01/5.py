#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.
#-----------------------------------------------------------------------------------------------------------------------
populationA = int(input("Informe a populção de A: "))
populationB = int(input("Informe a populção de B: "))
annual_growth_rateA = float(input("digite a taxa de crescimento populacao A (ex: 0.1 para 10%): "))
annual_growth_rateB = float(input("digite a taxa de crescimento populacao B (ex: 0.1 para 10%): "))

years = 1
while populationA < populationB:
    populationA = populationA * (1 + annual_growth_rateA )
    populationB = populationB * (1 + annual_growth_rateB )
    years = years + 1

print("Populacao A =", round(populationA))
print("Populacao B =", round(populationB))
print("Anos =", years)