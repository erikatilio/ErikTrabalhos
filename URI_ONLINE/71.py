x = int(input())
y = int(input())
soma = 0
if y < 0 < x:
    for g in range(y+1,x+1):
        if g % 2 != 0:
            soma += int(g)
elif y > 0 and x > 0:
    for e in range(y,x):
        if e % 2 != 0:
            soma+= int(e)
print(int(soma))