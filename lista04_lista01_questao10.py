#-------------------------------------------------------------------------------# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#10.Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
#-------------------------------------------------------------------------------
shift = input("Em que turno você estuda?(M-matutino,V-Vespertino e N-Noturno):")

if shift == "M" or shift == "m":
    print("Bom Dia!")
else:
    if shift == "V" or shift == "v":
            print("Boa Tarde!")
    else:
        if shift == "N" or shift == "n":
            print("Boa Noite!")
