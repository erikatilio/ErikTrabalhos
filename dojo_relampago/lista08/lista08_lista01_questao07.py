#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para
#a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa
#deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
#prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa
#deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
#O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
#Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
#-----------------------------------------------------------------------------------------------------------------------

def valorPagamento(valor,atraso):
    if (valor < 0):
        return None
    if (atraso > 0):
        multa = valor * 0.03
        adicionalAtraso = valor * (atraso * 0.01)
        return valor + multa + adicionalAtraso
    else:
        return valor
valor = 1
relatorio = 0
quantidade = 0
while valor != 0:
    valor = float(input("Digite o valor a ser pago: "))
    if valor != 0:
        atraso = int(input("Digite quantos dias de atraso: "))
        resultado = valorPagamento(valor,atraso)
        quantidade += 1
        relatorio += resultado
        print("Valor a ser pago: %.2f"%resultado,"R$")
print("Relatorio do dia:")
print("Quantidade de prestações pagas no dia =",quantidade)
print("Valor total de prestações pagas no dia = %.2f"%relatorio)