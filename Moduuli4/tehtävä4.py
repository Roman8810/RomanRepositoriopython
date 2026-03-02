import random
arvaa = random.randint(1,10)
while True:
    arvaus = int(input('Arvaa luku väliltä 1-10: '))
    if arvaa < arvaus:
        print('Liian suuri arvaus')
    elif arvaa > arvaus:
        print('Liian pieni arvaus')
    else:
        print('Oikein!')
        break

