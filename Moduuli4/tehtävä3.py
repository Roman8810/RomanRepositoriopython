syote = (input('Anna jokin luku (tyhjä lopettaa toiminnon): '))
if syote =='':
    print('Toiminto lopetettu')
else:
    pienin = int(syote)
    suurin = int(syote)

    while True:
        syote = input('Anna jokin luku (tyhjä lopettaa toiminnon): ')
        if syote == '':
            print('Toiminto lopetettu')
            break
        luku = int(syote)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
    print('Pienin luku', pienin)
    print('Suurin luku', suurin)