n = int(input())
for g in range(1,n+1):
    if g % 2 == 0:
        e = int(g)
        d = e**2
        p = str(e) + str("^2 =")
        print(p,d)