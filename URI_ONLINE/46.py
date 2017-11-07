tempo = input().split()
a1 = int(tempo[0])
a2 = int(tempo[1])
if a2 > a1:
    t = a2 - a1
    print("O JOGO DUROU",t,"HORA(S)")
elif a1 > a2:
    o = 24 - a1
    t = a2 + o
    print("O JOGO DUROU",t,"HORA(S)")
elif a1 == a2:
    print("O JOGO DUROU 24 HORA(S)")