pituus = float(input('Anna kuhan mitta senttimetreinä: '))
alamitta = 37
if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f'Kuha on alamittainen, laske kuha takaisin veteen')
    print(f'Pituudesta puuttuu {puuttuu:.1f} cm alimmasta sallitusta pyyntimitasta.')
else:
    print('Saat pitää kuhan')

