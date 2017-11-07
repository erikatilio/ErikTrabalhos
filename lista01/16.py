#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
#Faça um programa que gere a série até que o valor seja maior que 500.
#-----------------------------------------------------------------------------------------------------------------------

c = 1
a = 0
b = 1

print(a)
print(b)

while c < 500:
    fibo = a + b
    print(fibo)
    a = b
    b = fibo
    c = c + 1
    if fibo >= 500:
        break