number_a = int(input())
number_b = int(input())

entre = []
aux = []
if number_a > number_b:
    for g in range(number_b,number_a):
        entre.append(g)
else:
    for g in range(number_a,number_b):
        entre.append(g)

for u in entre:
    if int(u) % 5 == 2 or int(u) % 5 == 3:
        aux.append(u)

for c in aux:
    print(c)