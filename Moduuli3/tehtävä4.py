vuosi = int(input('Anna vuosiluku: '))
if vuosi % 400 == 0:
    print('Antamasi vuosi on karkausvuosi')
elif vuosi % 100 == 0:
    print('Antamasi vuosiluku ei ole karkausvuosi')
elif vuosi % 4 == 0:
    print('Antamasi vuosiluku on karkausvuosi')
else:
    print('Antamasi vuosiluku ei ole karkausvuosi')

