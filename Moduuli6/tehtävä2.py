import random
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
tahkot = int(input('Anna tahkojen määrä 6 tai 21: '))
while True:
    tulos = heita_noppaa(tahkot)
    print(tulos)
    if tulos == tahkot:
        print('Sait maksimiluvun!')
        break