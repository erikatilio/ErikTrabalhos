#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
#Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens
#que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens
#o cliente está levando e olhar na tabela de preços.
#Você foi contratado para desenvolver o programa que monta esta tabela de preços,
#que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50
#-----------------------------------------------------------------------------------------------------------------------

items = int(input("Quantos itens o cliente está levando?: "))

item = items
c = 1

while items < 0 or items > 50 or items == 0:
    print("Valor invalido!")
    items = int(input("Quantos itens o cliente está levando?: "))

if 0 < items <= 50:
  while c <= items:
      item = c * 1.99
      if c < item:
        print(c,"- R$%.2f"%item)
        c = c + 1
