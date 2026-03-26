def kuusi(koko):
    print('Tämä on kuusi')
    for i in range(koko):
        print(' '* (koko - i - 1) +'*' *(2 * i + 1))
    print(' * ')
kuusi(5)