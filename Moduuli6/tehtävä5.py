def poista_parittomat(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset
alkuperainen = [2,4,6,5,4,2,1,90,76,200,100,5,13,25,53]
karsittu = poista_parittomat(alkuperainen)
print('Alkuperäinen lista: ', alkuperainen)
print('Karsittu lista: ', karsittu)