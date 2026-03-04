kayttaja = (input('Kerro nimesi: '))
if kayttaja == 'Matti' or kayttaja == 'matti':
    print('Seuraava, kiitos!')
else:
    annos = int(input('Montako keittoannosta: '))
    hinta = 5.90
    kokonaishinta = annos * hinta
    print(f'Kokonaishinta on: {kokonaishinta:.2f} ')
    print('Seuraava, kiitos!')