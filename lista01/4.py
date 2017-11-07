#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
#ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#-----------------------------------------------------------------------------------------------------------------------

populationA = 80000
populationB = 200000
annual_growth_rateA = 0.03
annual_growth_rateB = 0.015

years = 1
while populationA < populationB:
    populationA = populationA * (1 + annual_growth_rateA )
    populationB = populationB * (1 + annual_growth_rateB )
    years = years + 1

print("Populacao A =", round(populationA))
print("Populacao B =", round(populationB))
print("Anos =", years)