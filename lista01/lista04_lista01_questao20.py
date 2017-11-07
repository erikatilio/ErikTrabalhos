#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#Faça um Programa para leitura de três notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e presentar:
#a.A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#b.A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#c.A mensagem "Aprovado com Distinção", se a média for igual a 10.
#-----------------------------------------------------------------------------------------------------------------------

np1 = float(input("Informe sua primeira nota: "))
np2 = float(input("Informe sua segunda nota: "))
np3 = float(input("Informe sua terceira nota: "))
average = (np1+np2+np3)/3

if average == 10:
    print("Aprovado com Distinção")
else:
    if average >= 7:
        print("Aprovado")
    else:
        if average < 7:
            print("Reprovado")