def main():
    kenttä = {}
    while True:
        print('\nToiminnot: ')
        print('1. Lisää lentoasema')
        print('2. Hae lentoasema')
        print('3. Lopeta')
        valinta = input('Anna valinta: ')
        if valinta == '1':
            icao = input('Anna ICAO-koodi: ').upper()
            nimi = input('Anna lentoaseman nimi: ').upper()
            kenttä[icao]=nimi
            print('Tallennettu.')
        elif valinta == '2':
            icao = input('Anna ICAO-koodi: ').upper()
            print(kenttä.get(icao,'Lentoasemaa ei löytynyt.'))
        elif valinta == '3':
            print('Toiminto lopetettu.')
            break
        else:
            print('Virheellinen valinta')
if __name__ == '__main__':
    main()