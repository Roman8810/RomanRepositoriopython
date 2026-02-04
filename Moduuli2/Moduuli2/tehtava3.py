
kanta_str = input('Anna suorakulmion kanta:  ')
korkeus_str = input('Anna suorakulmion korkeus:  ')

kanta = float(kanta_str)
korkeus = float(korkeus_str)

pinta_ala = (kanta*korkeus)
piiri = (2*kanta+2*korkeus)

print('Pinta-ala on: ' + str(pinta_ala))
print('Piiri on: ' + str(piiri))

