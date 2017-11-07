#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
#dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#
#Valor da Dívida| Valor dos Juros| Quantidade de Parcelas|  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67
#-----------------------------------------------------------------------------------------------------------------------divida = int(input("Digite o valor da sua divida: "))
divida = float(input("Digite o valor da sua divida: "))

c = 1
valor = 0
juros = 0
porcentagem_juros = 0
parcelas = 1
valor_parcelas = 0
divida_com_juros = 0

print( "Valor da Dívida         |  Quantidade de Parcelas       |   Valor dos Juros             |   Valor da Parcela ")
print("-"*130)

while c <= 5:
    if c == 1:
        valor_parcelas = divida
        print("Valor da divida =%.2f"%divida, "  |   ", "Valor dos juros =", juros, "   |   ",
              "Quantidades de parcelas =", parcelas, "    |   ", "Valor das parcelas =%.2f"%valor_parcelas)
        parcelas = 3
        porcentagem_juros = 100

    else:
        juros = porcentagem_juros
        valor_parcelas = (divida + juros)/parcelas
        divida_com_juros = divida + juros
        print("Valor da divida =%.2f"%divida_com_juros, "  |   ", "Valor dos juros =",juros, "   |   ",
              "Quantidades de parcelas =",parcelas, "    |   ", "Valor das parcelas =%.2f"%valor_parcelas)
        parcelas += 3
        porcentagem_juros += 50
    c += 1