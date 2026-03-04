tuntipalkka = float(input('Tuntipalkka: '))
tyotunnit = float(input('Tehdyt tunnit: '))
viikonpaiva = input('Viikonpäivä: ')
paivapalkka = tuntipalkka * tyotunnit
if viikonpaiva == 'Sunnuntai' or viikonpaiva == 'sunnuntai':
    paivapalkka = (tuntipalkka *2)*tyotunnit
else:
    paivapalkka = (tuntipalkka * tyotunnit)

print('Tuntipalkka: ',tuntipalkka)
print('Työtunnit: ',tyotunnit)
print('Viikonpäivä: ',viikonpaiva)
print(f'Päiväpalkka: {paivapalkka:.2f}')

    

