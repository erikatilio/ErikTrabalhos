#Faça um programa que leia e valide as seguintes informações:
#
#   Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#   Salário: maior que zero;
#   Sexo: 'f' ou 'm';
#   Estado Civil: 's', 'c', 'v', 'd';
#-----------------------------------------------------------------------------------------------------------------------

name = input("Informe seu nome: ")
while len(name) < 3:
    print("Nome maior que 3 letras!")
    name = input("Informe seu nome novamente: ")

age = int(input("Informe sua idade: "))
while age < 0 or age > 150:
    print("Idade inválida!")
    age = int(input("Informe sua idade novamente: "))

salary = float(input("Informe seu salário: "))
while salary <= 0:
    print("Salário inválido!")
    salary = float(input("Informe seu salário novamente: "))

sex = input("Informe seu sexo (f)Feminino ou (m)Masculino: ")
while sex != 'f' or sex != 'm':
    print("Sexo informado inválido!")
    sex = input("Informe seu sexo novamente (f)Feminino ou (m)Masculino: ")

state_civil = input("Informe seu estado civil, (s)Solteiro, (c)Casado, (v)Viúvo, (d)Divorciado: ")
while state_civil != 's' or state_civil != 'c' or state_civil != 'v' or state_civil != 'd':
    print("Estado civil informado inválido")
    state_civil = input("Informe seu estado civil novamente, (s)Solteiro, (c)Casado, (v)Viúvo, (d)Divorciado: ")

print("Informações Válidas")