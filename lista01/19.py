#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
#-----------------------------------------------------------------------------------------------------------------------

number = int(input("Digite quantos números serão inputados?(entre 0 e 10000): "))

c = 0
sum = 0

while number < 0 or number > 10000:
    print("Digite entre 0 e 10000!")
    number = int(input("Digite quantos números serão inputados?(entre 0 e 10000): "))

x = int(input())
larger = x
smaller = x

while c < number-1:
    x = int(input())
    if x < smaller:
        larger = x
    if x > larger:
        larger = x
    c = c + 1
    sum = sum + x

print("Menor valor: %d" % smaller)
print("Maior valor: %d" % larger)
print("Soma: %d" % (sum +1))