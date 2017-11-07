#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
#magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
#seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
#programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
#magro, além da média das alturas e dos pesos dos clientes.
#-----------------------------------------------------------------------------------------------------------------------

mBaixo = 0
msAlto = 0
mediaAltura = 0
mediaPeso = 0
cont = 1
msGordo = 0
msMagro = 0

codigo =(int(input("Digite o Codigo: ")))

while codigo == 0:
    codigo = (int(input("Digite o Codigo: ")))

altura =(float(input("Digite a sua altura:")))
peso =(float(input("Digite seu peso:")))

mBaixo = altura
msAlto = altura
msGordo = peso
msMagro = peso
mediaAltura = altura
mediaPeso = peso

while codigo != 0:
    cont = cont + 1
    if (mBaixo > altura):
        mBaixo = altura
    if (msAlto < altura):
        msAlto = altura
    if (msMagro > peso):
        msMagro = peso
    if (msGordo < peso):
        msGordo = peso

    codigo = (int(input("Digite o Codigo: ")))
    if(codigo == 0):
        cont -= 1
        continue

    altura = (float(input("Digite a sua altura:")))
    peso = (float(input("Digite seu peso:")))

    mediaAltura += altura
    mediaPeso += peso

mediaAltura = mediaAltura / cont
mediaPeso = mediaPeso / cont

print(" Numero de pessoas",cont)
print(" O mais Alto",msAlto)
print(" O mais Baixo", mBaixo)
print(" A media da Altura :", mediaAltura)
print("A media do peso:", mediaPeso)
print(" O mais gordo e :", msGordo)
print(" O mais magro e :", msMagro)