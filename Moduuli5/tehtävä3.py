kokonaisluku = int(input('Anna jokin kokonaisluku: '))
alkuluku = True
if kokonaisluku < 2:
    alkuluku = False
else:
    for i in range(2, kokonaisluku):
        if kokonaisluku % i == 0:
            alkuluku = False
            break
if alkuluku:
    print(kokonaisluku, 'on alkuluku')
else:
    print(kokonaisluku, 'ei ole alkuluku')
