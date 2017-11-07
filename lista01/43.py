#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
#Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
#Considere que o cliente deve informar quando o pedido deve ser encerrado.
#-----------------------------------------------------------------------------------------------------------------------

valor = 0
sum = 0
codigo = 1

while codigo != 0:
    codigo = int(input("digite o codigo do produto ou 0 para sair: "))
    if codigo != 0:
        qty = int(input("digite a quantidade do produto: "))
        if codigo == 100:
            valor = 1.2
        elif codigo == 101:
            valor = 1.3
        elif codigo == 102:
            valor = 1.5
        elif codigo == 103:
            valor = 1.2
        elif codigo == 104:
            valor = 1.3
        elif codigo == 105:
            valor = 1.0
        valorParcial = valor * qty
        print(codigo, " -- ", qty, " --- R$", valorParcial)
        sum = sum + valorParcial
if sum != 0:
    print("valor total = R$", sum)