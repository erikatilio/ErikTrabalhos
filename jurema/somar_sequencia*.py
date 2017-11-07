c = 1
vote = 0
while c != 0:
    s = input().split()
    for i in s:
        if int(i) > 9 or int(i) < -1:
            vote += 1
    n = s.index("-1")
    conta1 = []
    conta2 = []
    for g in s[:n]:
      conta1.append(g)
    for e in s[n + 1:]:
      conta2.append(e)
    if int(len(conta1)) != int(len(conta2)):
        vote += 1
    c = 0
if vote != 0:
    print("False")
elif vote == 0:
   n = s.index("-1")
   conta_m = []
   conta_n = []
   for g in s[:n]:
       conta_m.append(g)
   for e in s[n+1:]:
       conta_n.append(e)
   m = ("").join(conta_m)
   n = ("").join(conta_n)
   resultado = int(m) + int(n)
   print(resultado)