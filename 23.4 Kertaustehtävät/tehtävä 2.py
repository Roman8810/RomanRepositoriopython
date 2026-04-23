oppilaat = {'Tupu': ['Tupu',7,'Fysiikka'],
            'Hupu': ['Hupu',7,'Liikunta'],
            'Lupu': ['Lupu',7,'Kemia'],}
print('Tupu on vuosiluokalla', oppilaat['Tupu'][1],'ja Hupun lempiaine on',oppilaat['Hupu'][2])
oppilaat ['Hupu'][2] = 'Biologia'
oppilaat ['Nupu'] = ['Nupu',7,'Matikka']
del oppilaat['Lupu']
print('Lopullinen sanakirja: ')
for i in oppilaat.values():
    print(i)