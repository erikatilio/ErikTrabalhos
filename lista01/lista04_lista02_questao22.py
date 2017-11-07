#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#22.Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A,
#e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par
#escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".
#Entrada
#
#Quatro números inteiros A, B, C e D.
#Saída
#
#Mostre a respectiva mensagem após a validação dos valores.
#-----------------------------------------------------------------------------------------------------------------------

a, b, c, d = input().split()
A = float(a)
B = float(b)
C = float(c)
D = float(d)

if(B > C and D > C and C+D > A+B and C > 0 or D > 0 and (A/2) == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')