#-------------------------------------------------------------------------------# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#2.A fórmula para calcular a área de uma circunferência é:
#area = π . raio2. Considerando para este problema que π = 3.14159:
#- Efetue o cálculo da área, elevando o valor de Raio ao quadrado e multiplicando por π.
#Entrada
#A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
#Saída
#Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo,
#com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas,
#não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
#-------------------------------------------------------------------------------

lightning = float(input("Digite o raio do circulo: "))
pi = 3.14159
area = pi*lightning**2

print("A=",round(area,4))
