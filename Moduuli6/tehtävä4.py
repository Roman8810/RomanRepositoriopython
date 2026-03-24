def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa
numerot = [3,5,6,2,1,6,5,10]
tulos = laske_summa(numerot)
print('Listan summa on:', tulos)