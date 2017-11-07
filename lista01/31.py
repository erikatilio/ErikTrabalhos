# primeiro while para controlar o registro das compras
while True:
    print('Loja Tabajara')
    cont = 1
    total = 0
    # segundo while para calcular cada produto
    while True:
        valor = float(input("Produto {}: R$ ".format(cont)))
        cont += 1
        total += valor
        # se for digitado 0 encerra a compra
        if valor == 0:
            break
    # calculo do Total e troco
    print('Total: ', total)
    din = float(input('Dinheiro :'))
    # Condição do dinheiro for menor que o total
    if din >= total:
        troco = din - total
        print('Troco: ', troco)
    else:
        print('Dinheiro insuficiente')
        din = float(input('Dinheiro :'))
        troco = din - total
        print('Troco: ', troco)

    reset = input('Pressione 0 para reiniciar ou 1 para encerrar: ')
    if reset == '0':
        continue
    else:
        print('Finalizando compra')
    break