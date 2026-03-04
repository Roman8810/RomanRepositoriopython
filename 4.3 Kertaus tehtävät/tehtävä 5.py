import math
while True:
    print('\nValitse laskutoimitus: ')
    print('1. Yhteenlasku')
    print('2. Vähennyslasku')
    print('3. Kertolasku')
    print('4. Jakolasku')
    print('5. Sulje laskin')
    valinta = input('Anna valinta (1-5): ')
    if valinta == '5':
        print('Laskin suljetaan')
        break
    if valinta in['1','2','3','4']:
        luku1 = float(input('Anna ensimmäinen luku: '))
        luku2 = float(input('Anna toinen luku: '))
        if valinta == '1':
            tulos = luku1 + luku2
            print(tulos)
        elif valinta == '2':
            tulos = luku1 - luku2
            print(tulos)
        elif valinta == '3':
            tulos = luku1 * luku2
            print(tulos)
            if luku2 == 0:
                print('Nollalla ei voi jakaa')
            else:
                tulos = luku1 / luku2
                print(tulos)
    else:
        print('Valitse numero 1-5. ')