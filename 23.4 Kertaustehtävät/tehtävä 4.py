import math
def piste(x,y):
    return x,y
def etaisyys(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
x1 = float(input('Anna piste x1: '))
y1 = float(input('Anna piste y1: '))
x2 = float(input('Anna piste x2: '))
y2 = float(input('Anna piste y2: '))
p1 = piste(x1,y1)
p2 = piste(x2,y2)
e  = etaisyys(p1,p2)
print('Piste 1: ',p1)
print('Piste 2: ',p2)
print('Etäisyys: ',round(e,2))