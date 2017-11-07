#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
# utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
#-----------------------------------------------------------------------------------------------------------------------

voter = 1
c = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_white = 0
sum_null = 0

while voter != 0:
    voter = int(input("Vote: jose (1), joão (2), giovana (3), carlos (4), branco (5): "))

    if voter == 1:
        sum_1 += 1
    if voter == 2:
        sum_2 += 1
    if voter == 3:
        sum_3 += 1
    if voter == 4:
        sum_4 += 1
    if voter == 5:
        sum_white += 1
    if voter > 5 or voter <= 0:
        sum_null += 1
    c += 1

percentege_null = (sum_null/c)*100
percentege_white = (sum_white/c)*100

print(sum_1,"- jose/",sum_2,"- joão/",sum_3,"- giovana/",sum_4,"- carlos/")
print("Votos nulos =",sum_null)
print("Votos em branco =",sum_white)
print("Porcentagem de votos nulos sobre o total de votos =",percentege_null,"%")
print("Porcentgem de votos em branco sobre o total de votos =",percentege_white,"%")
