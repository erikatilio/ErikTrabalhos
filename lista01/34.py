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
#34.Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo
#é aquele que é divisível apenas por um e por ele mesmo.
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#-----------------------------------------------------------------------------------------------------------------------
print("*Atenção: Números primos são definidos apartir de 2*")
number = int(input("Digite um número inteiro para verificar se ele é primo: "))

c = 2

while c < number:
    if number%c == 0:
        c = number
        check = 0
    else:
         c = c + 1
         check = 1
if number == 2:
    check = 2
else:
    if number == 1:
        check = 3

if check == 1 or check == 2:
    print(number,"é primo")
else:
     print(number,"não é primo")