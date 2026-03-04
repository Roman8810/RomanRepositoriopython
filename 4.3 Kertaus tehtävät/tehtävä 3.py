from math import sqrt
while True:
 luku = float(input('Anna jokin luku: '))
 if luku == 0:
     print('Exiting...')
     break
 elif luku < 0:
     print('Virheellinen luku')
 else:
     print(sqrt(luku))