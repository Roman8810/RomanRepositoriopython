import math
def pizzan_hinta(halkaisija,hinta):
    sade_m = (halkaisija / 2) / 100
    pinta_ala = math.pi * sade_m ** 2
    return hinta / pinta_ala
halkaisija_1 = float(input('Anna pizzan 1 halkaisija (cm): '))
hinta_1 = float(input('Anna pizzan 1 hinta (eur): '))
halkaisija_2 = float(input('Anna pizzan 2 halkaisija (cm): '))
hinta_2 = float(input('Anna pizzan 2 hinta (eur): '))
yksi = pizzan_hinta(halkaisija_1,hinta_1)
kaksi = pizzan_hinta(halkaisija_2,hinta_2)
print('Pizzan 1 yksikköhinta (eur/m^2): ', round(yksi, 2))
print('Pizzan 2 yksikköhinta (eur/m^2): ', round(kaksi, 2))
if yksi < kaksi:
    print('Pizza 1 on edullisempi kukkarolle')
elif kaksi < yksi:
    print('Pizza 2 on edullisempi kukkarolle')
else:
    print('Molemmat pizza maksavat saman verran')