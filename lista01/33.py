n = int(input("Quantas temperaturas serão informadas?\n"))
i = 0
temp =  int(input("Temperatura: "))
maior = temp
menor = temp
soma = temp
while i<n-1:
    temp =  int(input("Temperatura: "))
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    soma+=temp
    i+=1
media = soma/n
print ("Maior temperatura: %d" % maior)
print ("Menor temperatura: %d" % menor)
print ("Média das temperaturas: %d" % media)