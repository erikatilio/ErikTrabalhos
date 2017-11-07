pares = []
for g in range(5):
    x = int(input())
    if x % 2 == 0:
        pares.append(x)
print(int(len(pares)), "valores pares")