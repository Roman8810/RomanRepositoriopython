kaupungit = []
print('Anna viiden kaupungin nimet')
for i in range(5):
    kaupunki = input(f'{i+1}. Kaupunki: ')
    kaupungit.append(kaupunki)
print('\n Syötetyt kaupungit:')
for kaupunki in kaupungit:
    print(kaupunki)