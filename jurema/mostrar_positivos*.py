numeros = input().split()
size = int(len(numeros))
if size > 10 and size < 0:
    while size > 10 and size < 0:
        numeros = input().split()
        size = int(len(numeros))
else:
     for g in numeros:
         if int(g) >= 0:
             print(g,end=" ")