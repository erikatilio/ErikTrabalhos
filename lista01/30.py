#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
#que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços
#de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
#
#   Preço do pão: R$ 0.18
#   Panificadora Pão de Ontem - Tabela de preços
#   1 - R$ 0.18
#   2 - R$ 0.36
#   ...
#   50 - R$ 9.00
#-----------------------------------------------------------------------------------------------------------------------

breads = int(input("Quantos pães o cliente está levando?: "))

bread = breads
c = 1

while breads < 0 or breads > 50 or breads == 0:
    print("Valor invalido!")
    breads = int(input("Quantos pães o cliente está levando?: "))

print("Preço do pão: R$ 0.18")
print("Panificadora Pão de Ontem - Tabela de preços")

if 0 < breads <= 50:
    while c <= breads:
        bread = c * 0.18
        if c > bread:
            print(c,"- R$%.2f"%bread)
            c = c + 1