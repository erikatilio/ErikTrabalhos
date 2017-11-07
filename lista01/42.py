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
#42.Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
#seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
#  A entrada de dados deverá terminar quando for lido um número negativo.
#-----------------------------------------------------------------------------------------------------------------------

c = 0

sum0_25 = 0
sum26_50 =0
sum51_75 = 0
sum76_100 = 0

number = float(input("Digite qualquer número"))
while number > 0:
    if 0 < number <= 25:
        sum0_25 = sum0_25 + 1
    if 25 < number <= 50:
        sum26_50 = sum26_50 + 1
    if 50 < number <= 75:
        sum51_75 = sum51_75 + 1
    if 75 < number <= 100:
        sum76_100 = sum76_100 + 1
    c = c + 1


print("Existem" ,sum0_25,"entre 0 e 25 ")
print("Existem" ,sum26_50,"entre 26 e 50 ")
print("Existem" ,sum51_75,"entre 52 e 75 ")
print("Existem" ,sum76_100,"entre 76 e 100")