sukupuoli = input('Oletko mies vai nainen?: ')
hemoglobiini = float(input('Anna hemoglobiiniarvosi (g/l): '))

if sukupuoli == 'nainen':
    if hemoglobiini < 117:
        print('hemoglobiiniarvosi on liian alhainen')
    elif hemoglobiini <= 175:
        print('hemoglobiiniarvosi on normaali')
    else:
        print('hemoglobiiniarvosi on liian korkea')
elif sukupuoli == 'mies':
    if hemoglobiini < 134:
        print('hemoglobiiniarvosi on liian alhainen')
    elif hemoglobiini <= 195:
        print('hemoglobiiniarvosi on normaali')
    else:
        print('hemoglbiiniarvosi on liian korkea')
else:
    print('tuntematon sukupuoli')

