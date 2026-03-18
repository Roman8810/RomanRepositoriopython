maara = int(input('Kuinka monta arpakuutiota heitetään?: '))
import random
summa = 0
for i in range(maara):
    luku = random.randint(1, 6)
    print(luku)
    summa = summa + luku
print('Silmälukujen summa on: ',summa)