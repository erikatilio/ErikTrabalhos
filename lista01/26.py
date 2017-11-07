# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Diogo Roberto Duarte da Costa 1715310056
# Iury da Silva Coelho          1715310069
#
#26.Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
#-----------------------------------------------------------------------------------------------------------------------

voters = int(input("Digite o número total de eleitores: "))

c = 0

sum1 = 0
sum2 = 0
sum3 = 0

while c < voters:
    vote = int(input("Vote: Digite (1) para Candidato 1; Digite (2) para Candidato 2; Digite (3) para o Candidato 3: "))
    if vote == 1:
        sum1 = sum1 + 1
    if vote == 2:
        sum2 = sum2 + 1
    if vote == 3:
        sum3 = sum3 + 1
    c = c + 1

print(("Candidato (1) teve: "), sum1, ("votos"))
print(("Candidato (2) teve: "), sum2, ("votos"))
print(("Candidato (3) teve: "), sum3, ("votos"))