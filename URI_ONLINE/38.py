pedido = input().split()
cod = int(pedido[0])
quant = int(pedido[1])

if cod == 1:
    p = 4*quant
    print("Total: R$ %.2f"%p)
if cod == 2:
    p = 4.5*quant
    print("Total: R$ %.2f"%p)
if cod == 3:
    p = 5*quant
    print("Total: R$ %.2f"%p)
if cod == 4:
    p = 2*quant
    print("Total: R$ %.2f"%p)
if cod == 5:
    p = 1.5*quant
    print("Total: R$ %.2f"%p)