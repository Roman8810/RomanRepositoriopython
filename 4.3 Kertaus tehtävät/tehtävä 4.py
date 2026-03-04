tarina = ''
while True:
    sana = input('Anna sana lisättäväksi tarinaan: ')
    if sana == 'Loppu' or sana == 'loppu':
        print('Tarina: ' , tarina)
        break
    else:
        tarina += sana +  " "