# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Iury da Silva Coelho          1715310069
#
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.
#Faça um programa que leia e valide as seguintes informações:
#-----------------------------------------------------------------------------------------------------------------------

username = input("Informe seu username: ")
password = input("Digite sua senha: ")

while username == password:
    print("Não ultilize como password seu username!")
    password = input("Digite sua senha: ")
print("Informações validas")