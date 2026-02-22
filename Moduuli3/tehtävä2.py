hytti = input('Syötä hyttiluokkasi, vaihtoehdoista LUX, A, B, C: ')
if hytti == 'LUX':
    print('Hyttisi on parvekkeellinen yläkannella')
elif hytti == 'A':
    print('Hyttisi on ikkunallinen, autokannen yläpuolella')
elif hytti == 'B':
    print('Hyttisi on ikkunaton, autokannen yläpuolella')
elif hytti == 'C':
    print('Hyttisi on ikkunaton, autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka')

