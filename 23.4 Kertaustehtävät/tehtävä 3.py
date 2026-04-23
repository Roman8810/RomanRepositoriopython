kirjasto = {'Tuntematon sotilas': ['Väinö Linna',1954,'Sotaromaani'],
            'Vanhus ja meri': ['Ernest Hemingway',1952,'Realismi'],
            'Monte Criston Kreivi': ['Alexandre Dumas',1844,'Seikkailuromaani'],
            'Sadan vuoden yksinäisyys': ['Gabriel Garcia Marquez',1967,'Realismi']}
print('Teoksen vanhus ja meri on kirjoittanut',kirjasto['Vanhus ja meri'][0],
      'ja Tuntemattoman sotilaan genre on',kirjasto['Tuntematon sotilas'][2])
kirjasto ['Kahden kaupungin tarina'] = ['Kahden kaupungin tarina',1859,'Historiallinen romaani']
del kirjasto['Tuntematon sotilas']
print('Päivitetty sanakirja: ')
for i in kirjasto.values():
    print(i)