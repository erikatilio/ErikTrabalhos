#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
#que o usuário digite o salário inicial do funcionário.
#-----------------------------------------------------------------------------------------------------------------------

salary = float(input("Informe o salário: "))
percentage = float(input("Informe a porcentagem: "))
year = int(input("Informe o ano: "))
year2 = int(input("Informe o ano atual: "))

while year <= year2:
    print("Ano:(",year,") Percentual:(",percentage,") Salario: R$%.2f"%salary)
    salary += (salary * (percentage / 100))
    percentage *= 2
    year += 1

print("Salario atual do funcionario: R$%.2f"%salary)