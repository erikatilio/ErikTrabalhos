#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#
#25) Criar um algoritmo que leia valores para uma matriz M2x2. Calcular e imprimir o
#determinante. Para cálculo do determinante de uma matriz de ordem 2, é simplesmente
#computar a diferença entre os produtos das diagonais principal e secundária,
#respectivamente.
#-----------------------------------------------------------------------------------------------------------------------

colunas = 2
linhas = 2
matriz = []
for g in range(linhas):
    linha = []
    for e in range(colunas):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz.append(linha)
dp = (int(matriz[0][0]))*(int(matriz[1][1]))
ds = (int(matriz[0][1]))*(int(matriz[1][0]))
det = dp - ds
print(det)