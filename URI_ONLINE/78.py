x = int(input())
if 2 < x < 1000:
    for g in range(1,11):
        prod = x*g
        print(g,"X",x,"=",prod)