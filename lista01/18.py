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
#18.Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#-----------------------------------------------------------------------------------------------------------------------
n = int(input("Quantos números serão inputados?: "))

c = 0
sum = 0

x = int(input())
larger = x
smaller = x

while c < n-1:
    x = int(input())
    if x < smaller:
        larger = x
    if x > larger:
        larger = x
    c = c + 1
    sum = sum + x

print("Menor valor: %d" % smaller)
print("Maior valor: %d" % larger)
print("Soma: %d" % sum)