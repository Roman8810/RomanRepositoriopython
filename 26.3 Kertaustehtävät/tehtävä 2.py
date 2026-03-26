luvut = []
luku = int(input('Anna jokin luku, 0 lopettaa toiminnon: '))
while luku != 0:
    luvut.append(luku)
    print('Lista', luvut)
    print('Järjestettynä', sorted(luvut))
    luku = int(input('Anna jokin luku, 0 lopettaa: '))