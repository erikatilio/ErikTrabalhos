numeros = input().split()
x = numeros[0]
sim = 0
for i in numeros[1:]:
    if (x == i):
        sim += 1
if sim != 0:
    print("True")
else:
    print("False")