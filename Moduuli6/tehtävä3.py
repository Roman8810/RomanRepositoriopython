def gallona_litroiksi(gallonat):
    return gallonat * 3.785
while True:
    gallonat = float(input('Anna gallonamäärä, negatiivinen luku sulkee laskurin: '))
    if gallonat < 0:
        print('Toiminto lopetettu')
        break
    litrat = gallona_litroiksi(gallonat)
    print(litrat, 'litraa')