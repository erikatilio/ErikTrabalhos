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
#50.Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
#-----------------------------------------------------------------------------------------------------------------------

n = int(input("Digite um número: "))

c = 0
h = 0

while c < n:
    h = h + 1/(c+1)
    c = c + 1

print("O valor de H é = ",h)