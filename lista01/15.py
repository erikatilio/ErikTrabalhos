#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo.
#-----------------------------------------------------------------------------------------------------------------------

n = int(input("digite o numero de termos que desea formar da serie de fibonacci: "))

c = 1
a = 0
b = 1
print(b)
while c < n:
    i = a + b
    print(i)
    a = b
    b = i
    c = c + 1
