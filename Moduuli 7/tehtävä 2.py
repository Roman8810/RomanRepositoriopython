nimet = set()
while True:
    nimi = input('Anna nimi (tyhjä lopettaa toiminnon): ')
    if nimi == "":
        print('Toiminto lopetettu...')
        break
    if nimi in nimet:
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
        nimet.add(nimi)
        print(nimi)
print('Syötetyt nimet: ')
for nimi in nimet:
    print(nimi)
