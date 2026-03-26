def suurin_arvo(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
luku1 = float(input('Anna luku 1: '))
luku2 = float(input('Anna luku 2: '))
luku3 = float(input('Anna luku 3: '))
tulos = suurin_arvo(luku1,luku2,luku3)
print('Suurin luku on:',tulos)