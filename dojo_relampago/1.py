matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for x in range(4):
    c = x
    f = 4
    i = x
    while f > i:
        print(matriz[c][i])
        i += 1
