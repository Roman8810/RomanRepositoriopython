luvut = []
luku = input('Anna jokin luku tai lopeta painamalla enter: ')
while luku != '':
    luvut.append(float(luku))
    luku = input('Anna toinen luku tai lopeta painamalla enter: ')
luvut.sort(reverse=True)
while len(luvut) < 5:
    luvut.append(0)
print(luvut)
print('Viisi suurinta suurimmasta alkaen' ,luvut[:5])